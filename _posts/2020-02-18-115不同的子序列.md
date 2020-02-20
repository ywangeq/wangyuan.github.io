---
layout:     post
title:      Leecode
subtitle:   115 不同的子序列
date:       2020-02-18
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - Leecode_medium
    - 动态规划
---
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

示例 1:

输入: S = "rabbbit", T = "rabbit"
输出: 3
解释:

如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

- dp[i][j]表示前s[:i] 和 t[:j]有多少个相同的子序列
- 如果s[i] =t[j], 说明当前状态没影响，所以看s[i]加不加入匹配从而有两个状态
- dp[i][j] = dp[i-1][j-1] +dp[i-1][j]  前一个表示match  后一个表示跳过 


```
def numDista(s,t):
    n,m = len(s),len(t)
    dp = [[0]*(m+1) for i in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        dp[i][0]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1]==t[j-1]:
                dp[i][j] =dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]
```