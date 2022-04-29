#collage.py 
import dominantcolor as domCol
import filetrawler as fileTrawl
from PIL import Image

masterImage = "master.png"

images = "images\\"
images = fileTrawl.getFiles(images)
domImages = {}

for image in images:
    domImages[image] = [domCol.returnDominantColor(image),False]
    print(f"Dominant color found for image {image}:{domImages[image]}")
    #The bool was so that we can tell whether or not this image has been used before.
    #This is so that we only reuse images if we have to.

master = Image.open(masterImage)

pixel_vals = list(master.getdata())

