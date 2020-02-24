---
layout:     post
title:      Leecode
subtitle:   977 有序数组的平方
date:       2020-02-23
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - Leecode_medium
    - 双指针
---

给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。


示例 1：

输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]

- 这道题之所以整理，是因为有很多乱七八糟的方法，但是最快的是双指针

```
def sorted(A):
    i = 0
        while i<len(A) and A[i]<0:
            i+=1
       
        j=i-1
        res=[]
        while i<len(A) and j>=0:
            if A[i]**2<A[j]**2:
                res.append(A[i]**2)
                i+=1
            else:
                res.append(A[j]**2)
                j-=1
        while i <len(A):
            res.append(A[i]**2)
            i+=1
        while j>=0:
            res.append(A[j]**2)
            j-=1
        return res
```