---
layout:     post
title:      Leecode
subtitle:   149 直线上最多的点数
date:       2020-02-06
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - Leecode_hard
    - python
---

给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。
-思路 类似于枚举优化

输入: [[1,1],[2,2],[3,3]]
输出: 3



```
def maxpoint(points):
    n = len(points)
    if n < 3:
        return n
    max_count = 1
    def max_p(i):
        def check_line(i,j,count,duo):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]
            if x1==x2 and y1==y2:
                duo+=1
            elif y1==y2:
                nonlocal hor_line
                hor_line+=1
                count = max(count,hor_line)
            else:
                slop = (x1-x2)/(y1-y2)
                lines[slop] = line.get(slop,1)+1
                count = max(lines[slop],count)
            return count,duo
        lines,hor_line={},1
        count =1
        duo =1
        for j in range(i+1,n):
            count,duo = check_line(i,j,count,duo)
        return count+duo
    for i in range(n-1):
        max_count = max(max_p(i),max_count)
    return max_count
```