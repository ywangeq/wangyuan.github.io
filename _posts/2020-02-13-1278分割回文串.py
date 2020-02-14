---
layout:     post
title:      Leecode
subtitle:   1278 分割回文串III 813最大平均值和的分组
date:       2020-02-13
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

我们将给定的数组 A 分成 K 个相邻的非空子数组 ，我们的分数由每个子数组内的平均值的总和构成。计算我们所能得到的最大分数是多少。

注意我们必须使用 A 数组中的每一个数进行分组，并且分数不一定需要是
。
示例:
输入: 
A = [9,1,2,3,9]
K = 3
输出: 20
解释: 
A 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20.
我们也可以把 A 分成[9, 1], [2], [3, 9].
这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.
- 思路类似也是break 点去看


```
def largetave(A,K):
    n = len(A)
    S = [0]*(n+1)
    dp =[[0]*(K+1) for i in range(n+1)]
    for i in range(1,n+1):
        S[i] = S[i-1]+A[i-1]
        dp[i][1] = S[i]/i
    for m in range(2,K+1):# 分多少个
        for i in range(m,n+1):# 至少要有m个
            for j in range(m-1,i):# 要在i上分 那长度至少m-1
                dp[i][m] = max(dp[i][m],dp[j][m-1]+(S[i]-S[j])/(i-j))
    return dp[n][K]

```
