'''

@author: Yueshen
'''

import os
import codecs

def generateCategory(categoryFile, categoryFolder):
    
    content = codecs.open(categoryFile).readlines()
    
    if len(content) == 0:
        print("The length of the content is 0")
        return
    #if
    
    numFolderNameMap = {}
    for line in content:
        line = line.decode("gbk").strip("\n").strip()
        if line.find(":") > 0:
            folderName = line.split(":")[1].strip("\n").strip()
            num = line.split(":")[0].strip("\n").strip()
            numFolderNameMap[num] = folderName
            folderPath = os.path.join(categoryFolder, folderName)
            
            if not os.path.exists(folderPath):
                os.mkdir(folderPath)
        #if
        else:
            if line.find(",") > 0:
                commaList = line.split(",")
                if len(commaList) < 3:
                    print("Then length of commaList is less than 3")
                    continue
                #if
                num = commaList[0].strip("\n").strip()
                fatherFolderName = numFolderNameMap[num]
                folderName = commaList[2].strip("\n").strip()
                folderPath = os.path.join(categoryFolder, fatherFolderName, folderName)
                
                if not os.path.exists(folderPath):
                    os.mkdir(folderPath)
            else:
                print("Folder name errors")
            #else
        #else
    #for
#def

if __name__ == '__main__':
    
    rootDir = r"C:\Users\Yueshen\git\ProjectCrawler\data\xiangha"
    categoryFile = os.path.join(rootDir, "foodcategory.txt")
    categoryFolder = os.path.join(rootDir, "category")
    
    generateCategory(categoryFile, categoryFolder)
    print("Program ends")
    
#if