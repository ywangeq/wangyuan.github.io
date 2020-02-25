---
layout:     post
title:      Leecode
subtitle:   424 替换后的最长重复字符
date:       2020-02-25
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - Leecode_medium
    - 滑窗
    - 字符串
---

给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。在执行上述操作后，找到包含重复字母的最长子串的长度。

注意:
字符串长度 和 k 不会超过 104。

示例 1:

输入:
s = "ABAB", k = 2

输出:
4

解释:
用两个'A'替换为两个'B',反之亦然。

- 这个题目可以思考一下，就是最长重复字符就是 dic里面最大的value +k要< 当前的窗口长度

```
def characterRe(s,k):
    from collections import defaultdict
    lookup =defaultdict(int)
    r,l=0,0
    res = 0
    while r<len(s):
        lookup[s[r]]+=1
        while r-l+1 - max(lookup.values())>k:
            lookup[s[l]]-=1
            l+=1

        res = max(res,r-l)
    return res
```