import pytesseract
import cv2
from pytesseract import Output
from function import *

img = cv2.imread("plate4.jpg")
cv2.imshow('img', img)

carplate_img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
detected_carplate_img = plate.detect(carplate_img_rgb)
cv2.imshow('detected_carplate_img', detected_carplate_img)
carplate_extract_img = plate.extract(carplate_img_rgb)
carplate_extract_img = plate.enlarge_img(carplate_extract_img, 120)

carplate_extract_img_gray = cv2.cvtColor(carplate_extract_img, cv2.COLOR_RGB2GRAY)

thresh = cv2.threshold(carplate_extract_img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


d = pytesseract.image_to_data(thresh, config=f'--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789', output_type=Output.DICT)

n_boxes = len(d['level'])
for i in range(n_boxes):
    (text,x,y,w,h) = (d['text'][i],d['left'][i],d['top'][i],d['width'][i],d['height'][i])
    cv2.rectangle(carplate_extract_img, (x,y), (x+w,y+h) , (0,255,0), 2)
text=d['text'][-1]
info=[f"numero de plaque {text}", f"wilaya de {plate.region(text[-2:])}", f"annee 20{text[6:8]}", f"type de vehicule: {plate.type_vehicule(text[5:6])}"]


cv2.rectangle(img, (20, 20), (650, 150), (59, 57, 56), -1)
cv2.putText(img, info[0], (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,51,255), 2, cv2.LINE_AA)
cv2.putText(img, info[1], (50,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,51,255), 2, cv2.LINE_AA) 
cv2.putText(img, info[2], (50,110), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,51,255), 2, cv2.LINE_AA) 
cv2.putText(img, info[3], (50,140), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,51,255), 2, cv2.LINE_AA)  
cv2.imshow('img', img)
cv2.imshow("detected_carplate_img", detected_carplate_img)
cv2.imshow("carplate_extract_img", carplate_extract_img)
cv2.imshow('threshold', thresh)
cv2.waitKey(0)
