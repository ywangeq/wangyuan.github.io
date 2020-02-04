---
layout:     post
title:      Leecode
subtitle:   141 判断链表有无环,160 相交链表
date:       2020-02-01
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - 链表
    - Leecode_easy
    - python
--- 
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

```
class Solution:
    def hascycle(self,head):
        p,q = head,head
        while q and p and q.next:
            p = p.next
            q = q.next.next
            if q==p:
                return True
        return False
```

160 找到链表相交的入口
- 拼接链表
```
class Solution:
    def getintersec(self,heada,headb):
        ha,hb = heada,headb
        while ha!=hb:
            ha = ha.next if ha else headb
            hb = hb.next if hb else heada
        return ha
```