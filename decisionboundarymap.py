# using pillow we will visualise the decision boundary of the model and also
# will understand how was the dataset itself and if it was appropriate for 
# training the ML or not

"""
ofc this is extra but i just couldnt control myself from adding this to the final 
thing basically ill use pillow module instead of matplotlib to give each pixel a 
color to show if the person bought it or not 
each pixel will represent a person if its blue then he bought it 
if its red then he didnt buy it 
and y axis will represent salary
x axis will represent the ages from 1-100
ive been using pillow from years so i was familiar with it
"""

# i stored the trained model in trainedmodel.pkl using the finalcleanpredictor.py
import pickle
from PIL import Image

file = open("trainedmodel.pkl", "rb")
trainedmodel = pickle.load(file)
file.close()


# 4 lakh was approx the max so 400 pixel so 1000 per pixel approx gap
img = Image.new("RGB" , (100,400))
pixels = img.load()
for x in range(100):         # ages took as x axis
    for y in range(400):    # salary as y axis
        age = x + 1 
        salary = (y / 400) * 400000  
        pred = trainedmodel.predict([[age, salary]])[0]
        if pred == 1:
            pixels[x, 400 - y - 1] = (0, 0, 255)    # blue -- will buy
        else:
            pixels[x, 400 - y - 1] = (255, 0, 0)    # red - won't buy
img.save("decision_boundary2afterfilters.png")
img.show()
