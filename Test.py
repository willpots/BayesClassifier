from BayesClassifier import *

c = BayesClassifier()
c.load("data/movies.data.pickle")
print c.classify("I love my AI class!")
print c.classify("I hate my AI class!")
print c.classify("I absolutely detest that")

