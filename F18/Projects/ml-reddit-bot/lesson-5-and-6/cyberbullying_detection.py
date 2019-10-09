# Data processing tools
import praw
import pickle
import pandas
import numpy

# Machine Learning Tools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

# Natural Language Processing Tools
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize 
from nltk.stem.snowball import SnowballStemmer
import re


class CyberbullyingDetectionEngine:
    """ Class that deals with training and deploying cyberbullying detection models
    """
    def __init__(self):
        self.corpus = None
        self.tags = None
        self.lexicons = None
        self.vectorizer = None
        self.model = None
        self.metrics = None
    
    class CustomVectorizer:
        """ Extracts features from text and vectorizes them
        """
        def __init__(self, lexicons):
            self.lexicons = lexicons

        def transform(self, corpus):
            """ Returns a numpy array of word vectors
            """
            word_vectors = []
            for text in corpus:
                features = []
                for k, v in self.lexicons.items():
                    features.append(len([w for w in word_tokenize(text) if w in v]))

                word_vectors.append(features)

            return numpy.array(word_vectors)

    def _simplify(self, corpus):
        """ Takes in a list of strings and removes stopwords, converts to lowercase,
            removes non-alphanumeric characters, and stems each word
        """
        stop_words = set(stopwords.words('english'))
        stemmer = SnowballStemmer('english')
        
        def clean(text):
            text = re.sub('[^a-zA-Z0-9]', ' ', text)
            words = [stemmer.stem(w) for w in word_tokenize(text.lower()) if w not in stop_words] 
            return " ".join(words)

        return [clean(text) for text in corpus]
    
    def _get_lexicon(self, path):
        """ Takes in a path to a text file and returns a set
            containing every word in the file
        """
        words = set()
        with open(path) as file:
            for line in file:
                words.update(line.strip().split(' '))

        return words

    def _model_metrics(self, features, tags):
        """ Takes in testing data and returns a dictionary of metrics
        """
        tp = 0
        fp = 0
        tn = 0
        fn = 0

        predictions = self.model.predict(features)
        for r in zip(predictions, tags):
            if r[0] == 1 and r[1] == 1:
                tp += 1
            elif r[0] == 1 and r[1] == 0:
                fp += 1
            elif r[0] == 0 and r[1] == 1:
                fn += 1
            else:
                tn += 1
        
        precision = tp / (tp + fp)
        recall = tp / (tp + fn)
        return {
            'precision': precision,
            'recall': recall,
            'f1': (2 * precision * recall) / (precision + recall)
        }

    def load_corpus(self, path, corpus_col, tag_col):
        """ Takes in a path to a pickled pandas dataframe, the name of the corpus column,
            and the name of the tag column, and extracts a tagged corpus
        """
        data = pandas.read_pickle(path)[[corpus_col, tag_col]].values
        self.corpus = [row[0] for row in data]
        self.tags = [row[1] for row in data]

    def load_lexicon(self, fname):
        """ Loads a set of words from a txt file
        """
        if self.lexicons is None:
            self.lexicons = {}
        
        self.lexicons[fname] = self._get_lexicon('./data/' + fname + '.txt')
        
    def load_model(self, model_name):
        """ Loads a ML model, it's corresponding feature vectorizer, and it's performance metrics
        """
        self.model = pickle.load(open('./models/' + model_name + '_ml_model.pkl', 'rb'))
        self.vectorizer = pickle.load(open('./models/' + model_name + '_vectorizer.pkl', 'rb'))
        self.metrics = pickle.load(open('./models/' + model_name + '_metrics.pkl', 'rb'))
    
    def train_using_bow(self):
        """ Trains a model using Bag of Words on the loaded corpus and tags
        """
        corpus = self._simplify(self.corpus)
        self.vectorizer = CountVectorizer()
        self.vectorizer.fit(corpus)

        bag_of_words = self.vectorizer.transform(corpus)
        x_train, x_test, y_train, y_test = train_test_split(bag_of_words, self.tags, test_size=0.2, stratify=self.tags)

        self.model = MultinomialNB()
        self.model.fit(x_train, y_train)

        self.metrics = self._model_metrics(x_test, y_test)

    def train_using_tfidf(self):
        """ Trains a model using tf-idf weighted word counts as features
        """
        corpus = self._simplify(self.corpus)
        self.vectorizer = TfidfVectorizer()
        self.vectorizer.fit(corpus)

        word_vectors = self.vectorizer.transform(corpus)
        x_train, x_test, y_train, y_test = train_test_split(word_vectors, self.tags, test_size=0.2, stratify=self.tags)

        self.model = MultinomialNB()
        self.model.fit(x_train, y_train)

        self.metrics = self._model_metrics(x_test, y_test)

    def train_using_custom(self):
        """ Trains model using a custom feature extraction approach
        """
        corpus = self._simplify(self.corpus)
        self.vectorizer = self.CustomVectorizer(self.lexicons)
        
        word_vectors = self.vectorizer.transform(corpus)
        x_train, x_test, y_train, y_test = train_test_split(word_vectors, self.tags, test_size=0.2, stratify=self.tags)

        self.model = SVC()
        self.model.fit(x_train, y_train)

        self.metrics = self._model_metrics(x_test, y_test)

    def evaluate(self):
        """ Returns a dictionary of model performance metrics
        """
        return self.metrics

    def save_model(self, model_name):
        """ Saves the model for future use
        """
        pickle.dump(self.model, open('./models/' + model_name + '_ml_model.pkl', 'wb'))
        pickle.dump(self.vectorizer, open('./models/' + model_name + '_vectorizer.pkl', 'wb'))
        pickle.dump(self.metrics, open('./models/' + model_name + '_metrics.pkl', 'wb'))

    def predict(self, corpus):
        """ Takes in a text corpus and returns predictions
        """
        x = self.vectorizer.transform(self._simplify(corpus))
        return self.model.predict(x)

if __name__ == '__main__':
    reddit = praw.Reddit(
        client_id = 'rFp_QaS7A2NlHw',  
        client_secret = 'IuLWUdlgRYJaF3ARpfhgQrQ1Yw4',
        user_agent = 'script_name by /u/username' 
    )

    new_comments = reddit.subreddit('TwoXChromosomes').comments(limit=1000)
    queries = [comment.body for comment in new_comments]

    engine = CyberbullyingDetectionEngine()
    engine.load_corpus('./data/final_labelled_data.pkl', 'tweet', 'class')

    engine.load_model('bow')
    print(engine.evaluate())
    print(engine.predict(queries))

    engine.load_model('tfidf')
    print(engine.evaluate())
    print(engine.predict(queries))

    engine.load_model('custom')
    print(engine.evaluate())
    print(engine.predict(queries))
