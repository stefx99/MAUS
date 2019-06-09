
from _io import open
import os
import shutil
from genericpath import isdir

class FileHandler(object):
    """
    classdocs
    """

    def __init__(self):
        """
        Constructor
        """
        super(FileHandler, self).__init__()

    def createFile(self, path, name):
        open(os.path.join(path, name), mode='w').close()

    def createDirectory(self, path, name):
        os.mkdir(os.path.join(path, name))

    def removeFile(self, path, name):
        os.remove(os.path.join(path, name))

    def removeDirectory(self, path, name):
        shutil.rmtree(os.path.join(path, name))

    def rename(self, path, oldName, newName):
        os.rename(os.path.join(path, oldName), os.path.join(path, newName))

    def getChildList(self, path):
        return os.listdir(path)

    def copyDir(self, src, dest):
        shutil.copytree(src, dest)

    def getType(self, path):
        if isdir(path):
            return 'FOLDER '
        else:
            return 'FILE '