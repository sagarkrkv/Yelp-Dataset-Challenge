negative_list = []
positive_list = []

path = "C:/Users/ShravanJagadish/Desktop/Search/Final Project/Output/2011-2013_Noun Extraction/"

with open(path + "negative_Bakeries.txt") as file:
    contents = file.readlines()
    for content in contents:
        inter = content.split()
        for words in inter:
        #print(content)
            negative_list.append(words)
            #print(words)

with open(path + "positive_Bakeries.txt") as file:
    contents = file.readlines()
    for content in contents:
        inter = content.split()
        for words in inter:
        #print(content)
            positive_list.append(words)
            #print(words)

new_negative_list = ""
new_positive_list = ""


for words in negative_list:
    if words not in positive_list:
        new_negative_list = new_negative_list +  " " + words


for words in positive_list:
    if words not in negative_list:
        new_positive_list = new_positive_list + " " + words

print("size of old negative file" , len(negative_list))
print("size of new negative file" , len(new_negative_list))

print("size of old positive file" , len(positive_list))
print("size of new positive file" , len(new_positive_list))


with open(path + "newNegative_Bakeries.txt",'w') as file:
    file.write(new_negative_list)

with open(path + "newPositive_Bakeries.txt",'w') as file:
    file.write(new_positive_list)

#print(new_negative_list)
#print(new_positive_list)
            
