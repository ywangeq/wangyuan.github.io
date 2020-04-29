---
layout:     post
title:      Reading
subtitle:   个人总结_语义分割之spatial信息
date:       2020-04-17
author:     WY
header-img: img/post-bg-debug.jpg
catalog: true
tags:
    - Reading
    - Semantic Segmentation
    - spatial information
---

## 什么是spatial information
在语义分割中，网络通过encoder_downsample来编码高层级的feature 信息。 但是与此同时，由于这种降采样的操作会严重破坏图片特征的空间信息，导致在最后的细节上会有一些不一样的影响。 
现在大部分工作类似DUC,PSPNet,DeepLab系列等用空洞卷积来保留空间信息，已有Global Convolution Network使用大的kernel size来扩张感知视野。

上面的是基于encoder过程中经常采用的一些方法，而在整个语义分割过程中，一般网络都会用U-shape的网络结构来恢复出certain extent of spatial information. 在这些过程中，会结合deconv，skip connection来refine细节信息，但是U-shape这种结构对于一些丢失的空间信息并不容易恢复

