---
layout:     post
title:      Leecode
subtitle:   740 删除与获得点数
date:       2020-02-17
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - python
    - 动态规划
---

给定一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除每个等于 nums[i] - 1 或 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

- 这道题目如果想到转化，就和偷窃房屋那道题一样，如何转化呢
- 出现次数和，然后排序，不拿相邻的

```
def delet(nums):
    if not nums:
        return 0
    l = max(nums)
    gro =[0]*(l+1)
    for i in nums:
        gro[i]+=i

    n = len(gro)
    dp=[0 for i in range(n+1)]
    dp[0],dp[1] = gro[0],max(gro[0],gro[1])
    for i in range(1,n):
        dp[i] =max(dp[i-1],dp[i-2]+gro[i])
    return max(dp[-1],dp[-2])
```