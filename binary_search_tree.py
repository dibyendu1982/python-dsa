class Node :
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

class Tree:
    root = None 
    
    def add_node(self, node, value):
        if node is None:
            return Node(value)
        
        if value > node.value:
            # Add to right 
            node.right = self.add_node(node.right, value)
        else:
            # Add to left 
            node.left = self.add_node(node.left, value)
            
        return node 
    
    def print_sorted(self, node):
        if node is not None:
            self.print_sorted(node.left)
            print(node.value)
            self.print_sorted(node.right)
    
    def print_reverse_sorted(self, node):
        if node is not None:
            self.print_reverse_sorted(node.right)
            print(node.value)
            self.print_reverse_sorted(node.left)
    
ped = Tree()
ped.root = ped.add_node(ped.root, 5)
ped.root = ped.add_node(ped.root, 7)
ped.root = ped.add_node(ped.root, 1)
ped.print_sorted(ped.root)
print("Reverse Sorted")
ped.print_reverse_sorted(ped.root)

            
            
        
        
            

    
        
        