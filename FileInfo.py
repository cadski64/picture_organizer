
# Class:    FileInfo
# Created:  12/19/2016
# Author:   Curtisd
# Purpose:  Encapsulate file information in a single class

class FileInfo:

    fileSize = 0
    filePath = None
    fileName = None

    def __init__(self, size, path, name):
        self.fileName = name
        self.filePath = path
        self.fileSize = size

    def GetFileSize(self):
        return self.fileSize

    def GetFilePath(self):
        return self.fileSize

    def GetFileName(self):
        return self.fileName

