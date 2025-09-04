import sklearn , csv
from sklearn.linear_model import LogisticRegression

def returndataset():
   file = open("dataset.csv" , "r")
   database = list(csv.reader(file))[2:]
   #print(database)
   file.close()
   return database

# no need of sigmoid

mlmodel = LogisticRegression()
datasethold = returndataset() # stored the data in a var
x = [] # input params 
y = [] # output params

for i in datasethold:
   age , salary , output = i[2], i[3] , i[4]
   # 4 types of things exists in dataset that makes dataset
   # bad or inappropriate : "NaN", "Null", "", "?" 
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


# to make it like a program
while True:
   param = input("\nPlease enter the 'age salary' of the customer : ")
   age , salary = float(param.split(" ")[0]), float(param.split(" ")[1])
   prediction = bool(trainedmodel.predict([[age,salary]]))
   if prediction:
      print("Yes the probability of this customer purchasing the TV is HIGH")
   else:
      print("The probability of this customer purchasing the TV is LOW")

# more test cases :
# after analysing the dataset manually myself 
# about how it has decided to the give 0 to some and 1 to another
# print(trainedmodel.predict([[,]]))

# im pasting below the test cases that i tested with its output given by the model 

"""
Please enter the 'age salary' of the customer : 18 10
The probability of this customer purchasing the TV is LOW
Please enter the 'age salary' of the customer : 18 1000
The probability of this customer purchasing the TV is LOW
Please enter the 'age salary' of the customer : 18 1000000
Yes the probability of this customer purchasing the TV is HIGH

Please enter the 'age salary' of the customer : 12 100
The probability of this customer purchasing the TV is LOW

Please enter the 'age salary' of the customer : 12 10000
The probability of this customer purchasing the TV is LOW
this feels very realistic in my opinion

Please enter the 'age salary' of the customer : 12 1000000
Yes the probability of this customer purchasing the TV is HIGH
a rich kid even if hes 12 will def buy a TV

Please enter the 'age salary' of the customer : 100 70000
Yes the probability of this customer purchasing the TV is HIGH
if a 100 year old has 70k then he will buy it


Please enter the 'age salary' of the customer : 1 70000
The probability of this customer purchasing the TV is LOW
but in this if a newborn of 1 age has 70k he wont buy it
so by this we know model isnt biased towards the money only 
but also considers age 
i think this much test cases are satisfactory !!!!


"""