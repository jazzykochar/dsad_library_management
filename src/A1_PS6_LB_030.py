# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 23:37:14 2020

@author: sidus
D:\MtechDS\Sem1\DSAD\Assignment\Assignment1Solution\dsad_library_management\src
"""

stockout_count = 0
stockout_list =[]
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
                   
    def printBooks(self, bkNode):
        if bkNode: 
            
            # First recur on left child 
            self.printBooks(bkNode.left) 
      
            # then print the data of node      
            output(str(bkNode.bookID)+","+str(bkNode.avCntr))
            
            # now recur on right child 
            self.printBooks(bkNode.right) 

    def _stockOut(self, bkNode):
         if bkNode: 
            # First recur on left child 
            self._stockOut(bkNode.left) 
            # then print the data of node      
            self._processStockOut(bkNode)
            # now recur on right child 
            self._stockOut(bkNode.right)
 
            
    def _processStockOut(self,bkNode):
        global stockout_count
        if bkNode.avCntr == 0:
            stockout_list.append(bkNode)  
            stockout_count = stockout_count +1
            output(str(bkNode.bookID))
#            print(bkNode.bookID)

            
def output(text):
    with open('../data_files/outputPS6.txt', 'a+') as outf:
        outf.write(text+"\n") 
#def_chkInChkOut(self, bkID, inOut):

#def _getTopBooks(self, bkNode):
#
#def _notIssued(self, bkNode):
#    
#def _findBook(self, eNode, bkID):
#
   
        
#
def main():
    # Code to create the binary tree
    with open('../data_files/inputPS6.txt') as inpf:
        bkId,availCount = inpf.readline().split(",")
        print(bkId,availCount)
        root = bookNode(int(bkId), int(availCount))
        counter = 1
        for i, line in enumerate(inpf.readlines()):
            counter = counter + 1
            bkId,availCount = line.split(",")
            print(bkId, availCount)
            root._readBookList(int(bkId), int(availCount))
    
#    Code to create output directory
#    if not os.path.exists('../data_files/outputPS6.txt'):
#        os.mkdir('../data_files/outputPS6.txt')
    
    with open('../data_files/prompts_stockout.txt', 'r') as prof:
        for line in prof.readlines():
            print(line)
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
            elif "ListStockOut" in line:
                output("All available copies of the below books have been checked out:")
                root._stockOut(root)
                print(stockout_count)
                for i in stockout_list: 
                    print(i.bookID) 
    
            elif "printInventory" in line:
                output("There are a total of "+str(counter)+" book titles in the library.")
                root.printBooks(root)
            else:
                continue
    
if __name__=="__main__":
    main()
        
            
    # Df to Book Node
    
#    _readBookList(bkID, availCount)