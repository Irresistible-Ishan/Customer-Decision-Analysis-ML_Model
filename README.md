# Customer Decision Analysis model trained using logistics regression 

## Modules used : scikit-learn , csv 
## Model used : Logistic regression 
## dataset used : given by the event host -> dataset.csv
## final code filename : finalcleanpredictor.py
## language used : python

## modules to be installed using : `pip install scikit-learn`

### I have included 2 extra codes where in one i've just experimentally revised the data handling using csv and the another is where ive shows my actual thought process using excessive live comments in the code itself
### I have also included 3 pictures of very initial thought process of how i came upon the decision of using this particular model and not any other regression or ml model.

after completely training the model i couldnt resist the urge to make a mapping to visualise the model decision upon which it was trained the dataset
later i learned that it was called decision boundary where the decision changes 
as X axis i have taken the age from 1 to 100 and y axis is the salary of 4 lakh max approx to only consider under 50 LPA customers to reduce errors in the dataset
later i also implemeted more filters using if statements and more methods to clean the dataset to make the decision better and better 
### RED : did not buy the TV , BLUE : bought the TV
![DECISIONBOUNDARYMAP](decision_boundary.png)
### module used to make this heatmap or decision boundary : pillow ( did not choose to use matplotlib due to personal preference)


### I would suggest to not rely on the given handwritten thought process because it was very inital and the more indepth ones are written in the code file itself
# thought process images:

![1](thoughtprocess1.jpg)
![2](thoughtprocess2.jpg)
![3](thoughtprocess3.jpg)

### Sorry for inconveniences cause by handwriting as this is a very rough blueprint for my own use during the making of this, but stil uploaded it as its very important to show the decision tree of how someone would come to choose the right model , in AIML , its all about choosing the right tools and right approach mostly
