#栈调用
import 链表自定义
def StackUnderflow(ValueError):
    pass

class LStack(object):
    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top == None

    def top(self):
        if self.is_empty():
            raise StackUnderflow('in stack.top()')
        else:
            return self._top.elem
    def push(self,elem):
        self._top = 链表自定义.Node(elem,self._top)
    def pop(self):
        if self.is_empty():
            raise StackUnderflow('in stack.pop()')
        else:
            self._top = self._top.next
            return self._top.elem
    def __str__(self):
        '''外部调用print就会打出结果，
        但
        1，返回结果必须是str；
        2，用''.join(list)合并列表必须保证列表中都是字符串。'''
        cur = self._top
        a=[]
        while cur != None:
            a.append(str(cur.elem))
            cur = cur.next
        s = ','.join(a)
        return '打印%s'%s

def main():
    st = LStack()
    st.push(3)
    st.push(5)
    print(st)

if __name__ == '__main__':
    main()