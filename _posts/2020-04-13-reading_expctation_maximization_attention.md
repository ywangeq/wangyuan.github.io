---
layout:     post
title:      Reading
subtitle:   Expectation-Maximization Attention Networks for Semantic Segmentation
date:       2020-04-13
author:     WY
header-img: img/post-bg-debug.jpg
catalog: true
tags:
    - Reading
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

作者如图所示，在拟合阶段通过数据基础的加权和来得到输出，权重通过归一化最终的注意力map得到. 然后将这个EMA方法embed into神经网络中

#### 背景知识
- EM算法
- 高斯混合模型
- 非局部模块
##### EM
$$p(x|y,\theta) = \frac{p(y,x|\theta)}{p(y|\theta)}$$

1 EM算法的目的在于找出潜在变量模型的最大似然解，定义$X={x_1,x_2,...,x_N}$为数据集合，由N个观察样本组成，每个数据点$x_i$有对应的潜在变量$z_i$i. {X,Z}为完整的数据，其似然估计函数为$lnp(X,Z|\theta)$. 其中$\theta$是模型中所有参数的集合。在实际中，$Z$中潜在变量的值是来自于后验分布$p(Z|X,\theta)$。 EM算法通过两步操作来最大化$lnp(X,Z|\theta)$的似然值，即期望(E)操作和最大化M操作。

在期望(E)操作中，作者使用当前的参数$\theta^{old}$,通过$p(X,Z|\theta)$计算Z的后验分布。然后使用计算的后验分布来计算完整数据的似然值$\varTheta(\theta,\theta^{old}$的期望，如公式(1)

$$\varTheta(\theta,\theta^{old})=\sum_{z}{p(Z|X,\theta^{old})}$$

通过最大化M后，会得到修正的参数$\theta^{new}$通过最大化函数决定：

$$\theta^{new}=argmax\varTheta(\theta,\theta^{old})$$

EM迭代多次知道满足拟合条件


##### 高斯混合模型

2 高斯混合模型是EM算法的一个特殊情况。它将数据$x_n$视为高斯分布的线性叠加
$$p(x_n)=\sum_{k=1}z_{nk}N(x_n|u_k,\Sigma_k)$$

均值$u_k$和协方差$\Sigma_k$是第$k$个高斯基，其实还有一个先验$\pi_k$

$$lnp(X,Z|u,\Sigma)=\sum_{n=1}^{N}ln[\sum _{k=1}^{K}z_{nk}N(x_n|u_k,\Sigma_k)]$$

其中 $\Sigma_k{z_nk}$=1,$z_{nk}$可以看作第k个高斯基对观测值$x_n$所承担的责任，对于GMM，期望E操作，$z_{nk}$的期望值根据公式计算：
$$z_{nk}^{new}=\frac{N(x_n|u_{k}^{new},\Sigma_k)}{\Sigma_{j=1}^{K}N(x_n|u_{j}^{new},\Sigma_j)}$$

在最大化M操作中，参数按照下列公式更新

$$u_{k}^{new}=\frac{1}{N_k}\sum_{n=1}^{N}z_{nk}^{new}x_k$$
$$\Sigma_{k}^{new}=\frac{1}{N_k}\sum_{n=1}^{N}z_{nk}^{new}(x_n-u_{k}^{old})(x_n-u_{k}^{old})^{T}$$

其中$N_k = \sum_{n=1}^{N}z_{nk}^{new}$,当GMM你和后，重新估计的$x_{n}^{new}$可以表示为

$$x_n^{new}=\sum_{k=1}^{N}z_{nk}^{new}u_{k}^{new}$$

##### 非局部模块

3. 非局部模块与自注意力机制的功能相似
$$y_i=\frac{1}{C(x_i)}\sum_jf(x_i,x_j)g(x_j)$$

其中f表示一个通用核函数，$C(x)$是一个归一化因子，$x_i$定义了位置i的特征向量，因此此模块可以应用于CNN额特征图，从GMM的角度来看，非局部模块静静是$X$的一个重估基，无需进行期望操作和做大话操作

To do

https://zhuanlan.zhihu.com/p/79298756