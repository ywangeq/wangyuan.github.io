---
layout:     post
title:      Leecode180周赛
subtitle:   5179. 将二叉搜索树变平衡 5359. 最大的团队表现值
date:       2020-03-15
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - 平衡二叉树
    - 单调递增
---

5179 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。

如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。

如果有多种构造方法，请你返回任意一种。

- 这道题目我比赛取巧了，先中序得到排序数组，然后生成平衡

```
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        res=[]
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        def generate(arr,start,end):
           
            if start>end:
                return None
            mid = int((start+end)/2)
            node = TreeNode(arr[mid])
            node.left = generate(arr,start,mid-1)
            node.right = generate(arr,mid+1,end)
            return node
        return generate(res,0,len(res)-1)
        
```

5359 公司有编号为 1 到 n 的 n 个工程师，给你两个数组 speed 和 efficiency ，其中 speed[i] 和 efficiency[i] 分别代表第 i 位工程师的速度和效率。请你返回由最多 k 个工程师组成的 ​​​​​​最大团队表现值 ，由于答案可能很大，请你返回结果对 10^9 + 7 取余后的结果。

团队表现值 的定义为：一个团队中「所有工程师速度的和」乘以他们「效率值中的最小值」。

 - 这一题思路因为要找min的效率，所以先对效率进行排序，接下来就是一个遍历比较，当然需要优化，比赛的时候没优化。。。。。

```
def maxper(speed,efficiency,k)；
     grid=[]
        for i in range(n):
            
            grid.append([speed[i],efficiency[i]])
        from heapq import heappush,heappop

        grid = sorted(grid,key=lambda x: x[1])

        ans=0
        sum_=0
        q =[]
        for x,y in grid:
            if len(q)==k:
                b=heappop(q)
                sum_-=b
            else:
                b=0
            heappush(q,max(b,x))
            sum_+=max(b,x)
            ans = max(ans,y*sum_)
        return ans
            
```