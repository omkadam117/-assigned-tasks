import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

# Load the Twitter data
twitter_data = pd.read_csv("twitter_entity_sentiment_analysis.csv")

# Explore the data
print(twitter_data.head())
print(twitter_data.info())

# Handle missing values
twitter_data.dropna(inplace=True)

# Calculate sentiment scores
def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

twitter_data["sentiment_score"] = twitter_data["text"].apply(get_sentiment)

# Visualize sentiment distribution
sns.histplot(twitter_data["sentiment_score"], bins=30)
plt.title("Distribution of Sentiment Scores")
plt.xlabel("Sentiment Score")
plt.ylabel("Frequency")
plt.show()

# Visualize sentiment over time (assuming you have a 'created_at' column)
twitter_data["created_at"] = pd.to_datetime(twitter_data["created_at"])
sns.lineplot(x="created_at", y="sentiment_score", data=twitter_data)
plt.title("Sentiment Over Time")
plt.xlabel("Date")
plt.ylabel("Sentiment Score")
plt.show()

# Visualize sentiment by entity (assuming you have an 'entity' column)
sns.boxplot(x="entity", y="sentiment_score", data=twitter_data)
plt.title("Sentiment by Entity")
plt.xlabel("Entity")
plt.ylabel("Sentiment Score")
plt.show()