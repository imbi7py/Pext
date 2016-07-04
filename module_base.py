from abc import ABC, abstractmethod


class ModuleBase(ABC):
    @abstractmethod
    def __init__(self, binary, vm, window, q):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def getSupportedCommands(self):
        pass

    @abstractmethod
    def getCommands(self):
        pass

    @abstractmethod
    def getEntries(self):
        pass

    @abstractmethod
    def copyEntryToClipboard(self, entryName):
        pass

    @abstractmethod
    def getAllEntryFields(self, entryName):
        pass

    @abstractmethod
    def runCommand(self, command, printOnSuccess=False, hideErrors=False):
        pass