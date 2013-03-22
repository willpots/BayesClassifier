from BayesClassifierBest import *

c = BayesClassifier()

c.train("data/movies_test.train")
c.test("data/movies_test.test", "outputFile.txt")

split("data/movies.data", "data/movies_test")
# c.train("data/simple.data")
# c.train("data/movies.data")
c.load("data/movies.data.pickle")
# c.train("data/20news.data")
# c.load("data/20news.data.pickle")





