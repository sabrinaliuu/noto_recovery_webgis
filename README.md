# Life Recovery after Noto Peninsula Earthquake
<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/ChatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/QGIS-93b023?style=for-the-badge&logo=qgis&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white" />
  <img src="https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white" />
  <img src="https://img.shields.io/badge/Leaflet-199900?style=for-the-badge&logo=Leaflet&logoColor=white" />
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" /></br>
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white" />
  <img src="https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white" />
  <img src="https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white" />
  <img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" />
</p>

<p>
  🥇<b>[2026/04/20 update] New version for C# ASP.NET (deploy on AZURE)</b></br>
  ⚫<a href="https://github.com/sabrinaliuu/noto_recovery_webgis_">Github</a>
  🔵<a href="https://notorecovery-fmdvf9cucdbpgacw.canadacentral-01.azurewebsites.net">Website</a>
</p>

## About the website
https://sabrinaliuu.github.io/noto_recovery_webgis/

<img width="812" height="468" alt="noto_gis" src="https://github.com/user-attachments/assets/3b0c0d08-13a0-4575-8e3f-6097ab97064d" />

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
