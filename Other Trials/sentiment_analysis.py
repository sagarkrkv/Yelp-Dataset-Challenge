from nltk.classify import NaiveBayesClassifier
#from nltk.corpus import posectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
import os
from textblob import TextBlob

neg_docs = []
with open("C:/Users/ShravanJagadish/Desktop/Search/Final Project/Output/2011-2013/negative_Bakeries.txt",'r') as file:    
    for lines in file:
        blob = TextBlob(lines)
        for sentences in blob.sentences:
            inp = []
            #print sentences
            content = sentences.split(" ")
            for words in content:
                if len(words) > 2 and words != 'null':
                    inp.append(words)
            if len(inp) > 1:
				#lister = [inp,'neg']
                #neg_docs.append(("[" + inp +"],'neg'"))
				neg_docs.append((inp,'neg'))

pos_docs = []
with open("C:/Users/ShravanJagadish/Desktop/Search/Final Project/Output/2011-2013/positive_Bakeries.txt",'r') as file:    
    for lines in file:
        blob = TextBlob(lines)
        for sentences in blob.sentences:
            inp = []
            #print sentences
            content = sentences.split(" ")
            for words in content:
                if len(words) > 2 and words != 'null':
                    inp.append(words)
					#inp = inp + words + ","
            if len(inp) > 1:
				#lister = [inp,'pos']
                #pos_docs.append(("[" + inp +"],'pos'"))
				pos_docs.append((inp,'pos'))

test_neg_docs = []
with open("C:/Users/ShravanJagadish/Desktop/Search/Final Project/Output/2014/negative_Bakeries.txt",'r') as file:    
    for lines in file:
        blob = TextBlob(lines)
        for sentences in blob.sentences:
            inp = []
            #print sentences
            content = sentences.split(" ")
            for words in content:
                if len(words) > 2 and words != 'null':
                    inp.append(words)
            if len(inp) > 1:
				#lister = [inp,'neg']
                #neg_docs.append(("[" + inp +"],'neg'"))
				neg_docs.append((inp,'neg'))

test_pos_docs = []
with open("C:/Users/ShravanJagadish/Desktop/Search/Final Project/Output/2014/positive_Bakeries.txt",'r') as file:    
    for lines in file:
        blob = TextBlob(lines)
        for sentences in blob.sentences:
            inp = []
            #print sentences
            content = sentences.split(" ")
            for words in content:
                if len(words) > 2 and words != 'null':
                    inp.append(words)
					#inp = inp + words + ","
            if len(inp) > 1:
				#lister = [inp,'pos']
                #pos_docs.append(("[" + inp +"],'pos'"))
				pos_docs.append((inp,'pos'))

print len(pos_docs) 
print len(neg_docs)
print neg_docs[0]

train_pos_docs = pos_docs[:800]
test_pos_docs = pos_docs[:800]
train_neg_docs = neg_docs[:800]
test_neg_docs = neg_docs[:800]

training_docs = train_pos_docs + train_neg_docs
testing_docs = test_pos_docs + test_neg_docs

#training_docs = pos_docs+neg_docs
#testing_docs = test_pos_docs+test_neg_docs

sentim_analyzer = SentimentAnalyzer()
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])
unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)

print len(unigram_feats)

sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
training_set = sentim_analyzer.apply_features(training_docs)
test_set = sentim_analyzer.apply_features(testing_docs)
trainer = NaiveBayesClassifier.train
#nbcl = NaiveBayesClassifier
classifier = sentim_analyzer.train(trainer, training_set)
#type(trainer.classify(test_set))
#prediction = NaiveBayesClassifier.classify(trainer)
#predict = prediction.classify(test_set)
#print predict
print classifier.show_most_informative_features(5)
for items in testing_docs:
	dict = {}
	dict.update({'word' : items[0]})
	print dict
	print classifier.classify(dict)

for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
	print '{0}: {1}'.format(key, value)
