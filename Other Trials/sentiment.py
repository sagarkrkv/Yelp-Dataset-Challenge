from nltk.classify import NaiveBayesClassifier
#from nltk.corpus import posectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
import os
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import EnglishStemmer

stemmer = EnglishStemmer()


def get_feature(sentence):
	sentence = sentence.lower()
	sentence = sentence.replace("null","")
	sentence = sentence.strip()
	return {'sentence' : sentence}

neg_docs = []
with open("C:/Users/ShravanJagadish/Desktop/Search/Final Project/Output/2011-2013/negative_Bakeries.txt",'r') as file:    
    for lines in file:
        blob = TextBlob(lines)
        for sentences in blob.sentences:
			for nword in sentences.noun_phrases:
				nlist = word_tokenize(nword)
				sent = ''
				for words in nlist:					
					sent = sent+stemmer.stem(words.lower()) + "_"
				sent = sent[:-1]
				neg_docs.append((get_feature(sent),'neg'))
            

pos_docs = []
with open("C:/Users/ShravanJagadish/Desktop/Search/Final Project/Output/2011-2013/positive_Bakeries.txt",'r') as file:    
    for lines in file:
        blob = TextBlob(lines)
        for sentences in blob.sentences:
            for nword in sentences.noun_phrases:
				nlist = word_tokenize(nword)
				sent = ''
				for words in nlist:
					sent = sent+stemmer.stem(words.lower()) + "_"
				sent = sent[:-1]
				pos_docs.append((get_feature(sent),'pos'))

test_neg_docs = []
with open("C:/Users/ShravanJagadish/Desktop/Search/Final Project/Output/2014/negative_Bakeries.txt",'r') as file:    
    for lines in file:
        blob = TextBlob(lines)
        for sentences in blob.sentences:
            for nword in sentences.noun_phrases:
				nlist = word_tokenize(nword)
				sent = ''
				for words in nlist:					
					sent = sent+stemmer.stem(words.lower()) + "_"
				sent = sent[:-1]
				test_neg_docs.append((get_feature(sent),'neg'))

test_pos_docs = []
with open("C:/Users/ShravanJagadish/Desktop/Search/Final Project/Output/2014/positive_Bakeries.txt",'r') as file:    
    for lines in file:
        blob = TextBlob(lines)
        for sentences in blob.sentences:
            for nword in sentences.noun_phrases:
				nlist = word_tokenize(nword)
				sent = ''
				for words in nlist:
					sent = sent+stemmer.stem(words.lower()) + "_"
				sent = sent[:-1]
				test_pos_docs.append((get_feature(sent),'pos'))


print len(pos_docs) 
print len(neg_docs)
print len(test_pos_docs) 
print len(test_neg_docs)
#print neg_docs[0]

#train_pos_docs = pos_docs[:800]
#test_pos_docs = pos_docs[:800]
#train_neg_docs = neg_docs[:800]
#test_neg_docs = neg_docs[:800]
#training_docs = train_pos_docs + train_neg_docs
#testing_docs = test_pos_docs + test_neg_docs

training_docs = pos_docs+neg_docs
testing_docs = test_pos_docs+test_neg_docs

#sentim_analyzer = SentimentAnalyzer()
#all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])
#unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)

#print len(unigram_feats)

#sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
#training_set = sentim_analyzer.apply_features(training_docs)
#test_set = sentim_analyzer.apply_features(testing_docs)
classifier = nltk.NaiveBayesClassifier.train(training_docs)
#type(trainer.classify(test_set))
#prediction = NaiveBayesClassifier.classify(trainer)
#predict = prediction.classify(test_set)
#print predict
print classifier.show_most_informative_features(5)
print nltk.classify.accuracy(classifier, testing_docs)

#for items in testing_docs:
#	print items[0]
#	print classifier.classify(items[0])

