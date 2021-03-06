

import numpy as np
import cv2
import pickle
import os



def getCalssName(classNo):
    if   classNo == 0: return 'Burgers - 360 cal'
    elif classNo == 1: return 'Cookies (30g) _ 148 cal'
    elif classNo == 2: return 'Donuts (100g) _ 452 cal'
    elif classNo == 3: return 'French_fries (100g)- 312 cal'
    elif classNo == 4: return 'Fried_chicken (100g) -246 cal'
    elif classNo == 5: return 'Fried_egg- 180 cal'
    elif classNo == 6: return 'Hotdogs - 290 cal'
    elif classNo == 7: return 'Pizza (100g) _ 266 cal'
    elif classNo == 8: return 'Apple (100g) _ 52 cal'
    elif classNo == 9: return 'Banana (100g) _ 89 cal'
    elif classNo == 10: return 'Orange (100g) _ 47 cal'

frameWidth= 640        
frameHeight = 480
brightness = 180
threshold = 0.95        
font = cv2.FONT_HERSHEY_SIMPLEX

 
# SETUP THE VIDEO CAMERA
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, brightness)
# IMPORT THE TRANNIED MODEL
pickle_in=open("model.p","rb") 
model=pickle.load(pickle_in)
 
def grayscale(img):
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return img
def equalize(img):
    img =cv2.equalizeHist(img)
    return img
def preprocessing(img):
    img = grayscale(img)
    img = equalize(img)
    img = img/255
    return img

    
 
while True:
 
    # READ IMAGE
    success, imgOrignal = cap.read()
     
    # PROCESS IMAGE
    img = np.asarray(imgOrignal)
    img = cv2.resize(img, (32, 32))
    img = preprocessing(img)
    cv2.imshow("Processed Image", img)
    img = img.reshape(1, 32, 32, 1)
    cv2.putText(imgOrignal, "CLASS: " , (20, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(imgOrignal, "PROBABILITY: ", (20, 75), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
    # PREDICT IMAGE
    predictions = model.predict(img)
    classIndex = model.predict_classes(img)
    probabilityValue =np.amax(predictions)
    if probabilityValue > threshold:
       
    #print(getCalssName(classIndex))

        cv2.putText(imgOrignal,str(classIndex)+" "+str(getCalssName(classIndex)), (120, 35), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.putText(imgOrignal, str(round(probabilityValue*100,2) )+"%", (180, 75), font, 0.75, (0, 0, 255), 2, cv2.LINE_AA)
        cv2.imshow("Result", imgOrignal)
        #print(getCalssName(classIndex))
        x=getCalssName(classIndex)
        
        
        
       
       
            
            
            
         
    if cv2.waitKey(1) and 0xFF == ord('q'):
    
        break
