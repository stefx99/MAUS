# Embedded file name: actions\ActionManager.py
"""
Created on Apr 18, 2016

@author: Petar
"""
from actions.AddDocumentAction import AddDocumentAction
from actions.AddPageAction import AddPageAction
from actions.AddProjectAction import AddProjectAction
from actions.AddSlotAction import AddSlotAction
from actions.RemoveNodeAction import RemoveNodeAction
from actions.RenameAction import RenameAction

class ActionManager(object):
    """
    classdocs
    """

    def __init__(self, tree):
        """
        Constructor
        """
        self.tree = tree
        self.newProjectAction = AddProjectAction(tree)
        self.newDocumentAction = AddDocumentAction(tree)
        self.newPageAction = AddPageAction(tree)
        self.newSlotAction = AddSlotAction(tree)
        self.removeChildAction = RemoveNodeAction(tree)
        self.renameAction = RenameAction(tree)