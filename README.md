# Life Recovery after Noto Peninsula Earthquake
<b>[2026/04/20 update] New version for C# ASP.NET (deploy on AZURE)</b></br>
⚫<a href="https://github.com/sabrinaliuu/noto_recovery_webgis_">Github</a>
🔵<a href="https://notorecovery-fmdvf9cucdbpgacw.canadacentral-01.azurewebsites.net">Website</a>
## About the website
https://sabrinaliuu.github.io/noto_recovery_webgis/
### Introduction
This is a website that visualizes the study <i>Analyzing the Seven Critical Elements of Life Recovery Using News: A Case Study of the 2024 Noto Peninsula Earthquake</i> by Yen-Ching Liu* and Shosuke Sato.

This website is produced by Yen-Ching Liu with Gemini.
### Interface
#### Map and Charts
You can select <b>Recovery Element and Month</b>.
The sentiment composition for each city will show on the map in a pie chart and under the map in a bar chart.<br>
As you select the pie chart, the details for the change in sentiment will display on the left.

#### Recognition: NLP Model Application
You can enter a recovery-related sentence in <b>Japanese</b> here.<br>
The <b>Life Recovery Elements, Cities in Noto Peninsula, and Sentiment </b> will be recognized by our NLP models and displayed.

### Tools
GitHub Pages (Frontend) + Render (Backend) by Flask

## About the study
In this study, NLP methods were applied to recognize the <b>recovery elements (keyword-based approach), sentiments (GPT-based approach), and locations (keyword-based approach)</b> in each paragraph. In other words, the textual data was converted into numerical data for further quantitative analysis.

Details are provided below: 
* Material: News on the Yahoo! Japan News website
* Time: August 2024 to July 2025
* Seven Critical Elements for Life Recovery: housing, social ties, townscape, physical and mental health, preparedness, relation to government, and economic and financial situation (Tatsuki and Hayashi, 2002)
* Sentiments: positive, negative, and neutral
* 12 cities in Ishikawa Prefecture on the Noto Peninsula: Suzu-shi (珠洲市), Wajima-shi (輪島市), Noto-cho (能登町), Anamizu-machi (穴水町), Shika-machi (志賀町), Nanao-shi (七尾市), Nakanoto-machi (中能登町), Hakui-shi (羽咋市), Hodatsushimizu-cho (宝達志水町), Kahoku-shi (かほく市), Uchinada-machi (内灘町), Tsubata-machi (津幡町)

This demonstrates the feasibility of using NLP methods on news data to gain insights into news media perceptions and to assess news coverage of disaster recovery.

Note: Manuscript under review
