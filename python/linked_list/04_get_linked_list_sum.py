# Q. 다음과 같은 두 링크드 리스트를 입력받았을 때, 합산한 값을 반환하시오

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
    
    def to_string(self):
        cur = self.head
        linked_string = ""
        while cur is not None:
            linked_string =  linked_string + str(cur.data)
            cur = cur.next
        return linked_string


def get_linked_list_sum(linked_list_1, linked_list_2):
    # 구현해보세요!
    list_1 = int(LinkedList.to_string(linked_list_1))
    list_2 = int(LinkedList.to_string(linked_list_2))
    return list_1 + list_2


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))