---
layout:     post
title:      Reading
subtitle:   Long Tail Problem
date:       2020-04-117
author:     WY
header-img: img/post-bg-debug.jpg
catalog: true
tags:
    - Reading
    - Problem
---

## Long Tail Problen in dataset
  
### 描述
    在一般的分类，检测等相关的数据集中，都会出现少量类别占据了绝大数的样本，也就是我们所说的Head部分，而大量的类别会仅仅占据少量的样本，也就是tail部分。

### 基本现存的解决方法

- Re-sampling: 简单的来说在训练的时候通过控制采样来尽可能控制样本平衡，例如对tail的类别样本进行过采样，对head类别进行欠采样。
- Re-weighting: 一种常用的方法，我们也会在样本分布不均匀的时候来尝试使用他，主要是给不同的类别loss设置不同的权重，对tail类别loss设置更大的权重。
  - Class-BalancedLossBasedonEffectiveNumberofSamples

- learning strategy: 当前有专门为解决少样本问题涉及的学习方法
  - 1. mete learning
  - 2. metric learning
  - 3. transfer learning
  - 4. 也有对训练策略的控制，例如将训练过程分成两步，第一步混合正常训练，第二步 可以对大部分layer进行fix 只对classifier进行balance sample training，或者其他类似的样本平衡策略
      - Equalization Loss for Long-Tailed Object Recognition
      - DECOUPLING REPRESENTATION AND CLASSIFIER FOR LONG-TAILED RECOGNITION


### 为什么要解决长尾问题
    长尾分布这种数据不平衡的问题会导致分类训练难以得到很好的效果，尤其是处于长尾区间的类别而言。现有的一些方法类似类别再平衡策论可以让长尾问题上的准确度表现得更好。 但是这些策论机制虽然显著提升分类器学习，但是同时又会一定程度上损害已学的深度特征的表征能力
