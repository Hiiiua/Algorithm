class SStack():
    def __init__(self):
        self._elem = []

    def is_empty(self):
        return self._elem == []
    def top(self):
        if self.is_empty():
            raise StackUnderflow('in stack.top()')
        else:
            return self._elem[-1]

    def push(self, elem):
        self._elem.append(elem)

    def pop(self):
        if self.is_empty():
            raise StackUnderflow('in stack.pop()')
        return self._elem.pop()
    def __str__(self): #一个打印方法
        a=[]
        for each in self._elem:
            a.append(str(each))
        a = ','.join(a)
        return a


