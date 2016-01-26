# YelpDatasetChallenge
This program is designed to predict numerical rating values,based on the textual review data for businesses in the yelpdataset.


Predict Rating can be executed by running the python file task2b.py

Requirements:
	Python 2.7
	Textblob api and its corpora.(http://textblob.readthedocs.org/en/dev/install.html)


Give arguments in this format
				
				python task2b.py predict 
				python task2b.py evaluate 
		
		If you need to generate training and test data files run
				python task2b.py parse 


		
		You can even run all the tasks at once
 				python task2b.py parse predict evaluate

This file takes commandline arguments and does 3 main functions:
1.) parse
2.) predict
3.) evaluate

Parse:
	Parse function parses the yelp_academic_dataset_business and yelp_academic_dataset_review files to create the base files required for prediction and also creates the ground truth file.
	
	The Train directory has all the reviews for businesses during the years 2011-2013 
		sorted by ratings and business_id.
	The Test directory has all the reviews for businesses during the year 2014 sorted by 
	month and business_id.

Predict:

	This function reads the reviews from the train directory created by the parse function and 
	creates a base sentence polarity for each rating and business during the years 2011-2013.

	It reads the reviews for each business for each month during 2014 from the test directory.
	Based on the base polarities for each business it predicts rating.

	It saves its output in the predicted_2014.csv file in the Task2B folder

Evaluate:
	This function compares the predicted rating for each business for each month in 2014 with the corresponding ground truth.
	Based on that it generates a report with the average accuracy.

	The report is saved as Evaluation_Results.txt in the Task2B folder.

	Error Percentage is calculated by  (actual-predicted)/actual

	Avg Accuracy is calculated by (1-Avg(Error Percentage))
