---
layout:     post
title:      Leecode元素右边第一个大的元素
subtitle:   739每日温度 503下一个更大元素 II 496 下一个更大元素
date:       2020-02-04
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - Leecode_hard
    - 依图
    - 单调栈
    - python
---

给定一个无序数组，大于所有元素右边第一个大于该元素的
- 用单调栈来索引
- 首先初始化栈，第一个元素索引值0
- 遍历下一个元素，如果栈不为空且当前元素大于栈顶元素，所有当前元素是栈顶元素右边第一个比他大的，弹出来，然后继续

```
def find_max(arr):
    if not arr: return arr
    stack = []
    stack.append(0)
    result = [0 for i in range(len(arr))]
    for i in range(1,len(arr)):
        while stack:
            if arr[i]>arr[stack[-1]]:
                pos = stack.pop()
                result[pos]=arr[i]
            else:
                stack.append(i)
                break
        if not stack:
            stack.append(i)
    while stack:
        pos = stack.pop()
        result[pos]=-1

    return result
```
题目变成了给定的是一个循环数组

- 思路 就是 把数组变成原来的2倍 arr=arr+arr
- 返回 result[:len(arr)]
- 也可以用索引去找，就不用复制一遍数组了
```
def find(arr):
    n = len(nums)
    stack =[]
    res = [0 for i in range(n)]
    for i in range(2*n-1,-1,-1):
        while stack and stack[-1]<=nums[i%n]:
            stack.pop()
        if i < n:
            res[i]=stack[-1] if stack else -1
        stack.append(nums[i%n])
    return res
```

496 下一个更大元素，
给定两个没有重复元素的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出-1。

- 基本思路一样，两个数组的话，对其中一个做个索引就好
```
def next(num1,num2):
    stack,record= [],{}
    for num in num2:
        while stack and stack[-1]<num:
            record[stack.pop()]=num
        stack.append(num)
    for num in stack:
        record[num]=-1
    return [record[num] for num in num1]
```