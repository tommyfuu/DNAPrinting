
import PIL.ImageStat
import PIL.Image
import math
import os

##test images
image1 = 'Screen Shot 2019-07-18 at 2.30.23 PM.png'
image2 = '/Users/fcl/desktop/DNAPrinting/CROPPED-zhe/帅 Tom 聪明'


#find perceived brightnes as a standard
##later could be compared to and decide whether the designated block would be inked or not
def standardBrightness(im):
    imgwidth, imgheight = im.size
    sumBrightness = 0 #initiate sum
    numberofpixels = 0 #initiate number of pixels
    for x in range(0, imgwidth):
        for y in range(0, imgheight):
            numberofpixels += 1
            rgb_im = im.convert('RGB')
            r,g,b = rgb_im.getpixel((x, y))
            sumBrightness+=math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
    standardBrightness = sumBrightness/numberofpixels
    return standardBrightness




#find the designated block, check whether its brightness is higher than the standard
## if yes return a true; otherwise false
def processBlock(img, x0, y0, standard):
    #box = (x0, y0, x0+boxWidth, y0+boxHeight)
    sumBrightness = 0 #initiate sum
    numberofpixels = 0 #initiate number of pixels
    for x in range(x0, x0+boxWidth):
        for y in range(y0, y0+boxHeight):
            numberofpixels += 1
            rgb_im = im.convert('RGB')
            r,g,b = rgb_im.getpixel((x, y))
            sumBrightness+=math.sqrt(0.241*(r**2) + 0.691*(g**2) + 0.068*(b**2))
    blockBrightness = sumBrightness/numberofpixels

    #compare with standard
    return blockBrightness > standard

if __name__ == "__main__":
    #read image
    im = PIL.Image.open(image1)

    #find perceived brightnes as a standard
    ##later could be compared to and decide whether the designated block would be inked or not
    standard = standardBrightness(im)

    #initiate array to prepare storage, in output each block should be true or false
    ## true means inked; false means not inked
    outputArray = [20, 40]

    #Parametrisation
    imgwidth, imgheight = im.size
    boxHeight = imgheight//40
    boxWidth = imgwidth//20

    #for loop that produces the output array: each block should have its right true or false
    #for i,j:
    for x0 in range(0, 20):
        for y0 in range(0, 40):
            outputArray[x0][y0] = processBlock(im, x0 , y0, standard) #true or false

    #print array
    for x0 in range(0, 20):
        for y0 in range(0, 40):
            if outputArray[x0][y0] == True:
                print("[X]")
            else:
                print("[ ]")
        print("\n")




