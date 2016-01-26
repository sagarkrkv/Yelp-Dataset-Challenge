from nltk.classify import NaiveBayesClassifier
#from nltk.corpus import posectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
import os
from textblob import TextBlob
##
##neg_docs = []
##with open("C:/Users/ShravanJagadish/Desktop/Search/Final Project/Output/2011-2013/negative_Bakeries.txt",'r') as file:    
##    for lines in file:
##        blob = TextBlob(lines)
##        for sentences in blob.sentences:
##            inp = ''
##            #print sentences
##            content = sentences.split(" ")
##            for words in content:
##                if len(words) > 3 and words != 'null':
##                    inp = inp + words + ","
##            if len(inp) > 1:
##                neg_docs.append(("[" + inp +"],'neg'"))
##
##pos_docs = []
##with open("C:/Users/ShravanJagadish/Desktop/Search/Final Project/Output/2011-2013/positive_Bakeries.txt",'r') as file:    
##    for lines in file:
##        blob = TextBlob(lines)
##        for sentences in blob.sentences:
##            inp = ''
##            #print sentences
##            content = sentences.split(" ")
##            for words in content:
##                if len(words) > 3 and words != 'null':
##                    inp = inp + words + ","
##            if len(inp) > 1:
##                pos_docs.append(("[" + inp +"],'pos'"))
##
##




pos_docs = []
pos_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'pos'))
pos_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'pos'))
pos_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'pos'))
pos_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'pos'))
pos_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'pos'))
pos_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'pos'))
pos_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'pos'))
pos_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'pos'))
pos_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'pos'))
pos_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'pos'))

neg_docs = []
neg_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'neg'))
neg_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'neg'))
neg_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'neg'))
neg_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'neg'))
neg_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'neg'))
neg_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'neg'))
neg_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'neg'))
neg_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'neg'))
neg_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'neg'))
neg_docs.append((['smart', 'and', 'alert', ',', 'thirteen', 'conversations', 'about', 'one','thing', 'is', 'a', 'small', 'gem', '.'], 'neg'))


print len(pos_docs) 
print len(neg_docs)
print neg_docs[0]

train_pos_docs = pos_docs[:80]
test_pos_docs = pos_docs[80:100]
train_neg_docs = neg_docs[:80]
test_neg_docs = neg_docs[80:100]

training_docs = train_pos_docs+train_neg_docs
testing_docs = test_pos_docs+test_neg_docs

sentim_analyzer = SentimentAnalyzer()
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])
unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)

print len(unigram_feats)

sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
training_set = sentim_analyzer.apply_features(training_docs)
test_set = sentim_analyzer.apply_features(testing_docs)
trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)

for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
	print '{0}: {1}'.format(key, value)
