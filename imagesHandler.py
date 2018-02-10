from PIL import Image
import numpy as np
from cv2 import *

def getCroppedPhotos(locations,img): 
    #only if we can get easy locations for gates
    src = Image.open(img)
    width = 50
    gateCount = 0

    for (x,y) in locations:
        temp = src.crop((x,y,width,width))
        temp.save("tempImages/gate%d"%gateCount)
        gateCount+=1


def getGridImages(img):
    #from a source image, img, this will generate
    #the 48 cropped images we want and put them in a folder
    #currently called 'testImg'
    src = Image.open(img)
    print(src.size[0])
    print(src.size[1])

    horiz = 8
    vert  = 6
    gridSize = horiz * vert

    gridWidth = src.size[0] // horiz
    gridHeight = src.size[1] // vert

    for col in range(horiz):
        for row in range(vert):
            left = col * gridWidth
            right = (col + 1) * gridWidth

            if (col%2 == 0):
                upper = row * gridHeight
                lower = (row + 1) * gridHeight
            else:
                upper = row * gridHeight + (gridHeight/2)
                lower = (row + 1) * gridHeight + (gridHeight/2)

            temp = src.crop((left,upper,right,lower))
            temp.save("testImg/%d-%d.jpg" %(row,col))


def filter_images():
    #returns a list of the filenames of the images
    #in testImg/ that it thinks have elements in them
    #works by checking if the cropped image has
    #any pixels that are strongly red
    threshold = 80
    has_elems = []
    horiz = 8
    vert  = 6
    for col in range(horiz):
        for row in range(vert):
            filename = "testImg/%d-%d.jpg" %(row,col)
            img = Image.open(filename)
            src = img.load()
            width,height = img.size
            for x in range(0,width,width//8):
                for y in range(0,height,height//8):
                    pixel = src[x,y]
                    newR = pixel[0]
                    newG = pixel[1]
                    newB = pixel[2]

                    if (newG<threshold and newB<threshold and 
                        newR > threshold):
                        #it has an element probably
                        if (filename not in has_elems):
                            has_elems.append(filename)
    #print(has_elems)
    return has_elems









    ####  OpenCV test functions  ####

def get_img():
    cam = VideoCapture(0)
    s, img = cam.read()
    if s:
        namedWindow("cam-test",WINDOW_NORMAL)
        imshow("cam-test",img)
        waitKey(0)
        #destroyWindow("cam-test")
        imwrite("CVTEST.jpg",img) #save image

def live_feed():
    cap = VideoCapture(0)
    while (True):
        ret,frame = cap.read()
        namedWindow('frame',WINDOW_NORMAL)
        imshow('frame',frame)
        if waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    destroyAllWindows()

 
            









