---
layout:     post
title:      Reading
subtitle:   Expectation-Maximization Attention Networks for Semantic Segmentation
date:       2020-04-13
author:     WY
header-img: img/post-bg-debug.jpg
catalog: true
tags:
    - Readiing
    - Semantic Segmentation
    - attention
---

## Expectation-Maximization Attention Networks for Semantic Segmentation

#### 关注的问题
现在的语义分割如果想要引入attention map需要依赖前文或者空间的关系进行计算，这样会耗费大量计算

#### Motivation
在这篇文章中，作者将注意力机制转化为最大期望的方法，通过迭代估算出一组更加紧凑的基础数据，然后通过这些基础数据计算注意力图。此外通过这些基础数据进行加权求和，可以得到低秩的结果表示，对噪声有比较好的忍耐性。

简单的来说，作者使用EM算法来先找到一个更为紧密的数据基础集合，而不是将所有像素作为重建的数据基础集合，这样可以降低计算的复杂性。 深入的来说，作者将用于重建的数据基础作为需要在EM算法中学习的参数，将注意力map作为潜在变量。 在此模式上，EM算法的目标是找出(数据基础)的一个最大似然估计

![baseline](https://raw.githubusercontent.com/ywangeq/ywangeq.github.io/master/img/EMA_baseline.png)