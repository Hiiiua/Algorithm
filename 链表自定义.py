class Node(object):
    def __init__(self, elem, next_ = None):
        self.elem = elem
        self.next = next_

class Llist(object):
    def __init__(self, node = None):
        self._head = node
    def is_empty(self):
        return (self._head == None)
    def length(self):
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count
    def travel(self):
        cur = self._head
        while cur != None:
            print(cur.elem, end =',')
            cur = cur.next
    def add(self, item):
        node = Node(item)
        node.next = self._head
        self._head = node
    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node
    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length():
            self.append(item)
        else:
            node = Node(item)
            pre = self._head
            count = 0
            while count <= (pos -1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node
    def remove(self, item):
        pre = self._head
        while pre.next!=None:
            if pre.next.elem != item:
                pre = pre.next
            else:
                next = pre.next
                pre.next = next.next
                break
        # cur = pre.next
        # if cur.elem == item:
        #     pre.next = None
    def search(self, item):
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
    def try_(self):
        # cur = self._head
        # a = self.elem

        return self._head.next

# l = Llist()
# print(l.is_empty())
# print(l.length())

# l.append(2)
# l.travel()
# print(l.is_empty())
# print(l.length())
#
# l.append(2)
# l.add(8)
# l.append(3)
# l.append(4)
# l.append(5)
# l.append(6)
# l.travel()
# print('\n---------')
# l.insert(-1, 900)
# # l.travel()
# # print('\n---------')
# l.insert(300,100)
# l.insert(2,888)
# l.travel()
# print('\n222222---------')
# l.remove(888)
# l.travel()
# print('\n33333333---------')
# l.remove(100)
# l.travel()
# print(l.search(900))
#
# print(l.try_())