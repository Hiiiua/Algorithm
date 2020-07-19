class Node(object):
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None

class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild == None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild == None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)
    '''广度优先遍历的列表写法：
    1，需要根节点
    2，需queue按顺序遍历
    3，本层和下一层需要分别记录个数，并在当前层建立列表加入result
    4，每一个调用node.left/node.right都给next的计数加一
    5，如果queue有值，则继续pop'''
    def BFS(self):
        q = [self.root]
        res = []
        cur_lv_num = 1
        next_lv_num = 0
        lv=[]

        while q:
            node = q.pop(0)
            lv.append(node.elem)
            cur_lv_num -= 1

            if node.lchild:
                next_lv_num += 1
                q.append(node.lchild)
            if node.rchild:
                next_lv_num += 1
                q.append(node.rchild)

            if cur_lv_num == 0:
                res.append(lv)
                cur_lv_num = next_lv_num
                next_lv_num = 0
                lv =[]
        return res
        '''在之前的基础上直接对于每次遍历计数，计数完成之后初始化一个新的层列表,再快可以用dequeue'''

    def ReBFS(self):
        q = [self.root]
        res = []
        while q:
            lv = []
            level_num = len(q)
            for i in range(level_num):
                node = q.pop(0)
                lv.append(node.elem)
                if node.lchild:
                    q.append(node.lchild)
                if node.rchild:
                    q.append(node.rchild)
            res.append(lv)
        return res

    def breadth_travel(self):
        '''广度遍历'''
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, node):
        if node is None:
            return
        print(node.elem, end=',')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def preRecur(self, node):
        ans = []
        if node is None:
            return
        self.prehelper(node, ans)
        return ans

    def prehelper(self, node, ans):
        if node:
            ans.append(node.elem)
            self.prehelper(node.lchild, ans)
            self.prehelper(node.rchild, ans)
        return ans

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=',')
        self.inorder(node.rchild)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end=',')

if __name__=='__main__':
    tree =Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    # print(tree.root.elem)
    #     # tree.breadth_travel()
    #     # print('\n')
    #     # print(tree.BFS())
    #     # print(tree.ReBFS())
    tree.preorder(tree.root)
    print('\n')
    print(tree.preRecur(tree.root))
    # tree.inorder(tree.root)
    # print('\n')
    # tree.postorder(tree.root)
