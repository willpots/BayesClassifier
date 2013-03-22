from BayesClassifier import *

c = BayesClassifier()

# c.train("data/movies_test.train")
# c.test("data/movies_test.test", "outputFile.txt")

# split("data/movies.data", "data/movies_test")
# c.train("data/simple.data")
# c.train("data/movies.data")
c.load("data/movies.data.pickle")
# c.train("data/20news.data")
# c.load("data/20news.data.pickle")


print c.classify("I loved it")
print c.classify("I thought I hated it but loved it")
print c.classify("I hated the movie. There was nothing good about it and it generally disgusted me.")
print c.classify("I loved and hated it")
print c.classify("I liked parts of it and but really hated it")
print c.classify("No one in the theatre could stand the movie")
print c.classify("You must see this movie!")
print c.classify("I love my AI class!")

# print c.classify("AMERICAN ATHEIST PRESS AAP publish various atheist books -- critiques of the Bible, lists of Biblical contradictions, and so on.  One such book is:")
# print c.classify(": I am a new reader of sci.crypt I would like to obtain a copy of a : public domain program that can encrypt files, preferably using DES, : that runs under MS-DOS. : I would also like to obtain a program which will password protect : floppy disks, if this is possible. : Thanks. : David Maddison: Melbourne, Australia")


