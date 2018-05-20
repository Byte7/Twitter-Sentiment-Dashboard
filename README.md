# Twitter-Sentiment-Dashboard
A twitter sentiment analysis dashboard made using Dash ⚡️
Dash is developed by Plotly.

## How to run the app

1. Sign into Twitter dev site (https://apps.twitter.com/). You'll need a twitter account for the same, so make sure you have one already or make a new one!
2. Click on create new app. Name your app, write a small description and related urls. One can change url later through settings.
3. After creating new app, generated api key will be displayed. Below api key, there is a option to generate access token and access secret. Generate access token and secret.
3. Fill the api key, api secret, access token, access secret in twitter_senti_dashboard.py
4. Run both files simultaneously.
5. View dashboard at `localhost:8050`.

## Make it yours
Currently the sentiment scores are calculated for tweets of topic `sports`.
You can change this line `twitterStream.filter(track=["sports"])` in the twitter_senti_dashboard.py file to track scores of any other topic.