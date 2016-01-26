import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
import os
from textblob import TextBlob
from nltk.stem.snowball import EnglishStemmer

stemmer = EnglishStemmer()

output_path = "C:/Users/ShravanJagadish/Desktop/Search/Final Project/Output/14_Noun Extraction/"
path = "C:/Users/ShravanJagadish/Desktop/Search/Final Project/Output/14/"


if not os.path.exists(output_path):
   		os.makedirs(output_path)

noun_list_positive = ""

for file_name in os.listdir(path):
	noun_list_negative = ""	
	with open(path+file_name, 'r') as file:
		#month = file_name.rsplit("_")
		my_file = file_name.rsplit(".txt")
		for line in file:
			blob = TextBlob(line)
			for sentence in blob.sentences:
				# if sentence.sentiment.polarity < 0:
					for nword in sentence.noun_phrases:
						nlist = word_tokenize(nword)
						#print nlist
						# if month[1] == 'positive':
						# 		noun_list_positive+="\""
						# else:
						# 		noun_list_negative+="\""
						for word in nlist:
							# if word not in ["amelie","airport","charlotte"]:
							# if month[1] == 'positive':
							# 	noun_list_positive+=stemmer.stem(word) + "_"
							# else:
								noun_list_negative+=stemmer.stem(word.lower()) + "_"
						# if month[1] == 'positive':
						# 		noun_list_positive=noun_list_positive[:-1]
						# 		noun_list_positive+="|"
						# else:
						noun_list_negative=noun_list_negative[:-1]
						noun_list_negative+=" "

	with open(output_path+file_name,'w') as writefile:
		writefile.write(noun_list_negative)
# with open(output_path+"sh-2012.txt",'w') as writefile:
# 	writefile.write(noun_list_negative)
