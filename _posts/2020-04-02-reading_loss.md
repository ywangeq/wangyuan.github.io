---
layout:     post
title:      Reading
subtitle:   different loss in semantic segmentation
date:       2020-04-02
author:     WY
header-img: img/post-bg-debug.jpg
catalog: true
tags:
    - Readiing
    - Semantic Segmentation
    - Loss
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


#### 本期介绍一些关于语义分割中对于极端样本情况下会使用的loss


### 1. Tversky loss
博主在做小目标检测的时候遇到这个,在了解tversky loss的时候可以看看tversky系数，这是Jaccard系数的一种广义系数。

**1 公式**:  &ensp; 
 $T(A,B)$ = $\frac{|A\bigcap B|}{|A\bigcup B| +\alpha|A=B| + \beta|B-A|}$

其中A为prediction，B为gt，如果了解过Dice loss不难发现，$\alpha=\beta=0.5$的时候，Tversky系数就是Dice系数，
而当设置$\alpha=\beta=1$时，此时tversky系数就是jaccard系数。
|A-B|意味着FP(假阳性)，而|B-A|意味着假阴性

#### 使用感想
    虽然这个loss是为了小目标，或者说对于整体来说很小的目标提出来的一个loss，但是在使用的过程中，一但目标和input超过了一个极限比例，loss很难是网络得到一个好的结果。一般我是先crossentroy 来train，等finetuning的时候再改变loss优化