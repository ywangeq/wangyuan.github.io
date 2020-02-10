---
layout:     post
title:      Leecode
subtitle:   1320  二指输入的的最小距离
date:       2020-02-10
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - python
    - Leecode_hard
    - 记忆化递归
    - 动态规划
---
![img](https://raw.githubusercontent.com/ywangeq/ywangeq.github.io/master/img/leecode_1320.png)
二指输入法定制键盘在 XY 平面上的布局如上图所示，其中每个大写英文字母都位于某个坐标处，例如字母 A 位于坐标 (0,0)，字母 B 位于坐标 (0,1)，字母 P 位于坐标 (2,3) 且字母 Z 位于坐标 (4,1)。

给你一个待输入字符串 word，请你计算并返回在仅使用两根手指的情况下，键入该字符串需要的最小移动总距离。坐标 (x1,y1) 和 (x2,y2) 之间的距离是 |x1 - x2| + |y1 - y2|。 

注意，两根手指的起始位置是零代价的，不计入移动总距离。你的两根手指的起始位置也不必从首字母或者前两个字母开始。

#### 记忆化递归
-不光要记录最小cost，还要记录两个手指打到了哪里
-state:(i,l,r)
- 函数dp(i,l,r):从i开始到n需要的最小cost
- 假设c= word[i],所以我们有两种选择
- dp(i,l,r) =min(dp(i+1,c,l)+cost(l,c)**左手打，右手不动**,dp(i+1,l,c)+cost(r,c))右手打左手不动
- T: O(n*(27^2))
- Space O(n*(27^2))
```
class Solution:
    def mindistance(self,word):
        krest = 26 #悬空
        n = len(word)
        mem = [[[0]*27 for _ in range(27)] for _ in range(n)]   
        # cost cal
        def cost(c1,c2):
            if c1 ==krest:
                return 0
            return abs(c1/6-c2/6)+abs(c1%6-c2%6)
        def dp(i,l,r):
            if i ==n:return 0
            if mem[i][l][r]:
                return mem[i][l][r]
            c = ord(word[i]) - ord('A')
            mem[i][l][r] = min(dp(i+1,l,c)+cost(r,c),dp(i+1,c,r)+cost(l,c))
            return mem[i][l][r]
        return dp(0,26,26)
```
