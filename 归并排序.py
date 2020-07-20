def devide_conquer(lst):
    left = 0
    right = len(lst)
    mid = (left + right) // 2
    print('mid',mid)
    l_list = lst[left:mid]
    r_list = lst[mid:right]
    print('分治',l_list,r_list)
    if mid <= 1:
        if l_list[0] > r_list[0]:
            a=r_list[0:] + l_list[0:]
            print('返回值a',a)
            return a
        else:
            b = l_list[0:] + r_list[0:]
            print('返回值b',b)
            return b

    devide_conquer(l_list)
    devide_conquer(r_list)


#
# def merge(lst):
#     left = 0
#     right = len(lst)
#     mid = (left+right)/2
#     #分治 排子序列

if __name__=='__main__':
    ans = devide_conquer([1,5,3,5,4,2])
    print(ans)



