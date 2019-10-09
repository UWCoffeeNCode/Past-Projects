import pandas as pd

# Read CSV file into Pandas Dataframe
# Rename columns of dataframe
df = pd.read_csv("sentiment_analysis_twitter_data.csv", encoding="utf-8")
df.columns = [
  'sentiment', 
  'user_id', 
  'time', 
  'query', 
  'user_name', 
  'text'
]

# Trim dataframe to relevant columns
# Re-label positive from "4" to "1"
df = df[['sentiment', 'text']]
df['sentiment'] = df['sentiment'].map({0: 0, 4: 1})

# Extract 1000 examples each of positive and negative tweets
negative = df.loc[df['sentiment'] == 0, ['sentiment', 'text']].head(1000)
positive = df.loc[df['sentiment'] == 1, ['sentiment', 'text']].head(1000)


# Create our final dataset and pickle it for later
df = pd.concat([negative, positive])
df.to_pickle("sentiment_data.pkl")
