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

本文的技术依据的base是,图片的语义分割标签Y 不是独立同分布的,其中包含的结构信息,以至于Y可以被压缩而不会造成太大的损失,
也就是我们常说的(信息冗余)

因此作者将Y(groud truth) 压缩到Y'并且为了保证转换过程中损失更少的信息,这里重新设定了一个误差
- 对于原始的tensor(H,W,C) 使用大小为(r,r)的滑窗处理,提取操作来构建通道信息块
- 之后reshape成 1 $\times$ N (N = $r \times r\times C$)
- 然后进行维度的压缩

至于重建误差,建议阅读原文,作者构建这个误差是为了保证在经行变换与反变换之后,前后的信息差异程度京可能的小

### 融合问题
由于该方法在融合的过程中,会导致softmax的局部失效,难以训练,所以引入了自适应温度Softmax


### 主要贡献
本篇文章主要是为了实现一个实时性,但是由于Dupsample本质很类似信息代价交换的过程,只是我们把他压缩了
因此作者重新设计的集成策略,让整个网络的重心转移到Dupsampling(毕竟快),因此使用低级别的下采样特征来进行融合(通俗来讲就是下采样可以只看快,不再过多关注performance)
这种信息解码器会偏好于上采样产生的信息,降低了需要深度cnn提取高维特征图的需要

### 实验结果
一个字 快还好