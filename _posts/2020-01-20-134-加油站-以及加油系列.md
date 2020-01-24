---
layout:     post
title:      Leecode-134,871
subtitle:   加油站系列(最低加油次数_hard)
date:       2020-01-20
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - Leecode_medium
    - 数组
    - 动态规划
    - python
    - 加油站
---


在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

- 思路 从0开始 要满足两个判断条件
- 1. 只有汽油数大于消耗的才能成为起点
- 2. 如果从起点开始，累计的汽油数要少于消耗的花费的话，设下一个点为起点
- 3. 把上次起点到被更新的起点处汽油的总消耗记录下来
- 4. 如果从新起点开始，到终点的汽油净入大于过去消耗，则可以为起点

```
def canCompleteCircuit(gas,cost):
    if not gas: return -1
    sp = 0 
    net_gas_from_sp=0
    net_gas_to_sp=0
    for i in range(len(gas)):
        net_gas_from_sp+=gas[i]-cost[i]
        if net_gas_from_sp < 0:
            net_gas_to_sp+=net_gas_from_sp
            sp=i+1
            net_gas_from_sp=0

    return sp if net_gas_from_sp+net_gas_to_sp>=0 else -1
```
**最低加油次数**

汽车从起点出发驶向目的地，该目的地位于出发位置东面 target 英里处。

沿途有加油站，每个 station[i] 代表一个加油站，它位于出发位置东面 station[i][0] 英里处，并且有 station[i][1] 升汽油。

假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。

当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。

为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。

注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。

输入：target = 100, startFuel = 1, stations = [[10,100]]
输出：-1
解释：我们无法抵达目的地，甚至无法到达第一个加油站。

- 思路  动态规划 O(n^2)
- dp[i] 表示加i次能够走的最远距离，需要满足dp[i]>=target的最小i
- 我们依次计算每个dp[i]，初始的就start油就好
- 每多一个加油站，如果之前可以通过加t次油到达这个加油站，现在就可以加t+1次1

```
def minRefuelStops(target, startFuel, stations):
    dp =[startFuel] + [0]*len(stations)
    for i,(location,cap) in enumerate(stations):
        for t in range(i,-1,-1):
            if dp[t]>=location:
                dp[t+1]=max(dp[t+1],dp[t]+cap)   
    for i,d in enumerate(dp):
        if d>=target:
            return i
    return -1
```
