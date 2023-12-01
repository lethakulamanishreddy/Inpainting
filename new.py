import cv2
from PIL import ImageTk, Image, ImageDraw
import PIL
from tkinter import *
import numpy as np
im=cv2.imread('P_20201129_165042-01.jpeg')
im=cv2.resize(im,(600,600))
cv2.imwrite('back.jpg',im)

width = 600
height = 600
center = height//2
white = (255, 255, 255)
green = (0,128,0)
black=(0,0,0)

def save():
    filename = "image.jpg"
    image1.save(filename)
    img=cv2.imread('back.jpg')
    img=cv2.resize(img,(600,600))
    mask=cv2.imread('image.jpg',0)
    mask=cv2.resize(mask,(600,600))
    dst=cv2.inpaint(img,mask,3,cv2.INPAINT_NS)
    cv2.imshow('original',img)
    cv2.imshow('Edited',dst)

    

def paint(event):
    # python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval(x1, y1, x2, y2, fill="white",width=10)
    draw.line([x1, y1, x2, y2],fill="white",width=10)

root = Tk()

# Tkinter create a canvas to draw on
cv = Canvas(root, width=width, height=height)
##cv.pack()

image = ImageTk.PhotoImage(file = 'back.jpg')
img=cv.create_image(10, 10, image = image, anchor = NW)

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = PIL.Image.new("RGB", (width, height), black)
draw = ImageDraw.Draw(image1)

# do the Tkinter canvas drawings (visible)
# cv.create_line([0, center, width, center], fill='green')

cv.pack(expand=YES, fill=BOTH)
cv.bind("<B1-Motion>", paint)

# do the PIL image/draw (in memory) drawings
# draw.line([0, center, width, center], green)

# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
# filename = "my_drawing.png"
# image1.save(filename)
button=Button(text="save",command=save)
button.pack()
root.mainloop()
