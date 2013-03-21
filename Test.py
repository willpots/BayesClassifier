from BayesClassifier import *

c = BayesClassifier()
# c.train("data/simple.data")
# c.train("data/movies.data")
c.load("data/movies.data.pickle")
print c.classify("I loved it")
print c.classify("I thought I hated it but loved it")
print c.classify("I hated the movie. There was nothing good about it and it generally disgusted me.")
print c.classify("I loved and hated it")
print c.classify("I liked parts of it and but really hated it")
print c.classify("No one in the theatre could stand the movie")
print c.classify("You must see this movie!")
print c.classify("I love my AI class!")