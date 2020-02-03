---
layout:     post
title:      Leecode
subtitle:   只出现一次的数字i,ii,iii（136，137，260）
date:       2020-01-30
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - Leecode_medium
    - 数组
    - python
    - 位运算
---

136 只出现一次的数字
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
- 线性遍历一遍，存hash
- 或者 可以数学sum
```
class Solution:
    def singleNumber(self,nums):
        hash_table ={}
        for i in nums:
            try: 
                hash_table.pop(i)
            except:
                hash_table[i]=1
        return hash_table.popitem()[0]

# 2*(a+b+c)-(a+b+b+c+c)=a
    def singleNumbers(self,nums):
        return 2*sum(set(nums))-sum(nums)
```

137 只出现一次的数字ii
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
- 位运算
- 或者 数学sum
```
class Solution:
    def singleNumber(self,nums):
        ones,twos =0,0
        for num in nums:
            ones = ones^num&~twos
            twos = twos^num&~ones
        return ones

        # return (3*sum(set(nums))-sum(nums))/2

```

260 只出现一次的数字iii
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]

```
from collections import Counter
class Solution:
    def singleNumber(self,nums):
        hashmap = Counter(nums)
        return [x for x in hashmap if hashmap[x]==1]
    # def singleNumber(self, nums: int) -> List[int]:
    #     # difference between two numbers (x and y) which were seen only once
    #     bitmask = 0
    #     for num in nums:
    #         bitmask ^= num
        
    #     # rightmost 1-bit diff between x and y
    #     diff = bitmask & (-bitmask)
        
    #     x = 0
    #     for num in nums:
    #         # bitmask which will contain only x
    #         if num & diff:
    #             x ^= num
        
    #     return [x, bitmask^x]

```