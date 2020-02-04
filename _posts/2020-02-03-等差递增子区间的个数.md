---
layout:     post
title:      算法
subtitle:   等差递增子区间的个数
date:       2020-02-03
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - 动态规划
    - 依图
    - python
---

给定一个一维数组，求数组中等差递增子区间的个数。
- 思路:dp[i] 表示套i元素位置的等差数列个数
```
def solution(A):
    n = len(A)
    dp =[0]*n
    if n <3:return 0
    for i in range(2,n):
        if A[i]-A[i-1]==A[i-1]-A[i-2]:
            dp[i] = dp[i-1]+1
    return sum(dp)
```
