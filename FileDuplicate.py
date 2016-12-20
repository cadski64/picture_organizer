
class FileDuplicate:

    fileName = None
    filePath = None
    fileList = []

    def __init__(self, fileName, filePath):
        self.fileName = fileName
        self.filePath = filePath
        self.fileList.append(filePath)

    def AddPath(self, filePath):
        self.fileList.append(filePath)

    