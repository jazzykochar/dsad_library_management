# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 23:37:14 2020

@author: sidus
D:\MtechDS\Sem1\DSAD\Assignment\Assignment1Solution\dsad_library_management\src
"""

class bookNode:
    def __init__(self, bkID, availCount):
        self.bookID = bkID
        self.avCntr = availCount
        self.chkOutCntr = 0
        self.left = None
        self.right = None
        
    def insert(self): 
        if self. is None: 
            root = node 
        else: 
            if root.val < node.val: 
                if root.right is None: 
                    root.right = node 
                else: 
                    insert(root.right, node) 
            else: 
                if root.left is None: 
                    root.left = node 
                else: 
                    insert(root.left, node) 
def _readBookList(self, bkID, availCount):


#def printBooks(self, bkNode):

#def_chkInChkOut(self, bkID, inOut):

#def _getTopBooks(self, bkNode):
#
#def _notIssued(self, bkNode):
#    
#def _findBook(self, eNode, bkID):
#
#def _stockOut(self, eNode):
#

if __name__ == "__main__":
    # Read 
    with open('../data_files/inputPS6.txt') as f:
        for line in f:
            split = line.split(",")
            bookNode(split[0], split[1])
            
    # Df to Book Node
    
#    _readBookList(bkID, availCount)