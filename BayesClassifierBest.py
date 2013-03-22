# Name: Parker Woodworth and Will Potter
# Date: 03/21/2013
# Description: Our awesome BayesClassifier
#
#

import math, os, pickle
from DataReader import *


class BayesClassifier:

   def __init__(self):
      '''This method initializes the Naive Bayes classifier'''
      self.word_counts = {} # Dictionary of dictionaries. Label as first key, word as second key
      self.docs = {} # Label is the key. Total docs / label
      self.word_sums = {} # Label is the key. Total # of words / label
      self.total_docs = 0

   def train(self, dataFile):   
      '''Trains the Naive Bayes Sentiment Classifier.'''
      dr = DataReader(dataFile)

      label, data = dr.next()
      while(label):
         try:
            if label not in self.word_counts:
               self.word_counts[label] = {}

            if label in self.docs:
               self.docs[label] += 1
            else:     
               self.docs[label] = 1
            self.total_docs += 1   

            for i in range(len(data)/2): #implementing bigrams instead of unigrams
               j = 2i
               bigram = data[j] + " " + data[j+1]
               if bigram in self.word_counts[label]:
                  self.word_counts[label][bigram] += 1
                  if data[j].isupper():
                     self.word_counts[label][bigram] += .5 # counts a word an extra half time if it is all caps
                  if data[j+1].isupper():
                     self.word_counts[label][bigram] += .5 # counts a word an extra half time if it is all caps
               else:
                  self.word_counts[label][bigram] = 1

            label, data = dr.next()


         except StopIteration:
            # Calculate the total number of words / label
            for label, label_words in self.word_counts.items():
               self.word_sums[label] = 0
               for word, word_count in label_words.items():
                  self.word_sums[label] += word_count                     

            self.save(dataFile+".pickle")
            return



   def classify(self, sText):
      '''Given a target string sText, this function returns the most likely document
      class to which the target string belongs (i.e., positive or negative ).
      '''
      words = tokenize(sText)
      probs = {}



      # Calculate probability for each label
      for label, label_words in self.word_counts.items():
         
         # Calculate label probability
         probs[label] = math.log(float(self.docs[label])/float(self.total_docs)) # Start off with p(label)

         # Calculate probability for each word
         for word in words:
            if word in self.word_counts[label]:
               probs[label] += math.log(float(self.word_counts[label][word]) / float(self.word_sums[label]))
            else:
               probs[label] += math.log(.05)

      # Now find the maximum probability
      prob_label, prob_number = "NONE", -1000

      for key, value in probs.items():
         print key, value
         if value > prob_number:

            prob_label, prob_number = key, value

      print probs

      return prob_label, prob_number


   def save(self, sFilename):
      '''Save the learned data during training to a file using pickle.'''

      f = open(sFilename, "w")
      p = pickle.Pickler(f)
      # use dump to dump your variables
      p.dump(self.word_counts)
      p.dump(self.docs)
      p.dump(self.word_sums)
      p.dump(self.total_docs)
      f.close()
   
   def load(self, sFilename):
      '''Given a file name of stored data, load and return the object stored in the file.'''

      f = open(sFilename, "r")
      u = pickle.Unpickler(f)
      # use load to load in previously dumped variables
      self.word_counts = u.load()
      self.docs = u.load()
      self.word_sums = u.load()
      self.total_docs = u.load()
      f.close()