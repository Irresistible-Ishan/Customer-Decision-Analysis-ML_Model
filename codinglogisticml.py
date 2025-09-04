# In this project im writing comments more than usual 
# because in instructions it was said that
# we should be able to show our thought process while making 

# apart from comments actually
# i was noting down my step by step thought process
# while making this 
# so its handwritten 
# ill be uploading a pdf or image files along side this in a
# different file

#here is the code below hope you enjoy :)
# sorry about inconvinence cause by flooding of code with comments
# i think ill also provide a clean version of this code in

"""finalcleancode.py"""


# reusing the csv logic from previous file
import csv , math , random , time

def returndataset():
   file = open("dataset.csv" , "r")
   database = list(csv.reader(file))[2:]
   #print(database)
   file.close()
   return database

#print(returndataset()[0])
# sigmoid function 
"""
sigmoid(z) = 1 / 1 + e^(-z)
can use math.e here 
"""
def sigmoid(z:float):
   return int(1/(1 + (math.e)**(-z)))

#print(sigmoid(0.7) , sigmoid(0.3)) 
# 0 ,0 
# came to realise sigmoid is not necessary
# but can be necessarly needed if
# model throws something above 100 or something
#print(sigmoid(1002))
# 1

 # uhhhh i guess first i gotta write the model
 # im unable to understand what output are 
 # we converting using sigmoid to 0-1 probability

# ah i cant apply multi regression + sigmoid 
# since dataset itself dosent have a var output to train on
# so ill have to directly use logistic model in sklearn

# my thinking was wrong so now ill have to directly 
# apply a logistics regression model

import sklearn 
from sklearn.linear_model import LogisticRegression

mlmodel = LogisticRegression()

# after looking at docs and few sources i came to know we have to put
# input parameters as a list such as [param 1 , param2 , and so on ] and output param as y
# all the possible values of each iteration or each row will be each elemnt in the list which goes into
# x and y of model.fit(x,y) 
# so ill apply that below here 
# print(returndataset())so last element of each goes as y 
# and before that one goes in x

datasethold = returndataset() # stored the data in a var
x = [] # input params 
y = [] # output params

"""
for i in datasethold:
   if not "NaN" in i or not "Null" in i: 
      x.append(i[2:4])
      y.append(i[-1]) 
# ok this is not working i noticed alot of problems in the
# dataset so ill black this code out and rewrite it differently
"""

for i in datasethold:
   age , salary , output = i[2], i[3] , i[4]
   # 4 types of things exists in data set that makes dataset
   # bad "NaN", "Null", "", "?" 
   if not any(seq in [age , salary , output] for seq in ["NaN", "Null", "", "?"]):
      try:
        age = float(age)
        salary = float(salary)
        output = int(output)
      except ValueError:
        continue
      x.append([age , salary])
      y.append(output)




trainedmodel = mlmodel.fit(x,y)
# now to use it we will use .predict() method
#print(trainedmodel.predict([[age , salary]])) - should give 1 or 0
#lets see if it works or not

print(trainedmodel.predict([[40 , 7000]]))
# YES NOW IT WORKS it came as 0 
print(trainedmodel.predict([[40 , 90000000]]))
# yess it should come as 1 as expected 
# actually this is so good since this salary is an unseen data
# and it still gave a logically correct ans 
# i think this is perfect!!

# ok got my first error after running the above and i think its 
# because of like in dataset hmm
# like NaN like none values are there so we need to clean the dataset
# a good and clean dataset can only work the best so we 
# need to ignore the ones with NaN in the values



# i think this works so well 
print(trainedmodel.predict([[]]))