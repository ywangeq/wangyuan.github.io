---
layout:     post
title:      Leecode 跳跃游戏
subtitle:   I--V
date:       2020-02-02
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - 跳跃游戏
    - python
---
Leecode-55 跳跃游戏I

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

- 思路 每步走最大的看能到的最远距离是多少

```
class Solution:
    def canJump(self,nums):
        start,end=0,0
        n = len(nums)
        while start<=end and end<n-1:
            end = max(end,nums[start]+start)
            start+=1
        return end>=n-1
```

45. 跳跃游戏 II
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

- 贪心O(n)
https://leetcode-cn.com/problems/jump-game-ii/solution/tan-xin-suan-fa-zhu-xing-jie-shi-python3-by-zhu_sh/

- 定义步数step，和最远达到距离max_b，记录上一次达到边界end
- 遍历数组，（0，n-1):
- 当前能到的最远位置是max(max_b,num[i]+i)
- 看i是否到达了之前记录的边界，如果到了，则更新end，step+1


```
class Solution:
    def jump(self,num):
        step=0
        max_b = 0
        end =0
        for i in range(len(num)-1):
            max_b =max(max_b,num[i]+i)
            if i==end:
                end = max_b
                step+=1
        return step
```

1306. 跳跃游戏 III
这里有一个非负整数数组 arr，你最开始位于该数组的起始下标 start 处。当你位于下标 i 处时，你可以跳到 i + arr[i] 或者 i - arr[i]。

请你判断自己是否能够跳到对应元素值为 0 的 任意 下标处。

注意，不管是什么情况下，你都无法跳到数组之外。

输入：arr = [4,2,3,0,3,1,2], start = 5
输出：true
解释：
到达值为 0 的下标 3 有以下可能方案： 
下标 5 -> 下标 4 -> 下标 1 -> 下标 3 
下标 5 -> 下标 6 -> 下标 4 -> 下标 1 -> 下标 3 

-dfs

```
class Solution:
    def canjump(arr,start):
        n,v = len(arr).{}
        def f(i):
            if arr[i]==0:
                v[i]=True
            elif i not in v:
                v[i]=False
                v[i] = 0<=i-arr[i]<n and f(i-arr[i])  or 0 <= i + arr[i] < n and f(i + arr[i])
            return v[i]
        return f(start)
```
跳跃游戏V
给你一个整数数组 arr 和一个整数 d 。每一步你可以从下标 i 跳到：

i + x ，其中 i + x < arr.length 且 0 < x <= d 。
i - x ，其中 i - x >= 0 且 0 < x <= d 。
除此以外，你从下标 i 跳到下标 j 需要满足：arr[i] > arr[j] 且 arr[i] > arr[k] ，其中下标 k 是所有 i 到 j 之间的数字（更正式的，min(i, j) < k < max(i, j)）。

你可以选择数组的任意下标开始跳跃。请你返回你 最多 可以访问多少个下标。

请注意，任何时刻你都不能跳到数组的外面。
输入：arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
输出：4
解释：你可以从下标 10 出发，然后如上图依次经过 10 --> 8 --> 6 --> 7 。

-dfs 记忆化
```
def maxjump(arr,d):
    dp={}
    def dfs(i):
        if i in dp:
            return dp[i]
        if i<0 or i>len(arr):
            return 0
        res =1
        for i in range(1,d+1):
            if st+i<len(n) and arr[st+i]<arr[st]:
                res = max(res,1+dfs(st+i))
            else:
                break
        for i in range(1,d+1):
            if st-i>=0 and arr[st-i]<arr[st]:
                res = max(res,1+dfs(st-i))
            else:
                break
        dp[i]=res
        return res
    res =1 
    for i in range(len(arr)):
        res = max(res,dfs(i))
    return res
```
