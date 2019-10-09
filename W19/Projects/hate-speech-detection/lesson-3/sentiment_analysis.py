import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import f1_score

class SentimentAnalysis:
    """ Trains a ML model to identify the sentiment of short text messages
    """
    def __init__(self):
        # Unpack and store data in class variables
        dataset = pd.read_pickle("./sentiment_data.pkl")[["text", "sentiment"]].values
        self.corpus = [row[0] for row in dataset]
        self.tags = [row[1] for row in dataset]

        # Needed to make predictions on future data
        self.vectorizer = None
        self.model = None
        self.metrics = None
    
    def train(self, method="bag_of_words"):
        """ Trains the ML model based on a given feature selection method
        """
        # Splits the dataset into an 80/20 train-test ratio
        x_train, x_test, y_train, y_test = train_test_split(
            self.corpus, 
            self.tags, 
            test_size=0.2, 
            stratify=self.tags
        )

        # Chooses our given feature selection method
        if method == "bag_of_words":
            self.vectorizer = CountVectorizer()
        elif method == "bigrams":
            self.vectorizer = CountVectorizer(ngram_range=(2, 2))
        elif method == "tf_idf":
            self.vectorizer = TfidfVectorizer()
        else:
            print("Invalid method given to .train()")

        # Vectorizes text into word vectors
        self.vectorizer.fit(x_train)
        x_train = self.vectorizer.transform(x_train)
        x_test = self.vectorizer.transform(x_test)

        # Training our machine learning model
        self.model = MultinomialNB()
        self.model.fit(x_train, y_train)

        # Computes the F1-score of our model
        self.metrics = f1_score(self.model.predict(x_test), y_test)

    def evaluate(self):
        """ Returns the model's F1-score
        """
        return self.metrics
    
    def predict(self, corpus):
        """ Returns sentiment predictions on a corpus on text
        """
        word_vectors = self.vectorizer.transform(corpus)
        return self.model.predict(word_vectors)
