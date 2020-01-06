---
layout:     post
title:      Reading
subtitle:   Decoders Matter for Semantic Segmentation
date:       2019-12-22
author:     WY
header-img: img/post-bg-debug.jpg
catalog: true
tags:
    - Readiing
    - Semantic Segmentation
    - decoder
---

> 题外话 博主脑残,看paper喜欢看纸质,然后纸就没了.....

> 今天看的是一个聚焦于语义分割decoder方面的改进 DUpsampling

首先,在此先列举一下之前的常用上采样操作
- 1. 双线性插值
- 2. 反卷积
- 3. 亚像素卷积

对于*1*和*2*大家应该都比较熟悉,主流的语义分割base都是这些实现的

对于*3*来所,博主个人理解是用channel space换空间信息
简单来说,如果我想恢复出一个(h,w,c)通道的输出特征图,那么我之前需要学习一个
(h/2,w/2,4*c)的feature tensor (假设是x2上采样)

### 优缺点


- 双线性插值, 过于简单,无法学习参数
- 反卷积 可以训练,但是因为有补0初始操作,实际上会有影响
- 亚像素卷积插值 个人认为这种信息互换的方式代价有点大,而且无法适用于过高的上采样模块


**DUpsampling**
基本流程可以看图
![img](https://raw.githubusercontent.com/ywangeq/ywangeq.github.io/master/img/Dupsample.png)

本文的技术依据的base是,图片的语义分割标签Y 不是独立同分布的,其中包含的结构信息