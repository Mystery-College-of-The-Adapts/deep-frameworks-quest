# Fractional Max-Pooling


## Abstract

ConvNets almost always incorporate some form of spatial pooling.

[**Spatial Pooling**](https://www.quora.com/What-is-spatial-pooling-in-computer-vision) is when local features(such as per-pixel measurements) are grouped together from spatially adjacent pixels. This is typically done to improve robustness to slight deformations of objects.

Max-pooling act on the hidden layers of the network, reducing their size by an integer multiplicative factor **alpha**.

Pros:
- By discarding 75% of your data, you build into the networka degree of invariance with respect to translaations and elastic distortions. 

Cons:
- By simply alternating convolutional layers with max-pooling layers, performance is limited due to the rapid reduction in spatial size


## Main idea of the paper

Using a **fractional version of max-pooling where **alpha** is allowed to take non-integer values

Reference:
<ul>
<li>
Benjamin Graham: “Fractional Max-Pooling”, 2014; <a href='http://arxiv.org/abs/1412.6071'>arXiv:1412.6071</a>.
</li>
</ul>
