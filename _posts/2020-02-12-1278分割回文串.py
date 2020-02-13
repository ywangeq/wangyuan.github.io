---
layout:     post
title:      Leecode
subtitle:   1278 分割回文串III
date:       2020-02-12
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - python
    - 动态规划
    - 字符串
    - 记忆化递归
---
给你一个由小写字母组成的字符串 s，和一个整数 k。

请你按下面的要求分割字符串：

首先，你可以将 s 中的部分字符修改为其他的小写英文字母。
接着，你需要把 s 分割成 k 个非空且不相交的子串，并且每个子串都是回文串。
请返回以这种方式分割字符串所需修改的最少字符数。

- 这条题目先不看分分割，很明显有另一个cost的先要写
- cost的话可以看成一个动态规划，
- cost[i][j] = cost[i+1][j-1] +(s[i]!=s[j]), 很经典的一个动态
- 让后我们再来看分割，其实不难发现也是一个dp
- dp[i][k] 表示前i个字符分割k次的最小，那么状态转移就是
- dp[i][k] = min(dp[i][k],dp[j][k-1]+cost[j+1][i]])   j在[0,i)

```
def partition(s,k):
    n = len(k)
    cost = [[0]*n for i in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if s[i]!=s[j]:
                cost[i][j] = cost[i+1][j-1] +1
            else:
                cost[i][j] = cost[i+1][j-1]

    dp = [[0]*(k+1) for i in range(n)]
    for i in range(n):
        dp[i][1] = cost[0][i]
        for m in range(2,k+1):
            for j in range(i):
                dp[i][m] = min(dp[i][m],dp[j][m-1]+cost[j+1][i])
    return dp[-1][-1]  
```

#### 如果想不到 没关系 我们还有记忆化递归
```
import functools
class Solution:
    def partition(self,s,k):
        @functools.lru_cache(None)
        def cost(i,j):
            if i >=j:
                return 0
            return cost(i+1,j-1) +(1 if s[i]!=s[j] else 0)
        @functools.lru_cache(None)
        def dp(i,k):
            if k==1: return cost(0,i)
            if k==i+1: return 0
            if k> i+1: return float('inf')
            return min([dp[j,k-1]+cost(j+1,i) for j in range(i)])
        return dp(len(s)-1,k)
```