#collage.py 
from cmath import inf
import dominantcolor as domCol
import filetrawler as fileTrawl
from PIL import Image
import PIL
from time import time
import numpy as np
masterImage = "master.png"

images = "images\\"
images = fileTrawl.getFiles(images)
images = fileTrawl.searchFiles(images,"",".jpg")
domImages = {}
averageTime = 0
i=0
for image in images:
    start = time()
    domImages[image] = [domCol.returnDominantColor(image)]
    finish = time()
    print(f"Dominant color found for image {image}:{domImages[image]}.")
    print(f"Time taken:{finish-start}.")

    i += 1
    averageTime+= finish-start
    print(f"Average: {averageTime/i}")

master = Image.open(masterImage)

pixel_vals = list(master.getdata())
def checkSimilarity(rgb1,rgb2,tolerance=10):
    if rgb1[0] > rgb2[0]-tolerance and rgb1[0] < rgb2[0]+tolerance:
        if rgb1[1] > rgb2[1]-tolerance and rgb1[1] < rgb2[1]+tolerance:
            if rgb1[2] > rgb2[2]-tolerance and rgb1[2] < rgb2[2]+tolerance:
                return True

    return False

pixelImages = [[]]
i=0
j=0
for pixel_val in pixel_vals:
    i+=1
    for image in domImages:
        j+=1
        imageTuple = domImages[image]
        if checkSimilarity(pixel_val,imageTuple[0]):
            print(f"{pixel_val} is similar to {image}")
            pixelImages[j[i]] = Image.open(image)
record = {"width":100000000,"height":10000000}
for row in pixelImages:
    for image in row:
        if image.height < record.height:
            record.height = image.height
            record.width = image.width
"""
for i in range(0,len(pixelImages)):
    for j in range(0,len(pixelImages[i])):
        pixel
"""