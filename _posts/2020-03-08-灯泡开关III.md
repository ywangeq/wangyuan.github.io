---
layout:     post
title:      Leecode 周赛
subtitle:   灯泡开关III
date:       2020-03-08
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - Leecode_medium
    - 模拟
---

房间中有 n 枚灯泡，编号从 1 到 n，自左向右排成一排。最初，所有的灯都是关着的。

在 k  时刻（ k 的取值范围是 0 到 n - 1），我们打开 light[k] 这个灯。

灯的颜色要想 变成蓝色 就必须同时满足下面两个条件：

灯处于打开状态。
排在它之前（左侧）的所有灯也都处于打开状态。
请返回能够让 所有开着的 灯都 变成蓝色 的时刻 数目 

- 模拟 如果某个时刻灯是全部蓝的，那么意思就是，时刻的sum 和我记录的cnt应该相同

```
def num(light):
    ans,cnt=0,0
    sm =0
    for i in light:
        sm +=i
        cnt +=1
        if sm == (cnt+1)*(cnt)//2:
            ans+=1
    return ans
```