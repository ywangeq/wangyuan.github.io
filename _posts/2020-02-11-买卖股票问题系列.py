---
layout:     post
title:      Leecode 股票买卖问题
subtitle:   121 最佳时期 122 不限制次数 123. 买卖股票的最佳时机 III 限制次数2 188. 买卖股票的最佳时机 限制次数k IV 309 买卖 有cd 714 有手续费
date:       2020-02-11
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - python
    - 动态规划
---
121 股票买卖 只能交易一次
股票最大利润是一个很好的问题，有各种拓展，类似限制次数，买卖冷冻期等

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。

- 很容易想到dp[i][0] 表示第i天手里没有股票的最大利润， dp[i][1]表示有，状态转移看代码

```
class Solution(object):
    def maxProfit(self,prices):
        dp = [[0 for i in range(2)] for _ in range(len(prices)+1)]
        dp[0][0]=0
        dp[0][1] = float('-inf')
        for i in range(1,len(prices)+1):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i-1])
            dp[i][1] = max(dp[i-1][1],-prices[i-1])
        return dp[-1][0]
```

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
- 注意该题不限制交易次数，也就是说贪心 每次都赚就可以了

```
# 贪心
def maxProfit(prices):
    res = 0
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            res +=(prices[i]-prices[i-1])
    return res
# 动态规划
# dp[i] 表示第i天的最大利润
def maxProfit(prices):
    if not prices:
        return 0
    dp = [0]*(len(prices))
    for i in range(1,len(prices)):
        if prices[i]>prices[i-1]:
            dp[i] = dp[i-1]+(prices[i]-prices[i-1])
        else:
            dp[i] = dp[i-1]


```

123. 买卖股票的最佳时机 III

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

- 这边我们先总结一下这类题型的基本框架，也是这条题目的基本写法
- dp[i][k][0] (i天还能交易k次没有股票的最大收益)
- dp[i][k][0] = max(dp[i-1][k][0],dp[i-1][k][1]+price[i])
- dp[i][k][1] = max(dp[i-1][k][1],dp[i-1][k-1][0]-price[i])
- 这边 我们就要注意了k，由于k存在，所以我们需要穷举k的所有状态

```
def maxProfit(self,price):
    # 这条题目k=2 其实可以压缩 不过算了
    k =2
    n = len(price)
    if not price:
        return 0
    dp = [[[0]*2 for _ in range(k+1)]for i in range(n)]
    #初始化
    for i in range(k+1):
        dp[0][i][1] = -price[0]
    for i in range(1,n):
        for K in range(1,k+1):
           dp[i][j][0] = max(dp[i-1][j][0],dp[i-1][j][1]+prices[i])
           dp[i][j][1] = max(dp[i-1][j][1],dp[i-1][j-1][0]-prices[i]) 
    return dp[n-1][k][0]
```

给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

- 这题模板可以直接解决 但是 空间复杂度太高，可以优化，当k大于最多执行次数是，可以被压缩为无数次

```
def maxProfit(k,prices):
    if not prices:
        return 0
    n = len(prices)
    max_k = n//2
    if k>=max_k:
        res = 0
        for i in range(n-1):
            res += max(0,prices[i+1]-prices[i])
        return res
    else:
        max_k = k
    dp = [[[0]*2 for _ in range(k+1)] for _ in range(n)]
    for i in range(max_k+1):
        dp[0][i][1] = -prices[0]   
    for i in range(1, n):
            for k in range(1, max_k+1):
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])
        return dp[n-1][max_k][0]
```

309 最佳买卖股票时机含冷冻期
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
- dp[i][0] =max(dp[i-1][0],dp[i-1][1]+price[i])  今天没有股票要么昨天也没有，昨天有，今天卖了
- dp[i][1] = max(dp[i-1][1],dp[i-2][0]+price[i])  今天有股票，要么昨天就有，要么前天也没有，今天不是冷冻今天买
```
def maxProfit(prices):
    n = len(prices)
    if n<=1:
        return 0
    dp = [[0]*2 for _ in range(n+1)]
    dp[0][0],dp[0][1] =0,float('-inf')
    for i in range(1,n+1):
        dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i-1])
        dp[i][1] = max(dp[i-1][1],dp[i-2][0]-prices[i-1])
    return dp[-1][0]

```