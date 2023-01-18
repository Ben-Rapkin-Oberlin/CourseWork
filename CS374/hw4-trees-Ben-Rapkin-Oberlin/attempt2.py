from pptree import *

class Node:

    def __init__(self,label='root', attribute='root', children=None, defualt=None):
        self.label=label #which column to look at
        self.attribute = attribute #which attribute is used to split the data
        self.children = {}
        self.default = defualt #the most popular label at that node, used for prediction if attribute is not found

    def add_child(self,label, attribute):
        self.children[attribute] = Tree(label,attribute)


class Tree:
    def __init__(self, attribute='root',label='root',father=None, children=[]):
        self.attribute = attribute #which attribute is used to split the data on this branch
        #self.father=father
        self.label=label
        self.children=[]
        if father:
            father.children.append(self)

    def __str__(self):
        return self.function
root=Tree('root')

sunny=Tree('sunny',root)
overcast=Tree('overcast',root)
rainy=Tree('rainy',root)

print_tree(root,"children", "attribute",horizontal=False)

