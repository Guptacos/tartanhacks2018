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

    for col in range(horiz):
        for row in range(vert):
            print("Row: %d Col: %d"%(row,col))
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
            









