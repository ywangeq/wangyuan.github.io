---
layout:     post
title:      Leecode
subtitle:   把数字翻译成字符串
date:       2020-03-19
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - 动态规划
---

给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

- 根据题目发现 可能性之和一位或者两位有关

```
class Solution:
    def translateNum(self, num: int) -> int:
        # s,a,b = str(num),1,1
        # for i in range(1,len(s)):
        #     a,b = b,(a+b) if 10 <= int(s[i-1:i+1])<=25 else b
        # return b 

        s = str(num)
        dp = [1] *(len(s)+1)
        for i in range(1,len(s)+1):
            if 10<= int(s[i-1:i+1])<=25:
                dp[i] = dp[i-1]+dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[-1]

```