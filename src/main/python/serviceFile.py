# serviceFile.py

#import regex
# , remove
from os import (access, R_OK, pardir)
# , exists
from os.path import (isfile, join, abspath)


import pysrt


class ServiceFile:
    def __init__(self):
        # 字符串,所支持的不带点号的文件扩展名的小写所组成的列表
        # 常用的字幕文件格式 srt,ass,vtt,ssa(SubStation Alpha)
        '''
        SubRip: srt


        SubRip, MicroDVD and MPL2 formats
        https://en.wikipedia.org/wiki/SubStation_Alpha

        '''
        self.supportedExtToLowerWithoutDot = ["srt", "ass"]
        # 字符串,当前文件的扩展名,例如 `.srt`
        self.fileExt = ""
        # 字符串,当前实例打开的文件路径
        self.filePath = ""
        # 对象类型的列表
        # 对象的结构示意{"text“:999,"start":对象,"end":对象}
        self.items = []
       #  弃用该属性
        self.parentDir = ''


###########################

    def isFileReadable(self, fileName):
        try:
            if isfile(fileName) and access(fileName, R_OK):
                return True
            return False
        except:
            return False

    def isStrContain(self, s, t):

        if s is None or len(s) == 0:
            return False
        return str.find(s, t) != -1
###########################

    def setItems(self, items):
        self.items = items

    def setFilePath(self, filePath):
        '''设置当前实例的文件名
        '''
        self.filePath = filePath
        #  os.path.abspath(os.path.join(yourpath, os.pardir))
        #  弃用该属性
        self.parentDir = abspath(join(filePath, pardir))

    def getFilePath(self):
        '''获取当前实例的文件名属性
        '''
        return self.filePath

    def parseItems(self):
        '''获取当前文件名的文件里的可翻译条目的应翻译字符串
        '''
        if len(self.items) != 0:
            return 1

        if len(self.filePath) == 0:
            return 2

        fileExtWithoutDot = self.filePath.split(".")[-1].lower()
        if fileExtWithoutDot not in self.supportedExtToLowerWithoutDot:
            return 3
        self.fileExt = "."+fileExtWithoutDot
        return self.parseSubtitleAndSetItems(fileExtWithoutDot)

    def parseSubtitleAndSetItems(self, format="srt"):
        '''解析正确则返回0,否则返回大于10的错误代码
        '''

        if format == "srt":
            return self.parseSrtAndSetItems()
        elif format == "ass":
            return self.parseAssAndSetItems()
        return 999

    def parseAssAndSetItems(self):

        return 666

    def parseSrtAndSetItems(self):
        try:
            self.items = pysrt.open(self.filePath, encoding='utf8')
            return 0
        except:
            return 11

    def rreplace(s, oldStr, newStr, count):
        '''
        替换字符串中oldStr最后count次出现的位置为newStr
        '''
        li = s.rsplit(oldStr, count)
        return newStr.join(li)

    def saveToFile(self, subs, languageDest, isBilingual=False):
        '''
        把当前实例对应的文件名和目标语种做相应处理后,把当前实例
        的items保存到文件中

        '''
        try:

            newStr = '-'+languageDest+self.fileExt if isBilingual == False else '-' + \
                languageDest+"-Bilingual"+self.fileExt
            targetFilePath = self.filePath.replace(self.fileExt, newStr, -1)
            print(targetFilePath)
            subs.save(targetFilePath, encoding='utf-8')
            return True
        except:
            return False
