# -*- coding: utf-8 -*-
"""
Created on Wed Sep 1 00:33:39 2021

@author: joseph
"""
#import nltk
#nltk.download()
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

#read the input file
f = open('input.txt','r')
text = f.read()

#split the text into sentences
sentences = tokenize.sent_tokenize(text)

pos_score_sum = 0
comp_score_sum = 0
neg_score_sum = 0

SIA = SentimentIntensityAnalyzer()

#sum the polarity scores of each sentences
for sentence in sentences:
    comp_score_sum += SIA.polarity_scores(sentence)['compound']
    pos_score_sum += SIA.polarity_scores(sentence)['pos'] 
    neg_score_sum += SIA.polarity_scores(sentence)['neg'] 

print("Average overall score: ")
#average the sum of scores

print("positive score", pos_score_sum/len(sentences))
print("negetive score", neg_score_sum/len(sentences))
print("compound score", comp_score_sum/len(sentences))
