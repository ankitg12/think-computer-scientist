'''
Stack is LIFO - implementing first using python List
Implement using Node later
'''

class Stack:
    def __init__(self):
        self._items = []

    def push(self,item):
        self._items.append(item)
        print "pushing : {}".format(item)
        # print "stack is now {}".format(self._items)


    def pop(self):
        item = self._items.pop()
        print "popping : {}".format(item)
        # print "stack is now {}".format(self._items)
        return item

    def isEmpty(self):
        return len(self._items) == 0

    def __str__(self):
        return str(self._items)


def checkstack():
    from random import randint
    stack = Stack()

    # insert items into stack
    for i in range(1,10):
        val=randint(1,100)
        print "going to put {} into stack".format(val)
        print "currently stack is {}".format(str(stack))
        stack.push(val)

def evalPostfix(expr):
    import re
    tokenList = re.split("[^0-9+*]",expr)
    stack=Stack()
    print "tokenList is {}".format(tokenList)
    for token in tokenList:
        #print "Processing token {}".format(token)
        if token == '' or token == ' ':
            continue
        elif token == '+':
            sum = stack.pop() + stack.pop()
            print "doing sum"
            #print "Sum is {}. pushing it to stack".format(sum)
            stack.push(sum)
            #print "Sum {} is pushed !!".format(sum)
        elif token == '*':
            product = stack.pop() * stack.pop()
            print "doing product"
            #print "Product is {}. pushing it to stack".format(product)
            stack.push(product)
            #print "Product {} is pushed !!".format(product)
        else:
            stack.push(int(token))
            #print " {} is pushed".format(token)
    print "Getting final result"
    return stack.pop()

if __name__=="__main__":
    evalPostfix("1 2 + 3 *")
