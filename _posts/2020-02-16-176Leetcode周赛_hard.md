---
layout:     post
title:      Leecode 周赛
subtitle:   5343 多次求和构造目标数组
date:       2020-02-16
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - Leecode_hard
    - 周赛
    - python
    - 倒退
---

给你一个整数数组 target 。一开始，你有一个数组 A ，它的所有元素均为 1 ，你可以执行以下操作：

令 x 为你数组里所有元素的和
选择满足 0 <= i < target.size 的任意下标 i ，并让 A 数组里下标为 i 处的值为 x 。
你可以重复该过程任意次
如果能从 A 开始构造出目标数组 target ，请你返回 True ，否则返回 False 。

- 倒推就好，，，，早上估计没睡醒

输入：target = [9,3,5]
输出：true
解释：从 [1, 1, 1] 开始
[1, 1, 1], 和为 3 ，选择下标 1
[1, 3, 1], 和为 5， 选择下标 2
[1, 3, 5], 和为 9， 选择下标 0
[9, 3, 5] 完成


```
class Solution:
    def isPossible(self,target):
        if sum(target)==len(target):
            return True
        index = target.index(max(target))
        target[index] = target[index] - sum(target[:index]+target[index+1:])
        if target[index]>=1:
            return self.isPossible(target)
        else:
            return False
```