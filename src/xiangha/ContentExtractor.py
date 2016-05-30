'''

@author: Yueshen
'''

import os
import re
from bs4 import BeautifulSoup
import codecs

def extractContent(inRootDir, outRootDir):
    
    firstIndent = "    "
    secondIndent = firstIndent + "    "
    thirdIndent = secondIndent + "    "
    fourthIndent = thirdIndent + "    "
    
    for folder in os.listdir(inRootDir):
        folderPath = os.path.join(inRootDir, folder)
        firstCategory = folder
        for subFolder in os.listdir(folderPath):
            subFolderPath = os.path.join(folderPath, subFolder)
            secondCategory = subFolder
            
            for htmlFile in os.listdir(subFolderPath):
                htmlFilePath = os.path.join(subFolderPath, htmlFile)
                htmlFile = htmlFile.replace(".html", "")
                numName = htmlFile.strip("\n").strip().split()

                if len(numName) < 2:
                    print("The length of numName is less than 2")
                    continue
                num = numName[0]
                name = numName[1]
                
                outXMLFilePath = os.path.join(outRootDir, htmlFile + ".xml")
#                 if  os.path.exists(outXMLFilePath):
#                     continue
                fileHandler = open(outXMLFilePath, "w")

                fileHandler.write("<content>\n\n")
                    
                fileHandler.write(firstIndent + "<id>\n")
                fileHandler.write(secondIndent + str(num) + "\n")
                fileHandler.write(firstIndent + "</id>\n\n")
                    
                fileHandler.write(firstIndent + "<name>\n")
                fileHandler.write(secondIndent + str(name) + "\n")
                fileHandler.write(firstIndent + "</name>\n\n")
                
                fileHandler.write(firstIndent + "<firstcategory>\n")
                fileHandler.write(secondIndent + folder + "\n")
                fileHandler.write(firstIndent + "</firstcategory>\n\n")
                
                fileHandler.write(firstIndent + "<secondcategory>\n")
                fileHandler.write(secondIndent + subFolder + "\n")
                fileHandler.write(firstIndent + "</secondcategory>\n\n")
                
                try:
                    content = codecs.open(htmlFilePath, "r", "utf-8").read()
                    soup = BeautifulSoup(content, "html.parser")

                    #alias, taboo and suit
                    divList = soup.findAll('div', class_ = 'ins')
                    if divList is None or divList == "" or len(divList) < 1:
                        #print("There is no divList in ", htmlFile)
                        fileHandler.write(firstIndent + "<alias>\n")
                        fileHandler.write("\n")
                        fileHandler.write(firstIndent + "</alias>\n\n")

                        fileHandler.write(firstIndent + "<taboo>\n")
                        fileHandler.write("\n")
                        fileHandler.write(firstIndent + "</taboo>\n\n")

                        fileHandler.write(firstIndent + "<suit>\n")
                        fileHandler.write("\n")
                        fileHandler.write(firstIndent + "</suit>\n\n")
                        
                    else:
                        div = divList[0]
                        pList = div.findAll('p')
                        fileHandler.write(firstIndent + "<alias>\n")
                        for pTag in pList:
                            pText = pTag.text
                            if "别名："in pText:
                                pText = pText.replace("别名：", "")
                                fileHandler.write(secondIndent + pText + "\n")
                                break
                            #if
                        #for
                        fileHandler.write(firstIndent + "</alias>\n\n")
                        
                        fileHandler.write(firstIndent + "<taboo>\n")
                        for pTag in pList:
                            pText = pTag.text
                            if "禁忌人群：" in pText:
                                pText = pText.replace("禁忌人群：", "")
                                fileHandler.write(secondIndent + pText + "\n")
                                break
                            #if
                        #for
                        fileHandler.write(firstIndent + "</taboo>\n\n")
                        
                        fileHandler.write(firstIndent + "<suit>\n")
                        for pTag in pList:
                            pText = pTag.text
                            if "适宜人群：" in pText:
                                pText = pText.replace("适宜人群：", "")
                                fileHandler.write(secondIndent + pText + "\n")
                                break
                        #for
                        fileHandler.write(firstIndent + "</suit>\n\n")
                    #if...else
                    
                    ulTag = soup.find('ul', id = 'eleInfo')
                    if ulTag is None or ulTag == "" or len(ulTag) < 1 :
                        #print("There is no ulTag in ", htmlFile)
                        fileHandler.write(firstIndent + "<ingredient>\n")
                        fileHandler.write("\n")
                        fileHandler.write(firstIndent + "</ingredient>\n\n")
                    else:
                        liList = ulTag.findAll("li")
                        if liList is None or liList == "" or len(liList) < 1:
                            print()
                            #print("There is no liList in ", htmlFile)
                        else:
                            fileHandler.write(firstIndent + "<ingredient>\n")
                            for liTag in liList:
                                fileHandler.write(secondIndent + "<element>\n")
                                spanTag = liTag.find('span')
                                name = spanTag.text
                                fileHandler.write(thirdIndent + "<name>\n")
                                fileHandler.write(fourthIndent + name + "\n")
                                fileHandler.write(thirdIndent + "</name>\n")
                                
                                emTag = liTag.find('em')
                                value = emTag.text
                                fileHandler.write(thirdIndent + "<value>\n")
                                fileHandler.write(fourthIndent + value + "\n")
                                fileHandler.write(thirdIndent + "</value>\n")
                                
                                fileHandler.write(secondIndent + "</element>\n")
                            #for
                            fileHandler.write(firstIndent + "</ingredient>\n\n")
                        #if...else...
                    #if...else
                    
                    divTag = soup.find('div', class_ = "ing_ins")
                    h2List = divTag.findAll('h2')
                    pList = divTag.findAll('p')
                    
                    h2Size = len(h2List)
                    fileHandler.write(firstIndent + "<introduction>\n")
                    try:
                        mark = 0
                        for i in range(0, h2Size):
                            if "介绍" in h2List[i].text:
                                pTag = pList[i]
                                introduction = str(pTag)
                                introduction = introduction.replace("<p>", "").replace("</p>", "").replace("</br>", "").replace("</a>", "")
                                introduction = introduction.replace("<br>", "\n" + secondIndent)
                                introduction = re.sub(r"<.*>", "", introduction)
                                fileHandler.write(secondIndent + introduction + "\n")
                                mark = 1
                                break
                            #if
                        #for
                        if mark == 0:
                            fileHandler.write("\n")
                        #if
                    except Exception as e:
                        print(htmlFile, " ", e)
                        fileHandler.write("\n")
                        fileHandler.write(firstIndent + "</introduction>\n\n")
                    
                    fileHandler.write(firstIndent + "</introduction>\n\n")
         
                    fileHandler.write(firstIndent + "<effect>\n")
                    try:
                        mark = 0
                        for i in range(0, h2Size):
                            if "功效与作用" in h2List[i].text:
                                pTag = pList[i]
                                effect = str(pTag)
                                effect = effect.replace("<p>", "").replace("</p>", "").replace("</br>", "").replace("</a>", "")
                                effect= effect.replace("<br>", "\n" + secondIndent)
                                effect = re.sub(r"<.*>", "", effect)
                                fileHandler.write(secondIndent + effect + "\n")
                                mark = 1
                                break
                            #if
                        #for
                        if mark == 0:
                            fileHandler.write("\n")
                    except Exception as e:
                        print(htmlFile, " ", e)
                        fileHandler.write("\n")
                        fileHandler.write(firstIndent + "</effect>\n\n")
                    
                    fileHandler.write(firstIndent + "</effect>\n\n")
                    
                    fileHandler.write(firstIndent + "<nutritive>\n")
                    try:
                        mark = 0
                        for i in range(0, h2Size):
                            if "营养" in h2List[i].text:
                                pTag = pList[i]
                                nutritive = str(pTag)
                                nutritive = nutritive.replace("<p>", "").replace("</p>", "").replace("</br>", "").replace("</a>", "")
                                nutritive = nutritive.replace("<br>", "\n" + secondIndent)
                                nutritive = re.sub(r"<.*>", "", nutritive)
                                fileHandler.write(secondIndent + nutritive + "\n")
                                mark = 1
                                break
                            #if
                        #for
                        if mark == 0:
                            fileHandler.write("\n")
                    except Exception as e:
                        print(htmlFile, " ", e)
                        fileHandler.write("\n")
                        fileHandler.write(firstIndent + "</nutritive>\n\n")
                    
                    fileHandler.write(firstIndent + "</nutritive>\n\n")
                    
                    fileHandler.write(firstIndent + "<cuisine>\n")
                    try:
                        mark = 0
                        for i in range(0, h2Size):
                            if "食用方法" in h2List[i].text:
                                pTag = pList[i]
                                cuisine = str(pTag)
                                cuisine = cuisine.replace("<p>", "").replace("</p>", "").replace("</br>", "").replace("</a>", "")
                                cuisine = cuisine.replace("<br>", "\n" + secondIndent)
                                cuisine = re.sub(r"<.*>", "", cuisine)
                                fileHandler.write(secondIndent + cuisine + "\n")
                                mark = 1
                                break
                            #if
                        #for
                        if mark == 0:
                            fileHandler.write("\n")
                        #if
                    except Exception as e:
                        print(htmlFile, " ", e)
                        fileHandler.write("\n")
                        fileHandler.write(firstIndent + "</cuisine>\n\n")
                    
                    fileHandler.write(firstIndent + "</cuisine>\n\n")

                    fileHandler.write(firstIndent + "<pictureweburl>\n")
                    divTag = soup.find('div', class_ = "pic")
                    if divTag is None or divTag == "" or len(divTag) < 1:
                        fileHandler.write("\n")
                    else:
                        imgTag = divTag.find('img')
                        srcAttribute = imgTag['src']                #get the value of an attribute
                        fileHandler.write(secondIndent + srcAttribute + "\n")
                    #if...else
                    fileHandler.write(firstIndent + "</pictureweburl>\n\n")
                    
                    fileHandler.write(firstIndent + "<picturelocalurl>\n")
                    fileHandler.write("\n")
                    fileHandler.write(firstIndent + "</picturelocalurl>\n\n")
                    
                    fileHandler.write("</content>\n")
                    #print(htmlFile)
                    fileHandler.close()
                    
                except Exception as e:
                    print(htmlFile, " error reason: ", e)       
                    fileHandler.write("</content>\n")
                    print(htmlFile)
                    fileHandler.close()
                #try...except
    #for
    
#def

if __name__ == '__main__':
    
    rootDir = r"C:\Users\Yueshen\git\ProjectCrawler\data\xiangha"
    inRootDir = os.path.join(rootDir, "category")
    outRootDir = os.path.join(rootDir, "foodtextbase")
    
    extractContent(inRootDir, outRootDir)
    print("Program ends")
#if