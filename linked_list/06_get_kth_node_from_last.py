
class Node():
  def __init__(self, data):
    self.data = data
    self.next = None
    
    
class LinkedList():
  def __init__(self, value):
    self.head = Node(value)
  
  def append(self, value):
    cur = self.head
    while cur.next is not None:
      cur = cur.next
    cur.next = Node(value)
    
  def get_kth_node_from_last(self, k):
    cur = self.head
    count = 0
    
    while cur.next is not None:
      cur = cur.next
      count += 1
  
    k = count - k
    print(k)
    count = 0
    cur = self.head
    
    while cur is not None:
      if k == count:
        return cur
      else :
        cur = cur.next
        count += 1
    
    return self.head
    # count = count - k
    # cur = self.head
    

        
    return 
  
  
linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!