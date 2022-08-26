class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist   

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    
    def pot(self):
        elements = []

        if self.left:
            elements += self.left.pot()

        if self.right:
            elements += self.right.pot()

        elements.append(self.data)

        return elements

    def prot(self):
        elements = [self.data]

        if self.left:
            elements += self.left.prot()
        
        if self.right:
            elements += self.right.prot()
        
        return elements

    
    def find_max(self):
        if not self.right:
            return self.data

        if self.right:
            return self.right.find_max()
    
    def find_min(self):
        if not self.left:
            return self.data
        
        if self.left:
            return self.left.find_min()
    
    def deletey(self,val): 
        if val < self.data:
            if self.left:
                self.left = self.left.deletey(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.deletey(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
        
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.deletey(min_val)
        
        return self
    

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    # countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    # country_tree = build_tree(countries)

    # print("UK is in the list? ", country_tree.search("UK"))
    # print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])

    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pot())
    print(numbers_tree.prot())

    sret = build_tree([4,1,5])
    sret.deletey(1)
    print(sret.in_order_traversal())
 
