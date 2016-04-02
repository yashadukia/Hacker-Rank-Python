"""Program to Balance the Parenthesis
We will use Stack Data Structure to implement this"""

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    
number = raw_input()    #input the number of sequences
number = int(number)    #converting the number from string to int

i = 0

while (i < number):

    seq = raw_input()   #get the input sequence

    if seq == None:
        continue
        
    s = Stack()         #creating Stack() object

    for j in seq:
        if j == '(' or j == '{' or j == '[':    #push all opening parenthesis onto Stack
            s.push(j)
        elif j == ')' or j == '}' or j == ']':  #pop from Stack if we receive any closing ones
            top = s.pop()
            if (top=='(' and j!=')') or (top=='{' and j!='}') or (top=='[' and j!=']'): #Compare opening closing if same or not
                print "NO"
                #i = i+1
                break
            elif len(s.items) == 0:
                print "YES"

    i = i+1