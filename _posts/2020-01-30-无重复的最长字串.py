---
layout:     post
title:      Leecode
subtitle:   3无重复的最长子串
date:       2020-01-30
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - 字符串
    - 滑窗
    - 依图
    - python
---

- 思路 如果滑窗i到j-1之间的字符串没有重复字符，我们只需要检查第j个是否存在于s[i:j]，
- 通过hash优化 可以降低复杂度

```
def long(s):
    dict_ ={}
    max_ = 0
    start=1
    for i in range(len(s)):
        if s[i] in dict_ and start<=dict_[s[i]]:
            start=dict_[s[i]]
        else:
            max_ = max(max_,i-start)
        dict_[s[i]] = i
    return max_

```