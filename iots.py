from cv2 import cv2 
import time
from PIL import Image
import pytesseract
import os
import pyttsx3
import sys


class init_voice() :
    engine = pyttsx3.init()  
    voices = engine.getProperty('voices')  
    engine.setProperty('voice', voices[0].id)  
    engine.setProperty('rate', 140)
  
reply = init_voice()

capture_duration = 100000

camera = cv2.VideoCapture(1)

start_time = time.time()
while True:
    return_value,image = camera.read()

 #   cv2.imshow('image',image)
   # cv2.waitKey(0)
    if (int(time.time()-start_time) < capture_duration):
        cv2.imwrite('test.jpg',image)
        break
camera.release()

textimage=Image.open("test.jpg")
#textimage = cv2.imread("test.jpg")
#textimage =textimage.convert('1')
textimage.save("result.jpg")
print("The scan")
print(pytesseract.image_to_string(textimage))
word = pytesseract.image_to_string(textimage)
f = open("demo.txt", "a")
f.write(word)
f.close()
reply.engine.say(word)
reply.engine.runAndWait()

cv2.destroyAllWindows()