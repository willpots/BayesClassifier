
# 1. Call this line to resplit data
# Should resplit fairly often.
# from BayesClassifierBest import *
# split("data/movies.data", "data/movies_test")

# 2. Test 5 specific phrases (This is what he is looking for in Writeup number 2) 
# from BayesClassifierBest import *
# c = BayesClassifier()

# c.train("data/movies_test.train")

# print c.classify("coyote ugly has no plot . the storyline is as skimpy as the costumes the women at the bar wear . it's a poor attempt at a remake of flashdance and its major audience seems to be lonely lonely teenage boys with no access to porn .")
# print c.classify("so stupid and juvenile this film is ! i can't believe that this was based on shakespeare ! this movie was too cheesy for me to withstand ! ( and i usually like bad b-grade movies too ! )")
# print c.classify("and nasty film by a director whose stock in trade is over the top unpleasantness e . g . the fury . de palma has to be one of the worst film makers of all time , right down there with tarantino and david lynch . if you want to see how gangster films should be done stick with coppola and scorsese .")
# print c.classify("this movie is smart , funny , and hits the spirit of corporate america right in the gonads . in the lines of catch-22 , this movie is brilliant , i loved it .")
# print c.classify("beautifully depicted the life of the french indian war . good battle scenes , with a romantic and heroic fame to it .")



# 3. Use these four lines to test classifier on a large subset of data. Output will be logged to ouputFile.txt
# This gives us our accuracy rate.
from BayesClassifierBest import *
c = BayesClassifier()
c.train("data/movies_test.train")
print c.test("data/movies_test.test", "outputFile.txt")






# MISC TESTING LINES
# split("data/movies.data", "data/movies_test")
# c.train("data/simple.data")
# c.train("data/movies.data")
# c.load("data/movies.data.pickle")
# c.train("data/20news.data")
# c.load("data/20news.data.pickle")


