---
layout:     post
title:      Leecode
subtitle:   445 两数相加II(链表相加)
date:       2020-02-22
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - Leecode_medium
    - 链表
---

给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。

 

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶:

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例:

输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出: 7 -> 8 -> 0 -> 7

- 用两个栈存，然后从低到高位相加，只要注意链表重建的时候，插在头部就好。

```
class Solution(object):
    def addTwoNumber(self,l1,l2):
        s1,s2 = [],[]
        while l1:
            s1.append(l1.val)
            l1 = l1.next

        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        dummy = ListNode(-1)
        carry=0
        while s1 or s2 or carry:
            n1,n2 = 0,0
            if s1:
                n1 = s1.pop() 
            if s2:
                n2 = s2.pop()

            count = n1 + n2 + carry
            n = count%10
            node = ListNode(n)
            node.next = dummy.next
            dummy.next = node
            carry = int(count/10)
        return dummy.next
            
```