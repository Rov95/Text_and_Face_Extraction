import cv2 as cv
import PIL
import pytesseract
from  PIL import ImageEnhance, ImageDraw, Image
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

face_cascade = cv.CascadeClassifier("OneDrive\Escritorio\scripts\haarcascade_frontalface_default.xml")

def extract_text(image):
    grey = image.convert("L")
    txt = pytesseract.image_to_string(grey)
    return txt

def create_file(text, name):
    file_name = "page_" + str(name) +  ".txt"
    with open(file_name, "w") as file:
        file.write(text)
        
def crop_face(PIL_image, cv_image):
    lst = []
    faces = face_cascade.detectMultiScale(cv_image, 1.40)
    if  len(faces) == 0:
        print("No faces detected")
        return lst
    else:
        rec = faces.tolist()
        for l in rec:
            crop = PIL_image.crop((l[0], l[1], l[0]+l[2], l[1]+l[3]))
            lst.append(crop)
        return lst



def show_faces(img_lst):
    if len(img_lst) > 0:
        first_image = img_lst[0]
        if len(img_lst) > 5:
            contact_sheet = PIL.Image.new(first_image.mode, (first_image.width*5, first_image.height*2))
        else:
            contact_sheet = PIL.Image.new(first_image.mode, (first_image.width*5, first_image.height))
        x=0
        y=0
        for im in img_lst[:]:
            im = im.resize((int(first_image.width), int(first_image.height)))
            contact_sheet.paste(im, (x, y))
            if x+first_image.width == contact_sheet.width:
                x=0
                y=y+first_image.height
            else:
                x=x+first_image.width
        return contact_sheet
    
    else:
        contact_sheet = PIL.Image.new("RGB", (50, 50))
        return contact_sheet
  
        

def look_for_a_word(word, lst_of_tuples):
    n = 0
    for pil, cvi, txt in lst_of_tuples:
        if word in txt:
            result = show_faces(crop_face(pil, cvi))
            print("The result for a-{}".format(n))
            result.show()
            n += 1
        else:
            print("This word is not on image a-{}".format(n))
            n += 1


#files = zip_file.infolist()
img0 = Image.open("images\pic_0.png")
img1 = Image.open("images\pic_1.png")
img2 = Image.open("images\pic_2.png")
img3 = Image.open("images\pic_3.png")
img4 = Image.open("images\pic_4.png")
img5 = Image.open("images\pic_5.png")
img6 = Image.open("images\pic_6.png")
img7 = Image.open("images\pic_7.png")
img8 = Image.open("images\pic_8.png")
img9 = Image.open("images\pic_9.png")
img10 = Image.open("images\pic_10.png")
img11 = Image.open("images\pic_11.png")
img12 = Image.open("images\pic_12.png")
img13 = Image.open("images\pic_13.png")
images = [img0, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13]
#----------------------------------------------------------------------------
cv_img0 = cv.imread("images\pic_0.png")
cv_img1 = cv.imread("images\pic_1.png")
cv_img2 = cv.imread("images\pic_2.png")
cv_img3 = cv.imread("images\pic_3.png")
cv_img4 = cv.imread("images\pic_4.png")
cv_img5 = cv.imread("images\pic_5.png")
cv_img6 = cv.imread("images\pic_6.png")
cv_img7 = cv.imread("images\pic_7.png")
cv_img8 = cv.imread("images\pic_8.png")
cv_img9 = cv.imread("images\pic_9.png")
cv_img10 = cv.imread("images\pic_10.png")
cv_img11 = cv.imread("images\pic_11.png")
cv_img12 = cv.imread("images\pic_12.png")
cv_img13 = cv.imread("images\pic_13.png")
cvs = [cv_img0, cv_img1, cv_img2, cv_img3, cv_img4, cv_img5, cv_img6, cv_img7, cv_img8, cv_img9, cv_img10, cv_img11, cv_img12, cv_img13]

texts = []

 for image in images:
        texts.append(extract_text(image))
        
for t in range(len(texts)):
        create_file(texts[t], t)

t0 = open("page_0.txt", "r")
t1 = open("page_1.txt", "r")
t2 = open("page_2.txt", "r")
t3 = open("page_3.txt", "r")
t4 = open("page_4.txt", "r")
t5 = open("page_5.txt", "r")
t6 = open("page_6.txt", "r")
t7 = open("page_7.txt", "r")
t8 = open("page_8.txt", "r")
t9 = open("page_9.txt", "r")
t10 = open("page_10.txt", "r")
t11 = open("page_11.txt", "r")
t12 = open("page_12.txt", "r")
t13 = open("page_13.txt", "r")
tx = [t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13]

info = []
for t in tx:
    info.append(t.read())

work = list(zip(images, cvs, info))
word = "Mark"


look_for_a_word(word, work)


