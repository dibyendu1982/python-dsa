class Node: 
    def __init__ (self, value):
        self.prev = None
        self.value = value
        self.next = None
        
class DoublyLinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None 
    
    def add_to_back(self, value):
        current_node = Node(value)
        
        if self.head == None:
            self.head = current_node
        else:
            self.tail.next = current_node
            current_node.prev = self.tail
            
        self.tail = current_node
        
    def add_to_front(self, value):
        current_node = Node(value)
        if self.head == None:
            self.head = current_node
        else:
            self.head.previous = current_node
            current_node.next = self.head
            self.head = current_node
            
        
    def remove_value(self, value):
        
        current = self.head
        
        #^ current.next = means do not go to next but assign the next 
        #^ current.next. following next. means go to next object 
        
        while current is not None:            
            ## Act only if the value matches 
            if current.value == value:
                
                ## If there's only 1 node which is head and tail 
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    return True
                
                ## If the node is the first node or the head, in case of head the prev is None  
                if current.prev is None:
                    self.head = self.head.next 
                    self.head.prev = None
                    return True
            
                ## If the node is the last node or the tail, in case of tail the next is None  
                if current.next is None:
                    self.tail = self.tail.prev
                    self.tail.next = None
                    return True
                
                current.prev.next = current.next
                current.next.prev = current.prev
                return True
            current = current.next 
        return False
    
    def print_forward(self): 
        current_node = self.head
        while current_node is not None: 
            print(current_node.value)
            current_node = current_node.next
    
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.add_to_back(5)
doubly_linked_list.add_to_back(7)
doubly_linked_list.add_to_back(1)
doubly_linked_list.add_to_front(9)

doubly_linked_list.print_forward()

# print("remove 1")
# doubly_linked_list.remove_value(1)

# doubly_linked_list.print_forward()