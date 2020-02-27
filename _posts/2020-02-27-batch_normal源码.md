---
layout:     post
title:      深度学习
subtitle:   batch normalization前向，后向代码
date:       2020-02-27
author:     WY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - 基本考点
    - 深度学习
---

```
def batchnorm_forward(x,gamma,beta,bn_param):
    mode = bn_param['mode']
    eps = bn_param.get('eps',1e-5)
    momentum = bn_param.get('momentum',0.9)

    N,D = x.shape
    running_mean = bn_param.get('running_mean',np.zeros(D,dtype=x.dtype))
    running_var = bn_param.get('running_var',np.zeros(D,dtype=x.dtype))

    out,cache =None, None
    if mode == 'train':
        sample_mean = np.mean(x,axis=0)
        sample_var = np.var(x,axis=0)
        out_ =(x-sample_mean)/np.sqrt(sample_var+eps)

        running_mean = momentum*running_mean+(1-momentum)*sample_mean
        running_var = momentum*running_var+(1-momentum)*sample_var
        out_ = gamma*out_+beta
        cache = (out_,x,sample_var,sample_var,eps,gamma,beta)
    elif mode=='test':
        scale = gamma/np.sqrt(running_var+eps)
        out = x*scale+(beta-running_mean&scale)

def batchnorm_backward(dout,cache):
    dx,dgamma,dbeta=None,None,NotImplemented
    out_,x,sample_var,sample_mean,eps,gamma,beta=cache
    N = x.shape[0]
    dout_ =gamma*out_
    dvar = np.sum(dout_*(x-sample_mean)*(-0.5)*(sample_var+eps)**(-1.5),axis=0)
    dx_ = 1/np.sqrt(sample_var+eps)
    dvar_ = 2*(x-sampl)/N

    di = dout_*dx_+dvar*dvar_
    dmean = -1*np.sum(di,axis=0)
    dmean_ = np.ones_like(x)/N
    
    dx = di+dmean*dmean_
    dgamma = np.sum(dout*out_,axis=0)
    dbeta = np.sum(dout,axis=0)

    return dx,dgamma,dbeta

```