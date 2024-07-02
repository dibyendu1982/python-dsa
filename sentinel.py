class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None 
        
class Sentinel:
    def __init__(self, *args):
        self.head = Node(None)
        self.tail = Node(None)
        # ~% Initially the sentinel has the head and tail connected to each other
        self.head.next = self.tail
        self.tail.prev = self.head
        self.add_to_back(args)
        # if len(args) > 0:
        #     self.add_to_back(args)
    
    def find_node(self, value):
        current = self.head.next
        while current is not self.tail:
            if current.value == value:
                return current
            current = current.next
        return None
    
    def insert(self, current, new_value):
        spot = Node(new_value)
        spot.next = current.next 
        spot.prev = current
        
        current.next.prev = spot
        current.next = spot
        return True
    
    def add_to_front(self, *args):
        if len(args) == 0: 
            return
        for arg in args:
            self.insert(self.head, arg)
    
    def add_to_back(self, *args):
        if len(args) == 0: 
            return
        for arg in args:
            self.insert(self.tail.prev, arg)
    
    def insert_after(self, existing_value, *args):
        current_node = self.find_node(existing_value)
        if current_node is not None:
            for arg in args:
                self.insert(current_node, arg)
        return current_node is not None 
      
    def insert_before(self, existing_value, *args):
        current_node = self.find_node(existing_value)
        if current_node is not None: 
            for arg in args:
                self.insert(current_node.prev, arg)
        return current_node is not None 
    
    def remove_values(self, *args):
        # ~% Instead of going through linked list values go through the parameters passed 
        # ~% This implementation removes all of the occurrences of the value in the list
        remove_list = []
        current_node = self.head.next 
        # for arg in args:
        while current_node is not self.tail: 
            if current_node.value in args and current_node is not None: 
                remove_list.append(current_node.value)
                current_node.next.prev = current_node.prev
                current_node.prev.next = current_node.next
            current_node = current_node.next
        return remove_list
    
    def print_forward(self):
        current_node = self.head.next
        while current_node is not self.tail:
            print(current_node.value)
            current_node = current_node.next
               


sentinel = Sentinel()
# sentinel.add_to_front(7)
# sentinel.add_to_front(5)
sentinel.add_to_back(1, 7, 5)
sentinel.insert_after(5,9)
sentinel.insert_before(9, 8, 6)
print("complete list")
sentinel.print_forward()
removed_list = sentinel.remove_values(8,5,4,3)
print("list after removal")
sentinel.print_forward()
print("removed list")
print(removed_list)


# def add_to_front(self, value):
    #    new_node = Node(value)
    #    # ~^ Boy should know where the line starts and who's next in line
    #    new_node.prev = self.head
    #    new_node.next = self.head.next
       
    #    # ~# MAke the start of the line point to the boy 
    #    self.head.next.prev = new_node
    #    self.head.next = new_node    
    
    # def insert_before(self, existing_value, new_value):
    #     new_node = Node(new_value)
    #     current_node = self.head.next
    #     while current_node is not self.tail:
    #         if current_node.value == existing_value:
    #             new_node.prev = current_node.prev
    #             new_node.next = current_node
    #             current_node.prev.next = new_node
    #             current_node.prev = new_node
    #             return True 
    #     return False
            
    # def insert_after(self, existing_value, new_value):
    #     new_node = Node(new_value)
    #     current_node = self.head.next 
    #     while current_node is not self.tail:
    #         if current_node.value == existing_value:
    #             new_node.prev = current_node
    #             new_node.next = current_node.next
    #             current_node.next.prev = new_node
    #             current_node.next = new_node
    #             return True
    #     return False
    
    # def add_to_back(self, value):
    #     new_node = Node(value)
        
    #     # ~% New Node point to the right places, let the boy reach his arms out to right locations
    #     new_node.next = self.tail
    #     new_node.prev = self.tail.prev
        
    #     # ~% Help the new Node by pointing head and tail to new node,
    #     # ~% head and tail reach out and pull the boy up
    #     # ~% Cannot use the head here because the node is added to the end. 
    #     self.tail.prev.next = new_node
    #     self.tail.prev  = new_node