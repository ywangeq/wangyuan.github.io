---
layout:     post
title:      Leecode
subtitle:   1218 最长定差子序列
date:       2020-02-14
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - python
    - 动态规划

---

给你一个整数数组 arr 和一个整数 difference，请你找出 arr 中所有相邻元素之间的差等于给定 difference 的等差子序列，并返回其中最长的等差子序列的长度。

- 看到这题，其实不难想到coin change
- 我们用dp[i] 表示 i是value， i为某个数是，最长的长度
- 那么dp[i] 很明显就能=dp[i-difference] + 1 if i- different else 1

```
def longSubsque(arr,diff):
    n = len(arr)
    dp={}
    dp[arr[0]]=1
    for i in range(1,n):
        if arr[i] -diff in dp:
            dp[arr[i]] = dp[arr[i]-diff]+1
        else:
            dp[arr[i]]=1
    return max(dp.values())
```