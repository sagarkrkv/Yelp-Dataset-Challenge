import os

negative_list = []
positive_list = []

main_positive_count=0;
main_negative_count=0;
main_total_count=0;

path = "C:/Users/ShravanJagadish/Desktop/Search/Final Project/Output/2011-2013_Noun Extraction/"
path_2014 = "C:/Users/ShravanJagadish/Desktop/Search/Final Project/Output/14_Noun Extraction/"

with open(path+"newNegative_Bakeries.txt") as file:
        contents = file.read()
        inter = contents.split()
        main_negative_count=len(inter)
        for words in inter:
                negative_list.append(words)

with open(path+"newPositive_Bakeries.txt") as file:
        contents = file.read()
        inter = contents.split()
        main_positive_count=len(inter)
        for words in inter:
                positive_list.append(words)		
		
main_total_count=main_positive_count+main_negative_count
main_positive_percent=(main_positive_count/main_total_count)*100

#print("main positive count ",main_positive_count, " main_negative_count " , main_negative_count, " main_total_count " , main_total_count)
#print("main_positive_percent ", main_positive_percent)

new_negative_list = ""
new_positive_list = ""
positive_count=0
negative_count=0
total_count=0
calculated_rating=0
counter = 0
for filenames in os.listdir(path_2014):
        with open(path_2014 + filenames, 'r') as file:
                content = file.read()
                inter = content.split()
                #ind_file_size = len(inter)
                for words in inter:
                        if words in positive_list:
                                positive_count+=1
                        elif words in negative_list:
                                negative_count+=1

        pos = (positive_count/main_positive_count)
        neg = (negative_count/main_negative_count)

        total_count=(positive_count)+(negative_count)
        positive_percent=(positive_count/total_count)*100
        truth = 0
        bid = filenames.rsplit('_Bakeries.txt')
        #print(bid[0])
        with open("C:/Users/ShravanJagadish/Desktop/Search/Final Project/Output/Ground Truth/14/GroundTruth_Bakeries.txt",'r') as filer:
                while(True):
                        line = filer.readline()
                        if(line == ""):
                                break
                        line_list = line.split('::')
                        #print(line_list[0] + " " + line_list[1])
                        if(line_list[0] == bid[0]):
                                truth = line_list[1]
                                break
##        new_rating = ((pos/(pos+neg))*100/20)
##        if(truth != 0):
##                counter = counter + 1
##                print(counter, " ", bid[0], " Pred- " , "{0:.2f}".format(new_rating) , " GT- " , "{0:.2f}".format(float(truth)), " Diff " , "{0:.2f}".format(abs(new_rating - float(truth))), \
##                      " EP- ", "{0:.2f}".format(100 * abs(new_rating - float(truth))/5))



##        new_rating = ((positive_count/(positive_count+negative_count))*100)/20
##        if(truth != 0):
##                counter = counter + 1
##                print(counter, " ", bid[0], " Pred- " , "{0:.2f}".format(new_rating) , " GT- " , "{0:.2f}".format(float(truth)), " Diff " , "{0:.2f}".format(abs(new_rating - float(truth))), \
##                      " EP- ", "{0:.2f}".format(100 * abs(new_rating - float(truth))/5))
        
        shravan = ((pos/(pos+neg))*100/20)
        pramod = ((positive_count/(positive_count+negative_count))*100)/20
        if(truth != 0):
                counter = counter + 1
                print(counter, " ", bid[0], " ", "{0:.2f}".format(100 * abs(shravan - float(truth))/5), " ", "{0:.2f}".format(100 * abs(pramod - float(truth))/5))
