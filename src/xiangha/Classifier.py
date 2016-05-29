
'''
@author: Yueshen

'''

import os
import codecs
import shutil

def readListAndMap(inFile):
    
    nameNumMap = {}
    content = codecs.open(inFile).readlines()
    
    if len(content) == 0:
        print("The length of the content is 0")
        return nameNumMap
    #if
    num = 0
    for line in content:
        line = line.decode('gbk').strip('\n').strip()
        nameNumMap[line] = num
        num = num + 1
    #for
    
    return nameNumMap
    
#def
    
def classifierHTMLFiles(inRootDir, outRootDir, website):
    
    inFile = os.path.join(inRootDir, "foodlist.txt")
    nameNumMap = readListAndMap(inFile)
    
    htmlDir = os.path.join(inRootDir, website)
    for htmlFile in os.listdir(htmlDir):
        fileName = htmlFile.replace(".html", "")
        if fileName in nameNumMap:
            num = nameNumMap[fileName]
            fileName = str(num) + " " + fileName
            print(fileName)
        else:
            print("The num of ", fileName, " does not exist")
        #if
        
        htmlFilePath = os.path.join(htmlDir, htmlFile)
        newHTMLFilePath = os.path.join(outRootDir, fileName + ".html")
        shutil.copy(htmlFilePath, newHTMLFilePath)
    #for
#def


if __name__ == '__main__':
    
    inRootDir = r'C:\Users\Yueshen\workspace_luna\crawl_data_homedepot_lowes_java\xiangha'
    outRootDir = r'C:\Users\Yueshen\git\ProjectCrawler\data\xiangha'
    website = "www.xiangha.com"
    
    classifierHTMLFiles(inRootDir, outRootDir, website)
    print("Program ends")
#if