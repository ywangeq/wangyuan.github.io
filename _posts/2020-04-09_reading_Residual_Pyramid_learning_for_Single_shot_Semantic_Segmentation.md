---
layout:     post
title:      Reading
subtitle:   Residual Pyramid Learning for Single-Shot Semantic Segmentation
date:       2020-04-02
author:     WY
header-img: img/post-bg-debug.jpg
catalog: true
tags:
    - Readiing
    - Semantic Segmentation
---

#### 关注的问题
本文发现如今的大部分语义分割的网络都是基于encoder和decoder来恢复pixel信息的，然后通过encoder构建以一种inverted pyramid network的特征提取，但是由于这种encode的方式，不可避免的丢失很多信息，所以在decoder的过程中需要额外的资源开销来恢复细节。有些做法为了在效果和效率之间达到一个平衡，关注在decode的结构上，类似取消deconv 直接插值回去。 也有一些skip了一些low level 特征来作为补充，但是会让decoder结构变得固定