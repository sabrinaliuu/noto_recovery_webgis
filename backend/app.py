from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()
my_api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json
    text = data.get("text")
    json_string = {
        "elements": recovery_element(text),
        "places":  extract_cities(text),
        "sentiment": ChatGPT_sentiment(text)
    }
    print(jsonify(json_string))
    return jsonify(json_string)

# Location
cities = ['珠洲市', '羽咋市', '志賀町', '宝達志水町', '七尾市', '能登町', '輪島市', '内灘町', 'かほく市', '穴水町', '津幡町', '中能登町']

def extract_cities(text):

    sorted_cities = sorted(cities, key=len, reverse=True)
    found = []
    remaining_text = text

    for city in sorted_cities:
        if city in remaining_text:
            found.append(city)
            remaining_text = remaining_text.replace(city, "")

    return found

# Recovery Elements
seven = ["housing", "social ties", "townscape", "physical and mental health", "preparedness", "relation to government", "economic and financial situation"];
keywords = {"1": ["仮設住宅", "半壊", "全壊","住宅被害", "家屋","住まい","再建","住宅","住民","建物", "家は","家で"],
            "2": ["祭り", "まつり", "協力", "ボランティア", "絆","祈願","祈り"],
            "3": ["土砂崩落", "人口", "開通","解体","朝市","交通","インフラ","鉄道","開通"],
            "4": ["不安", "沈む", "絶望", "痛む", "希望", "元気","寂しい","悲しい","うれしい"],
            "5": ["防災","整備","備え"],
            "6": ["アンケート", "公的支援", "政府", "公費","支援","取り組み","行政","予算"],
            "7": ["仮設商店","寄付", "義援金", "奨学金", "輪島塗", "ツアー", "輪島朝市", "住宅ローン", "再開","支援"]}
def recovery_element(text):
    seven_result = []
    for k in range(1,8):
        keyword = keywords[str(k)] 
        label = [1 for word in keyword if word in text ]
        if len(label)>0:
            seven_result.append(seven[k-1])
    return seven_result

# Sentiment Analysis (GPT)
client = OpenAI( api_key=  my_api_key) # testing only API key
def ChatGPT_sentiment(text):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[{
                    "role": "system",
                    "content": """
                                災害復興に関する文章を読んで、感情分析してください。
                                ポジは１、ネガはー１、なしは０、感情分析の結果だけ教えてください。
                                例：
                                イベントは令和6年能登半島地震の影響により開催を延期し、10月5日の5日間で開催される。
                                感情分析の結果はなし、
                                "0" だけ返事してください。
                                """
                },
                {
                    "role": "user",
                    "content": text
                }]
    )
    result = completion.choices[0].message.content

    sentiments = {"1": ["Positive"],"0": ["Neutral"], "-1": ["Negative"]}
    return sentiments[result][0]

if __name__ == "__main__":
    app.run(debug=True)