---
layout:     post
title:      Leecode
subtitle:   1048 最长字符串链
date:       2020-02-18
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - Leecode_medium
    - 动态规划
---

给出一个单词列表，其中每个单词都由小写英文字母组成。

如果我们可以在 word1 的任何地方添加一个字母使其变成 word2，那么我们认为 word1 是 word2 的前身。例如，"abc" 是 "abac" 的前身。

词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word_1 是 word_2 的前身，word_2 是 word_3 的前身，依此类推。

从给定单词列表 words 中选择单词组成词链，返回词链的最长可能长度。
 
- 思路的话就是动态规划，主要是字符串问题，用字典来存一下就好

```
def maxlink(words):
    words.sort(key=len)
    note = {}
    max_chain = 1
    for w in words:
        if w not in note:
            note[w]=1
        for i in range(len(w)):
            neword = w[i]+w[i:]
            if neword in note:
                note[word] = max(1+note[neword],note[word])
        max_chain = max(max_chain,note[word])
    return max_chain


```