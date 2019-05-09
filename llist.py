class Node:
    def __init__(self,cargo=None, next=None):
        self.cargo=cargo
        self.next=next

    def __str__(self):
        return str(self.cargo)

def printList(node):
    while node:
        print node,
        node = node.next
    print

def printBackward(list):
    if list == None: return
    printBackward(list.next)
    print list,

# Implement
# sorting the items
def sortList(list):
    pass

# removing particular item
def removeItem(list,item):
    pass


# remove items at particular index
def removeItemAtIndex(list,index):
    pass

def contains(list,item):
    node = list
    while node:
        if node.cargo == item:
            return True
        # update the variable to point to the next item
        # otherwise it'd be infinite loop
        node = node.next
    return False

if __name__=="__main__":
    from random import randint
    node0=Node(-1)

    # make the nodes
    for i in range(1,10):
        val = randint(1,100)
        makenode = 'node{}=Node({})'.format(i,val)
        print (makenode)
        exec(makenode)

    # link the nodes
    for i in range(1,10):
        linknode = 'node{}.next = node{}'.format(i-1,i)
        print(linknode)
        exec(linknode)
