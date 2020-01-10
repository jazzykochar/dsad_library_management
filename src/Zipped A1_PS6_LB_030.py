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
                    
    def _readBookList(self, bkID, availCount):
        
        node = bookNode(bkID, availCount)
        if self is None: 
            self = node 
        else: 
            if self.bookID < node.bookID: 
                if self.right is None: 
                    self.right = node 
                else: 
                    self.right._readBookList(bkID, availCount) 
            else: 
                if self.left is None: 
                    self.left = node 
                else: 
                   self.left._readBookList(bkID, availCount)

    def _printBooks(self, bkNode):
        if bkNode: 
            
            # First recur on left child 
            self._printBooks(bkNode.left) 
      
            # then print the data of node 
            print(bkNode.bookID)
      
            # now recur on right child 
            self._printBooks(bkNode.right) 
        
#def_chkInChkOut(self, bkID, inOut):

#def _getTopBooks(self, bkNode):
#
#def _notIssued(self, bkNode):
#    
#def _findBook(self, eNode, bkID):
#
#def _stockOut(self, eNode):
#
def main():
    # Read 
    with open('../data_files/inputPS6.txt') as f:
        bkId,availCount = f.readline().split(",")
        root = bookNode(int(bkId), int(availCount))
        for line in f.readlines():
            bkId,availCount = line.split(",")
#            print(bkId, availCount)
            root._readBookList(int(bkId), int(availCount))
    
    root._printBooks(root)
    
if __name__=="__main__":
    main()
        
            
    # Df to Book Node
    
#    _readBookList(bkID, availCount)