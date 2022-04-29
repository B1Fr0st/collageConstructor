#filetrawler.py 
from array import array
import os,time

def getFiles(dir,num=False,recursive=False,verbose=True):
    if recursive == False:
        string = f"Starting getFiles on target directory {dir}, with args num={num},recursive={recursive},verbose={verbose}"
        print("#"*len(string))
        print(string)
        print("#"*len(string))
    """
       dir=path to walk
       num=Whether to print the number of files found
       recursive=Whether the call is a recursive call by the function.
       verbose=Whether or not to print each file found.
    """
    
    #gets all of the files in a directory,including the ones in
    #subdirectories, and returns it in a list format.

    try:
        listOfFiles = os.listdir(dir)#locate all files including subdirs
    except PermissionError:
        print(f"Permission denied to {dir}","Warning")
        time.sleep(2)
        return []

    allFiles = []

    for entry in listOfFiles:

        path = os.path.join(dir,entry)#creates full path

        if os.path.isdir(path):#if the path is a directory
            print(f"Branching:{path}")
            allFiles = allFiles + getFiles(path,recursive=True)#recursively call getFiles
        else:
            if verbose == True:
                #print(f"File Located:{path}")
                pass
            allFiles.append(path)#adds the singular file to the list

    if num:
        print("Files Located:"+str(len(allFiles)))

    return allFiles






def searchFiles(files,keywords,imageType,verbose=True):
    """
    files=The files to search through
    keywords=Keywords to look for
    imageType=What type of file you want returned.
    """
    if keywords is not array:
        print("Keyword was string. Converting to array.")
        keywords = [keywords]
    matches = []
    for file in files:
        for keyword in keywords:
            if keyword in file and file not in matches:
                if imageType in file:
                    matches.append(file)
                    if verbose == True:
                        print(f"Match for keyword '{keyword}' found: {file}")
    print(f"Total matches found: {len(matches)}")
    return matches










def slimArray(array):
    newArray = []
    print(f"Slimming down {len(array)} items.")
    for i in range(0,len(array)):
        item = array[i]
        if item not in newArray:
            newArray.append(item)
        if i%1000 == 0:
            print(f"{i} items processed.")
    print(f"Pruned {len(array)-len(newArray)} items. New array: {len(newArray)} items.")
    return newArray