# Data Processing Libraries
import pandas

# Machine Learning Tools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Natural Language Processing Tools
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
import re


class HateSpeechDetection:
  def __init__(self):
    self.corpus = None
    self.tags = None
    self.vectorizer = None
    self.model = None
    self.metrics = None
  
  def _simplify(self, corpus):
    """ Take in a corpus and removes stopwords, 
        converts to lowercase, removes non-alpha-numeric characters,
        and stems each word
    """

    stop_words = set(stopwords.words('english'))
    stemmer = SnowballStemmer('english')

    def clean(text):
      """ Example:
          input: "I really love my dog Lulu!"
          output: "i real love my dog lulu"
      """
      text = re.sub(r"[^a-zA-Z0-9]", " ", text)
      words = [stemmer.stem(w) for w in word_tokenize(text.lower()) if w not in stop_words]
      return " ".join(words)
    
    return [clean(text) for text in corpus]
  
  def _model_metrics(self, feature_vectors, tags):
    """ Takes in testing data and computes f1-score
    """

    tp = 0
    fp = 0
    tn = 0
    fn = 0

    predictions = self.model.predict(feature_vectors)
    for r in zip(predictions, tags):
      if r[0] == 1 and r[1] == 1:
        tp += 1
      elif r[0] == 1 and r[1] == 0:
        fp += 1
      elif r[0] == 0 and r[1] == 0:
        tn += 1
      else:
        fn += 1
      
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1 = (2 * precision * recall) / (precision + recall)

    return {
      'precision': precision,
      'recall': recall,
      'f1': f1
    }

  def load_corpus(self, path, corpus_col, tag_col):
    """ Reads in path to a data file, and selects the columns containing
        the corpus and its subsequent tags
    """
    data = pandas.read_pickle(path)[[corpus_col, tag_col]].values
    self.corpus = [row[0] for row in data]
    self.tags = [row[1] for row in data]
  
  def train(self):
    """ Trains a ML model to detect hate speech
    """
    corpus = self._simplify(self.corpus)
    self.vectorizer = TfidfVectorizer()
    self.vectorizer.fit(corpus)

    word_vectors = self.vectorizer.transform(corpus)
    x_train, x_test, y_train, y_test = train_test_split(word_vectors, self.tags, train_size=0.8, stratify=self.tags)

    self.model = MultinomialNB()
    self.model.fit(x_train, y_train)

    self.metrics = self._model_metrics(x_test, y_test)

  def predict(self, text):
    """ Takes in a single message and checks if it is hate speech
    """
    text = [text]
    features = self.vectorizer.transform(text)
    return self.model.predict(features)
  
  def score(self):
    """ Returns model performance metrics
    """
    return self.metrics


if __name__ == "__main__":
    hsd = HateSpeechDetection()
    hsd.load_corpus("data.pkl", "tweet", "class")
    hsd.train()
    while True:
        query = input("Enter Query: ")
        if hsd.predict(query):
            print("Hate Speech Detected!")
        else:
            print("No Hate Speech Detected")
