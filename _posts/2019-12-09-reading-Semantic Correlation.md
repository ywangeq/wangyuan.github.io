---
layout:     post
title:      Reading
subtitle:   Semantic Correlation Promoted Shape-Variant Context for Segmentation
date:       2020-01-02
author:     WY
header-img: img/post-bg-debug.jpg
catalog: true
tags:
    - Readiing
    - Semantic Segmentation
    - Context 
---
<head>
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
            skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
            inlineMath: [['$','$']]
            }
        });
    </script>
</head>

## 1. Motivation

考虑到现存的一些语义分割框架在进行上下文捕捉是的视野都是固定的，这就导致了又不不同种类，不同数量，对于这个过程我们仅仅考虑固定的空间相关性会弱化特征。
基于这个想法，作者提出了一个基于语义关系的上下文信息采集框架。
![baseline](https://raw.githubusercontent.com/ywangeq/ywangeq.github.io/master/img/baseline_of_semantic_correlation.jpg)

## 2.basic method
本文本质上是基于固定的视野进一步去判断那里是上下文应该attention的捕捉区域

为了实现这个目标，作者用
- 对于每一个目标像素，都设置了一个Context Window
- 因此利用卷积特性，可以计算Context Window所有其他位置的卷积响应与目标像素处的卷积响应之差，如果差越小，则说明该位置与目标像素越关联，因此一个特征层 会产生H x W 个Context Windows

- 当然作者不是直接对于特征表达空间来做，首先他先通过一个Paired卷积和高斯映射来学习目标像素和周围其他像素的语义相关性

## 个人思考
简单的来说，很类似可行变卷积的变种attention机制（如果有的话），貌似和Pixel-Adaptive Convolution NN 类似，感觉计算量巨大，但是想过确实有了提升，毕竟引入了类似CRF的惩罚项.