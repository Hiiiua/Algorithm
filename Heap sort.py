def heapify(tree, i, n):
    '''对某个节点做heapify
    保证最上面的母节点是最大值
    左子节点位置为2i-1, 右子节点位置为2i+1'''
    if i < n:
        lc = 2*i+1
        rc = 2*i+2
        if lc < n and tree[i]<tree[lc]:
            tree[i], tree[lc] = tree[lc], tree[i]
            heapify(tree, lc, n)
        if rc < n and tree[i]<tree[rc]:
            tree[i], tree[rc] = tree[rc], tree[i]
            heapify(tree, rc, n)
    return tree

# num = [1,2]
# a = heapify(num,0,2)#lc =1 tree[1]=2 n =2 i=0 tree[i] = 3
# print(a)



def build_heap(nums, total_n):
    '''全堆排序
    1，根据node个数判断开始的母节点的位置（2i-1//2)
    2, 从这个节点往上递减heapify'''
    start = (total_n-1)//2 #全堆排序，从倒数第二层开始向上，先求开始点parent
    while start >= 0:
        heapify(nums, start, total_n)
        start -= 1
    return nums
'''heapify之后做堆的排序
1，完成根节点和最后节点的交换
2，断离最后节点
3，对根节点做heapify
4，重复以上'''

def heap_sort(heap, n):
    heap = build_heap(heap, n)
    # print('initial heap = ',heap)
    sort_heap = []
    while n > 0:
        heap[0], heap[n-1] = heap[n-1], heap[0]
        sort_heap.insert(0, heap.pop())
        n -= 1
        heapify(heap,0, n) #顺序很重要
    return sort_heap


nums = [2,5,3,1,10,4]
# a = build_heap(nums, 6)
# print('build_heap=',a)
b = heap_sort(nums, 6)
print('sort_heap=',b)


