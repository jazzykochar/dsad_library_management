# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 23:37:14 2020

@author: sidus
D:\MtechDS\Sem1\DSAD\Assignment\Assignment1Solution\dsad_library_management\src
"""
first, second, third = None, None, None

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
                node.avCntr = node.avCntr + 1
            elif inOut == 'checkOut':
                node.avCntr = node.avCntr - 1
                node.chkOutCntr = node.chkOutCntr + 1
            else:
                print('Please correct above line in prompts file as \''+str(inOut)+'\' with booking Id:\''+str(bkID)+'\' is not parseable')
        
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
        
    def _notIssued(self, bkNode):
        if bkNode:
        #First recur on left child 
            self._notIssued(bkNode.left) 
        #then print the data of node      
            self._processnotIssued(bkNode)
        # now recur on right child 
            self._notIssued(bkNode.right)
             
    def _processnotIssued(self,bkNode):
        if bkNode.chkOutCntr == 0:
            output(str(bkNode.bookID))
        
def output(text):
    parentFolder = '../data_files/'
    outputFile = 'outputPS6.txt'
    with open(parentFolder+outputFile, 'a+') as outf:
        outf.write(text+"\n") 

def main():
    
    # Path of parent folder for datasets and filenames  
    parentFolderPath = '../data_files/'
    inputFileName = 'inputPS6.txt'
    promptsFileName = 'promptsPS6.txt'
    
    #Code to read th input file and create a bst using bookId
    try:
        with open(parentFolderPath+inputFileName, 'r') as inpf:
            firstLine = inpf.readline()
            if not firstLine:
                print('Input file is empty ! Please add some books and their available counts in inputsPS6.txt')
            else:
                if ',' in firstLine:
                    print('Processing input line: ', firstLine)
                    firstLine.replace(" ","")
                    bkId, availCount = firstLine.split(",")
                    root = bookNode(int(bkId), int(availCount))
                    counter = 1
                    for i, line in enumerate(inpf.readlines()):
                        counter = counter + 1
                        if ',' in line:
                            line.replace(" ","")
                            print('Processing input line: ', line)
                            bkId,availCount = line.split(",")
                            root._readBookList(int(bkId), int(availCount))
                        else:
                            print('Line: ', i+2, ' in '+inputFileName+' not procesed ! Please use , as separator')
                    print('Binary Search Tree created successfully based on book Id !!')
                else:
                    print('Please use , as separator in inputfile')

    except FileNotFoundError:
        print('Input file does not exist !')
        if parentFolderPath == '':
            print('Please add an inputPS6.txt file in same directory as the python file')
        else:
            print('Please add an inputPS6.txt file in '+parentFolderPath+' directory')
    except:
        print('Exception occured while processing input file and creating bst. Please correct input file as per PS6')
        
    # Code to read the prompts file
    try:
        with open(parentFolderPath+promptsFileName, 'r') as prof:
            lines = prof.readlines()
            if not lines:
                print('Prompts file is empty ! Please add some prompts in promptsPS6.txt')
            else:
                for line in lines:
                    print('Processing prompt line: ', line)
                    if "check" in line:
                        #cleaning the line text
                        line.replace(" ","")
                        label, bkID = line.split(":")
                        root._chkInChkOut(int(bkID), label)                
                    elif "findBook" in line:
                        line.replace(" ","")
                        label, bkID = line.split(":")
                        root._findBook(root, int(bkID)) 
                    elif "ListTopBooks" in line:
                        global first, second, third
                        first,second, third = None, None, None
                        root._getTopBooks(root)
                        output("Top Books 1: "+str(first.bookID)+","+str(first.chkOutCntr))
                        output("Top Books 2: "+str(second.bookID)+","+str(second.chkOutCntr))
                        output("Top Books 3: "+str(third.bookID)+","+str(third.chkOutCntr))
                    elif "BooksNotIssued" in line:
                        output('List of Books not issued:')
                        root._notIssued(root)
                    elif "ListStockOut" in line:
                        output("All available copies of the below books have been checked out:")
                        root._stockOut(root)
                    elif "printInventory" in line:
                        output("There are a total of "+str(counter)+" book titles in the library.")
                        root.printBooks(root)
                    else:
                        print('Please correct above line in prompts file as it not in correct format')
        print('Program execution completed !!')
    except FileNotFoundError:
        print('Prompts file does not exist !')
        if parentFolderPath == '':
            print('Please add an promptsPS6.txt file in same directory as the python file')
        else:
            print('Please add an promptsPS6.txt file in '+parentFolderPath+' directory')
    except:
        print('An Exception occured while processing prompts file. Kindly refer to format specified in assignment PS6')

if __name__=="__main__":
    main()