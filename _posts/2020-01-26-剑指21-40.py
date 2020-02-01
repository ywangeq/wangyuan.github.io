---
layout:     post
title:      剑指offer 21-40
subtitle:   旋转列表
date:       2020-01-27
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - 剑指offer
---
#### 22.从上到下打印二叉树
就是我们说的层次遍历
```
def cengci(root):
    res = []

    def help(node,index):
        if not node:
            return 
        if len(res)==index:
            res.append([])
        res[index].append(node.val)
        help(node.left,index+1)
        help(node.right,index+1)
    help(root,0)
    return res
```

#### 23. 后序遍历
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

> 这道题看到的时候卡了一下 所以把思路写下来
- 若任意节点的左子树不空，则左子树上的所有结点的值均小于他的根节点的值
- 右边。。。。。大于
- 任意节点的左右子数也分别是二叉搜索数

- 二叉搜索树的后序遍历规律
- 数组的最后一个元素是整个二叉树的根节点

```
class Solution:
    def verify(self,sequence):
        if not sequence:
            return False
        root = sequence[-1]
        for i in range(len(sequence)):
            if sequence[i]>root:
                break
        for j in range(i,len(sequence)):
            if sequence[i]<root:
                return False

        left = True
        if i>0:
            left=self.verify(sequence[:i]) 
        right = True
        if i<len(sequence)-1:
            right=  self.verify(seq
            [i:-1])
        return right and left
```
怎样后序遍历一个二叉树呢
```
def post(root):
    res = []
    p=root
    stack = []
    while p or stack:
        while p:
            stack.append(p)
            res.append(p.val)
            p=p.right
        p=stack.pop()
        p = p.left
    return res[::-1]

```

#### 24 二叉树中和为某一值的路径
输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
```
class Solution:
    def findpath(self,root,target):
        res =[]
        if not root: return res
        self.target = target
        self.dfs(root,res,[root.val])
        return res
    def dfs(self,root,res,path):
        if not root.left and not root.right and sum(path)==self.target:
            res.append(path)
        if root.left:
            self.dfs(root.left,res,path+[root.left.val])
        if root.right:
            self.dfs(root.right,res,path+[root.right.val])
```

#### 25 复杂链表的复制
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
```
class RandomListNode():
    def __init__(self,x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    def clone(self,pHead):
        if not pHead:
            return None
        newhead = RandomListNode(pHead.label)
        newhead.random = pHead.RandomListNode
        newhead.next = pHead.next
        newhead.next = self.clone(pHead.next)
        return newhead


```

#### 26.二叉搜索树与双向链表
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

```
class Solution:
    def treetolist(root):
        if not root:
            return None
        first,last = None,None
        def help(node):
            nonlocal first,last
            if node:
                help(node.left)
                if last:
                    last.right = node
                    node.left = last
                else:
                    first=node
                last = node
                help(node.right)
        help(root)
        last.right = first
        first.left = last
        return first
```

#### 27.字符串的排列
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

```
class Solution:
    def permutat(self,st):
        res = []
        if len(st)<=1:
            return st
        n = len(st)
        for i in range(n):
            for j in self.permutat(st[:i)+st[i+1:]):
                temp = st[i]+str(j)
                if temp not in res:
                    res.append(temp)
        return res

# 个人比较偏好全排列模板直接上
    def permutate(self,st):
        res = []
        def dfs(s,temp):
            if len(temp)==len(st):
                res.append(temp.copy())
                return
            for i in range(0,len(s)):
                temp.append(s[i])
                dfs(s[:i]+s[i+1:],temp)
                temp.pop()
        dfs(st,[])
        # 在转换一下就好
        return res
```

#### 28.数组中出现次数超过一半的数字
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
```
class Solution:
    # 哈希
    def halfelement(self,nums):
        hash={}
        n =len(nums)
        if n==1:
            return nums[0]
        max_count=n//2
        for i in range(n):
            if nums[i] not in hash:
                hash[num[i]]=1
            else:
                hash[nums[i]]+=1
                if (hash[num[i]]>max_count):
                    return nums[i]
    # 上面的空间复杂为O(n),我们也可以用摩尔投票发优化到O(1)
    def halfelement(self,nums):
        n = len(nums)
        res,count =0,0
        for i in range(n):
            if count==0:
                res=nums[i]
                count+=1
            else: 
                if (nums[i]==res):
                    count+=1
                else:
                    count-=1
        if count>0:
            return res
```

#29.最小的K个数
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

```
#基于快排思想 O(nk)
class Solution:
    def getLeastK(self,arr,k):
        n = len(arr)
        if k>n:
            return []
        for i in range(k):
            for j in range(i+1,n):
                if arr[j]<arr[i]:
                    arr[i],arr[j] = arr[j],arr[i]
        return arr[:k]

#基于最大堆 O(nlogk) python只有最小堆，因此要转换一下
    def getLeastK(self,arr,k):
        import heapq
        max_heapq =[]
        length = len(arr)
        if not arr or k<=0 or k>length:
            return []
        k=k-1
        for i in arr:
            i =-i
            if len(max_heapq)<=k:
                heapq.heappush(max_heapq,i)
            else:
                heapq.heappop(max_heapq,i)

        return map(lambda x:-x, max_heapq)
```

#### 30.连续子数组的最大和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],

输出: 6

```
class Solution:
    def maxl(arr):
        if max(arr)<0: return max(nums)
        go,lo =0,0
        for i in range(len(arr)):
            lo = max(0,lo+nums[i])
            go = max(lo,go)
        return max(lo,go)
```

#### 31.从1到n的整数中1出现的个数
比如，1-13中，1出现6次，分别是1，10，11，12，13

```
def numberofone(n):
    count = 0
    for i in range(1,n+1):
        j =i
        while j:
            if j%10==1:
                count++1
            j/=10
    return count
```