from BayesClassifier import *

c = BayesClassifier()
c.train("data/simple.data")
# c.load("data/movies.data.pickle")
# c.train("data/movies.data")
print c.classify("I loved it")
print c.classify("I thought I hated it but loved it")
