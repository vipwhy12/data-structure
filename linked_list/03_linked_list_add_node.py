
class Node:
  def __init__(self, value):
    self.data = value
    self.next = None
    
class LinkedList:
  def __init__(self, data):
    self.head = Node(data)
    
  def append(self, data):
    cur = self.head
    while cur.next is not None:
      cur = cur.next
    cur.next = Node(data)
  
  def print_all(self):
    cur = self.head
    while cur is not None:
      print(cur.data)
      cur = cur.next
    
  def get_node(self, index):
    cur = self.head
    count = 0
    while count < index:
      cur = cur.next
      count += 1
      
    return cur
  
  def add_node(self, index, value):    
    new_node = Node(value)
    
    if index != 0:
      pre_node = self.get_node(index - 1)
      pre_node_next = pre_node.next
      pre_node.next = new_node
      new_node.next = pre_node_next
    else:
      new_node.next = self.head    
      self.head = new_node
      
    return "index 번째 Node 뒤에 value 를 추가하세요!"
  
  def delete_node(self, index):
    cur = self.head
    count = 0
    
    while cur.next is not None:
      count += 1
      cur = cur.next
    
    #삭제할 노드가 첫번째일때
    if index == 0:
      self.head = self.head.next
      return "노드가 첫번째일때"
    #삭제할 노드가 마지막일때
    elif index == count:
      self.get_node(index-1).next = None
      return "노드가 마지막일때!"
    
    else :
      self.get_node(index -1).next = self.get_node(index + 1) 
      return "노드가 중간에 있을때"
    
    return "실패"

      


linked_list = LinkedList(5)
linked_list.append(12)

linked_list.add_node(0, 3)

linked_list.print_all()

linked_list.delete_node(1)
