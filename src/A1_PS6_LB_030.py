# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 23:37:14 2020

@author: sidus
D:\MtechDS\Sem1\DSAD\Assignment\Assignment1Solution\dsad_library_management\src
"""
stockout_count = 0
first, second, third = None, None, None

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
    
    def _findBook(self, eNode, bkID):
        if eNode: 
            if eNode.bookID == bkID:
                if eNode.avCntr > 0:
                    output("Book id "+str(bkID)+" is available for checkout")
                else:
                    output("All copies of the book id "+str(bkID)+" have been checked out")            
            elif bkID<eNode.bookID:
            # First recur on left child 
                self._findBook(eNode.left, bkID)
            else:
            # now recur on right child 
                self._findBook(eNode.right, bkID) 
        else:
            output("Book id "+str(bkID)+" does not exist")

    def _getTopBooks(self, bkNode):
        global first, second, third 
        if bkNode: 
            # First recur on left child 
            self._getTopBooks(bkNode.left) 
            
            if first == None:
                first = bkNode
            elif second == None:
                if first.chkOutCntr < bkNode.chkOutCntr:
                    second = first
                    first = bkNode
                else:
                    second = bkNode
            elif third == None:
                if second.chkOutCntr < bkNode.chkOutCntr:
                    third = second
                    if first.chkOutCntr < bkNode.chkOutCntr:
                        second = first
                        first = bkNode
                    else:
                        second = bkNode
                else:
                    third = bkNode
            else:
                # then process the data of node
                if bkNode.chkOutCntr > first.chkOutCntr:
                    third = second
                    second = first
                    first = bkNode
                elif bkNode.chkOutCntr > second.chkOutCntr:
                    third = second
                    second = bkNode
                elif bkNode.chkOutCntr > third.chkOutCntr:
                    third = bkNode
       
            # now recur on right child 
            self._getTopBooks(bkNode.right) 

    def _stockOut(self, bkNode):
         if bkNode: 
            # First recur on left child 
            self._stockOut(bkNode.left) 
            # then print the data of node      
            self._processStockOut(bkNode)
            # now recur on right child 
            self._stockOut(bkNode.right)
 
    def _processStockOut(self,bkNode):
        if bkNode.avCntr == 0:
            output(str(bkNode.bookID))

    def _chkInChkOut(self, bkID, inOut):
        node = self._getNode(self, bkID)
        if node:
            if inOut == 'checkIn':
                print('avail counter: ', node.avCntr)
                node.avCntr = node.avCntr + 1
            elif inOut == 'checkOut':
                print('avail counter: ', node.avCntr)
                node.avCntr = node.avCntr - 1
                node.chkOutCntr = node.chkOutCntr + 1
        
    def _getNode(self, eNode , bkID):
        if eNode: 
            if eNode.bookID==bkID:
                return eNode
            
            elif bkID<eNode.bookID:
            # First recur on left child 
                return self._getNode(eNode.left, bkID)
            else:
            # now recur on right child 
                return self._getNode(eNode.right, bkID) 
        else:
            return None
        
def output(text):
    with open('../data_files/outputPS6.txt', 'a+') as outf:
        outf.write(text+"\n") 

def main():
    # Code to create the binary tree
    with open('../data_files/inputPS6.txt') as inpf:
        bkId, availCount = inpf.readline().split(",")
        print(bkId,availCount)
        root = bookNode(int(bkId), int(availCount))
        counter = 1
        for i, line in enumerate(inpf.readlines()):
            counter = counter + 1
            bkId,availCount = line.split(",")
            print(bkId, availCount)
            root._readBookList(int(bkId), int(availCount))
    
    with open('../data_files/promptsPS6.txt', 'r') as prof:
        for line in prof.readlines():
            print(line)
            if "check" in line:
                #cleaning the line text
                line.replace(" ","")
                label, bkID = line.split(":")
                root._chkInChkOut(int(bkID), label)                
            elif "findBook" in line:
#               cleaning the line text
                line.replace(" ","")
                label, bkID = line.split(":")
                root._findBook(root, int(bkID)) 
#                call find book function
            elif "ListTopBooks" in line:
                global first, second, third
                first,second, third = None, None, None
                root._getTopBooks(root)
                output("Top Books 1: "+str(first.bookID)+","+str(first.chkOutCntr))
                output("Top Books 2: "+str(second.bookID)+","+str(second.chkOutCntr))
                output("Top Books 3: "+str(third.bookID)+","+str(third.chkOutCntr))
#                Call function list top books
            elif "BooksNotIssued" in line:
                print('not issued')
#                call book not issued
            elif "ListStockOut" in line:
                output("All available copies of the below books have been checked out:")
                root._stockOut(root)
            elif "printInventory" in line:
                output("There are a total of "+str(counter)+" book titles in the library.")
                root.printBooks(root)
            else:
                continue

if __name__=="__main__":
    main()