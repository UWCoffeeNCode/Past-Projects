from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

CORPUS = [
    "buy pills",
    "i love cats",
    "do you want free money",
    "i love dogs too"
] 
y = [1, 0, 1, 0]

vectorizer = CountVectorizer()
vectorizer.fit(CORPUS)

X = vectorizer.transform(CORPUS)

classifier = MultinomialNB() 
classifier.fit(X, y)

tests = [
    "Dear sir, you have won one million money",
    "Lucy, I really love your pet cat"
]
test_vectors = vectorizer.transform(tests)
print(classifier.predict(test_vectors))
