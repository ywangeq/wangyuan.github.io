---
layout:     post
title:      剑指offer 1-10
subtitle:   旋转列表
date:       2020-01-26
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - 剑指offer
---

> 复习一下剑指offer的一些题目，大概66题，具体题解不会解释太多，不用过多观看，只是给自己的一个记录。

### 1 二维数组中的查找
在一个二维数组中，每一行都按照从左到右递增，每一列都按照从上到下递增，给定一个target看是否在数组中

```
class Solution:
    def find(self,target,matrix):
        row,col = len(matrix)-1,0
        while row>=0 and col<len(matrix[0]):
            if target==matrix[row][col]:
                return True
            elif target<matrix[row][col]:
                row-=1
            else:
                col+=1
        return False
```

#### 2.替换空格
实现一个函数，将一个字符串中的每个空格替换成%20。
例如 We are Happy
输出 We%20are%20Happy

```
def replace(s):
    res = ''
    for j in s:
        if j ==' '
            res = res+'%20'
        else：
            res = res+j
```

#### 3 从头到尾打印链表
输入一个链表，按链表值从头到尾的顺序返回一个ArrayList

```
class Solution:
    def printlist(self,listNode):
        if not listNode:
            return []
        res = []
        while listNode:
            res.append(listNode.val)
            listNode=listNode.next
        res.reverse()
        return res

```

#### 4 重建二叉树
通过二叉树的前序遍历和中序遍历，重建该二叉树

```
def reconbitree(pre,tin):
    if not pre:
        return None
    root = TreeNode(pre[0])
    index = tin.index(pre[0])
    root.left = reconbitree(pre[1:index+1],tin[:n])
    root.right = reconbitree(pre[index+1:],tin[index+1:])
    return root

```


#### 5用两个栈实现一个队列
用两个栈来实现一个队列完成push和pop

```
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self,val):
        self.stack1.append(val)
    def pop(self):
        if self.stack2==[]:
            if self.stack1==[]:
                return None
            else:
                for i in range(len(self.stack1)):
                    self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        
```
(转换)两个队列实现一个栈
```
class Solution:
    def __init__(self):
        self.q1=[]
        self.q2=[]
    def push(self,node):
        self.q1.append(node)
    def pop(self):
        if len(self.q1)==0:
            return None
        while len(self.q1)!=1:
            self.q2.append(self.q1.pop(0))
        self.q1,self.q2 = self.q1,self.q2
        return self.q2.pop()
```

#### 6 旋转数组中的最小数字
一个递增排序的数组做了一次旋转，给你旋转后的数组，找到最小元素。输入{3,4,5,1,2}输出1。
```
def minfind(arr):
    if not arr:
        return None

    r = len(arr)-1
    l = 0
    while l <r:
        mid = (l+r)//2
        if arr[mid]>arr[r]:
            l=mid+1
        else:
            r=mid

    return arr[l]
```
如果有重复的
```
def find(arr):
    l,r = 0 , len(arr)-1
    while l<r:
        mid = (l+r)//2
        if arr[mid]>arr[r]:
            l = mid+1
        elif arr[mid]<arr[r]:
            r = mid
        else:
            r=r-1
    return arr[l]
```

#### 7 斐波那契数列
要求输入一个整数n, 请你输出数列的第n项
```
def F(n):
    cache ={}
    def cal(N):
        if N in cache:
            return cache[N]
        if N <2:
            return N
        else:
            result = cal(N-1)+cal(N-2)
        cache[N]=result
        return result
    return cal(n)    
```