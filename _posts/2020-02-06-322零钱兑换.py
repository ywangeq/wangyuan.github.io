---
layout:     post
title:      Leecode
subtitle:   322 零钱兑换
date:       2020-02-06
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - Leecode_hard
    - 动态规划
    - python
---
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

- 类似跳楼梯
```
def coin(coins,amount):
    dp = [float('inf')*(amount+1)]
    dp[0] = 0
    for coin in coins:
        for x in range(coun,amount+1):
            dp[x] = min(dp[x-coin]+1,dp[x])
    return dp[amount] if dp[amount]!=float('inf') else -1

```