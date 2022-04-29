#collage.py 
import dominantcolor as domCol
import filetrawler as fileTrawl
from PIL import Image
from time import time
masterImage = "master.png"

images = "images\\"
images = fileTrawl.getFiles(images)
domImages = {}

for image in images:
    start = time()
    domImages[image] = [domCol.returnDominantColor(image),False]
    finish = time()
    print(f"Dominant color found for image {image}:{domImages[image]}.")
    print(f"Time taken:{finish-start}.")
    
    #The bool was so that we can tell whether or not this image has been used before.
    #This is so that we only reuse images if we have to.

master = Image.open(masterImage)

pixel_vals = list(master.getdata())

