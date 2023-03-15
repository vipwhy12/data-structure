
class Node: 
  def __init__(self, value):
    self.data = value
    self.next = None
    
class LinkedList:
  def __init__(self, value):
    self.head = Node(value)

  def append(self, value):
    cur = self.head
    
    while cur.next is not None:
      cur = cur.next
    
    cur.next = Node(value)
    
  def print_all(self):
    cur = self.head
    while cur is not None:
      print(cur.data)
      cur = cur.next
  
  def get_node(self, index):
    cur = self.head
    tmep_counter = 0
    
    while cur is not None:
      if tmep_counter == index :
        return cur.data
      else :
        tmep_counter += 1
        cur = cur.next
        
    return "Error : Out of Range"
      
linked_list = LinkedList(5)
linked_list.append(12)
linked_list.print_all()
linked_list.get_node(0)