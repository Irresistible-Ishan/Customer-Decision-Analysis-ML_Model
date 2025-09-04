import csv 

# i was just revising csv data handling 

file = open("dataset.csv" , "r")
database = csv.reader(file)
print(database) # it printed <_csv.reader object at 0x000002CAA0A33F40> an object
# iterting the object using loop
x = list(database)
#print(x)
print(x[2:])
#for i in list(database)[2:]:  # so i used database[2:] instad of database
#   print(i)
file.close()
# this is working 
# got output like thsi 
"""
['ï»¿set1data', '', '', '', '']
['', 'id', 'age', 'salary', 'bought TV']
['0', '1', '51', '8241', '1']
['1', '2', '33', '68076', '0']
['2', '3', '41', '7876', '0']
['3', '4', '60', '94066', '1']

i need to remove first 2 rows and then put it in the var
and use it in the ml code
"""