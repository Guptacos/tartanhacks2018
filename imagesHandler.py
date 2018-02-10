from PIL import Image

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
    src = Image.open(img)
    print(src.size[0])
    print(src.size[1])

    horiz = 8
    vert  = 6
    gridSize = horiz * vert

    gridWidth = src.size[0] // horiz
    gridHeight = src.size[1] // vert

    for row in range(vert):
        for col in range(horiz):
            print("Row: %d Col: %d"%(row,col))
            left = col * gridWidth
            upper = row * gridHeight
            right = (col + 1) * gridWidth
            lower = (row + 1) * gridHeight
            temp = src.crop((left,upper,right,lower))
            temp.save("testImg/%d-%d.jpg" %(row,col))
            print("left: %d right: %d upper: %d Lower: %d"
                     %(left,right,upper,lower))









