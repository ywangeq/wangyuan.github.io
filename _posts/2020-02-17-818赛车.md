---
layout:     post
title:      Leecode
subtitle:   818 赛车
date:       2020-02-17
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - python
    - 动态规划
    - 记忆化递归
---

你的赛车起始停留在位置 0，速度为 +1，正行驶在一个无限长的数轴上。（车也可以向负数方向行驶。）

你的车会根据一系列由 A（加速）和 R（倒车）组成的指令进行自动驾驶 。

当车得到指令 "A" 时, 将会做出以下操作： position += speed, speed *= 2。

当车得到指令 "R" 时, 将会做出以下操作：如果当前速度是正数，则将车速调整为 speed = -1 ；否则将车速调整为 speed = 1。  (当前所处位置不变。)

例如，当得到一系列指令 "AAR" 后, 你的车将会走过位置 0->1->3->3，并且速度变化为 1->2->4->-1。

现在给定一个目标位置，请给出能够到达目标位置的最短指令列表的长度。

- best case: t=2^n-1， 那直接n个A 就好
- 其次一种可能， t在[2^(n-2),2^(n-1))
- dp[t] = A^nR(n+1) + dp[left], left=2^n-1-t
- 第二中情况在2^(n-1)-1停下， 就是加速n-1次，掉头走/不走，再掉头
- dp[t] = min(A^(n-1)RA^(m)R(n+m+1)+dp[left]), m in [0,n-1]
- left = t- (2^(n-1))+(2^m-1)
- O(TlogT)
- S(T+logT)
-
```
### mem recursion
def racecar(target):
    from collections import defaultdict
    mem = defaultdict(int)
    def dp(t):
        if mem[t]:
            return mem[t]
        n = math.ceil(math.log2(t+1))
        if 1<<n ==t+1:
            mem[t]=n
            return mem[t]
        mem[t] =n+1 + dp(1<<n-t-1)
        for m in range(n-1):
            cur =(1<<(n-1)-(1<<m))
            mem[t] =min(mem[t],n+1+m+dp(t-cur))
        return mem[t]
    return dp(target)

## dp 表示到达位置x的最短指令长度
class Solution(object):
    def racecar(self, target):
        dp = [0, 1, 4] + [float('inf')] * target
        for t in xrange(3, target + 1):
            k = t.bit_length()
            if t == 2**k - 1:
                dp[t] = k
                continue
            for j in xrange(k - 1):
                dp[t] = min(dp[t], dp[t - 2**(k - 1) + 2**j] + k - 1 + j + 2)
            if 2**k - 1 - t < t:
                dp[t] = min(dp[t], dp[2**k - 1 - t] + k + 1)
        return dp[target]

```