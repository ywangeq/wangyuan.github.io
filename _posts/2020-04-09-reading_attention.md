---
layout:     post
title:      Reading
subtitle:   different attention in semantic segmentation
date:       2020-04-07
author:     WY
header-img: img/post-bg-debug.jpg
catalog: true
tags:
    - Reading
    - Semantic Segmentation
    - attention
---

1. cbam 不能加在最后一层
2. senet 还不错
3. ccnet- criss and cross attention ( generate globel feature to improve location)
4. EAnet
5. ExtremeC3Net: Extreme Lightweight Portrait Segmentation Networks using Advanced C3-modules
6. **strip** pooling: Strip Pooling: Rethinking Spatial Pooling for Scene Parsing
    - 和ccnet 非常类似的思想，通过一个带状kernel来genenrate一个long-range的context feature
    - 有趣的是ccnet通过recurrent的思想(n=2)来使current index tensor获得long range relationship from these position，但是strip pooling本身可以替换成平时使用的pooling，这样再stack deep的过程中，其实可以完成long range contextual feature generateion 
7. global based global reasoning network:
    - 通过模拟gcn来构建一个graph 信息流来build global relations between distant regions


