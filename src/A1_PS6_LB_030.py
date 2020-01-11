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
    def printBook_process(self,bkNode):
        print(bkNode.bookID,",",bkNode.avCntr)
                   

    def printBooks(self, bkNode):
        if bkNode: 
            
            # First recur on left child 
            self.printBooks(bkNode.left) 
      
            # then print the data of node 
            #print(bkNode.bookID,", ",bkNode.avCntr)
            
            self.printBook_process(bkNode)
            
      
            # now recur on right child 
            self.printBooks(bkNode.right) 
            
    
        

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
    # Code to create the binary tree
    with open('../data_files/inputPS6.txt') as inpf:
        bkId,availCount = inpf.readline().split(",")
        print(bkId,availCount)
        root = bookNode(int(bkId), int(availCount))
        for line in inpf.readlines():
            bkId,availCount = line.split(",")
            print(bkId, availCount)
            root._readBookList(int(bkId), int(availCount))
    
#    Code to create output directory
#    if not os.path.exists('../data_files/outputPS6.txt'):
#        os.mkdir('../data_files/outputPS6.txt')
    
    with open('../data_files/prompts_printInventory.txt', 'r') as prof:
        for line in prof.readlines():
            print(line)
            with open('../data_files/outputPS6.txt', 'w') as outf:
                if "check" in line:
                    print('check')
#                    call check in out function and dont write in output file
                elif "find" in line:
                    print('find')
    #                call find book function
                elif "ListTopBooks" in line:
                    print('list top')
    #                Call function list top books
                elif "BooksNotIssued" in line:
                    print('not issued')
    #                call book not issued
                elif "printInventory" in line:
                    root.printBooks(root)
                else:
                    continue
    
if __name__=="__main__":
    main()
        
            
    # Df to Book Node
    
#    _readBookList(bkID, availCount)