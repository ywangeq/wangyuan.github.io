---
layout:     post
title:      Leecode
subtitle:   1335 最低工作难度
date:       2020-02-20
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - Leecode_hard
    - 动态规划
---

你需要制定一份 d 天的工作计划表。工作之间存在依赖，要想执行第 i 项工作，你必须完成全部 j 项工作（ 0 <= j < i）。

你每天 至少 需要完成一项任务。工作计划的总难度是这 d 天每一天的难度之和，而一天的工作难度是当天应该完成工作的最大难度。

给你一个整数数组 jobDifficulty 和一个整数 d，分别代表工作难度和需要计划的天数。第 i 项工作的难度是 jobDifficulty[i]。

返回整个工作计划的 最小难度 。如果无法制定工作计划，则返回 -1 

输入：jobDifficulty = [6,5,4,3,2,1], d = 2
输出：7
解释：第一天，您可以完成前 5 项工作，总难度 = 6.

- 我们用dp[i][d] 来表示用d天去区分前i个job的最小难度
- dp[0][0] = 0，其他初始化都是inf
- transition dp[i][d] = min{dp[j][d-1]+max(jobs[j+1:i])}  这里 k-1<=j<i
-T:O(n^2 * k)


```
def minDifficulty(jobs,d):
    n = len(jobs)
    if d >n :
        return -1

    dp = [[float('inf')]*(d+1) for i in range(n+1)]
    dp[0][0]=0
    for i in range(1,n+1):
        for k in range(1,d+1):
            md = 0
            for j in range(i-1,k-2,-1):
                md = max(md,jobs[j])
                dp[i][k] = min(dp[i][k],dp[j][k-1]+md])
    return dp[-1][-1]
```