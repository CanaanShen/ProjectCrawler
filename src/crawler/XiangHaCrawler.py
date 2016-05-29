# -*- coding: utf-8 -*- 

'''
Created on 2016 

@author: Yueshen
'''

import os
import urllib.request

class XiangHaCrawler:
    
    def crawlXiangHa(self, rootURL, outDir):
        
        head = {
                'Connection': 'Keep-Alive',
                'Accept': 'text/html, application/xhtml+xml, */*',
                'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
        
        opener = urllib.request.build_opener()
        header = []
        for key, value in head.items():
            elem = (key, value)
            header.append(elem)
        
        opener.addheaders = header
        content = opener.open(rootURL).read()
        print(content)
    #def
#class

if __name__ == '__main__':
    
    rootURL = r"http://www.xiangha.com/shicai/%E7%8C%AA%E8%82%89"
    outRootDir = r"../../data"
    
    if not os.path.exists(outRootDir):
        os.mkdir(outRootDir)
    
    website = "xiangha"
    outDir = os.path.join(outRootDir, website)
    if not os.path.exists(outDir):
        os.mkdir(outDir)
    
    xianghaCrawler = XiangHaCrawler()
    xianghaCrawler.crawlXiangHa(rootURL, outDir)
    
    print("Program ends")