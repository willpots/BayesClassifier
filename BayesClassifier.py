# Name: 
# Date:
# Description:
#
#

import math, os, pickle
from DataReader import *

class BayesClassifier:

   def __init__(self):
      '''This method initializes the Naive Bayes classifier'''
      self.wc_neg = {}
      self.wc_pos = {}
      self.wc_total = {}
      self.n_pos = 0
      self.n_neg = 0


   def train(self, dataFile):   
      '''Trains the Naive Bayes Sentiment Classifier.'''
      dr = DataReader(dataFile)

      label, data = dr.next()
      while(label):
         if label == "positive":
            self.n_pos += 1
         elif label == "negative":
            self.n_neg += 1
         for i in range(len(data)):
            if label == "positive":
               if data[i] in self.wc_pos:
                  self.wc_pos[data[i]] += 1
               else:
                  self.wc_pos[data[i]] = 1
            elif label == "negative":
               if data[i] in self.wc_neg:
                  self.wc_neg[data[i]] += 1
               else:
                  self.wc_neg[data[i]] = 1
         label, data = dr.next()
      self.save(dataFile+"_data.data")


   def classify(self, sText):
      '''Given a target string sText, this function returns the most likely document
      class to which the target string belongs (i.e., positive or negative ).
      '''

   def save(self, sFilename):
      '''Save the learned data during training to a file using pickle.'''

      f = open(sFilename, "w")
      p = pickle.Pickler(f)
      # use dump to dump your variables
      p.dump(self.wc_pos)
      p.dump(self.wc_neg)
      p.dump(self.wc_total)
      p.dump(self.n_pos)
      p.dump(self.n_neg)
      f.close()
   
   def load(self, sFilename):
      '''Given a file name of stored data, load and return the object stored in the file.'''

      f = open(sFilename, "r")
      u = pickle.Unpickler(f)
      # use load to load in previously dumped variables
      u.load(self.wc_pos)
      u.load(self.wc_neg)
      u.load(self.wc_total)
      u.load(self.n_pos)
      u.load(self.n_neg)
      f.close()
