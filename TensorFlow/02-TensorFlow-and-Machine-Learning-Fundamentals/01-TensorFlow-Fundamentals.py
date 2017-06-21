
# coding: utf-8

# # Introduction to Computation Graphs
# - At the core of every TF program is the **computation graph**.
# - A computation graph is a specific type of directed graph that is used for:
#     - defining, unsurprisingly, computational structure
#     
# ![](https://i.imgur.com/v9cLnlB.jpg)
# 
# The above example can be looked at as a simple equation:
# $$f(1, 2) = 1 + 2 = 3$$
# 
# The fundamental building blocks of TF graphs are:
# - **Nodes:**
#     - Typically drawn as circles, ovals, or boxes
#     - Represent some sort of computation or action being done on or with data in the graph's context.
#     
# - **Edges:**
#     - actual values that get passed to and from Operations
#     - typically drawn as arrows

# # Defining Computation Graphs in TensorFlow
# TensorFlow workflow pattern follows two steps:
# - Define the computation graph
# - Run the graph (with data)

# # Building a TensorFlow Graph
# ![](https://i.imgur.com/ECJX8Iz.jpg)

import tensorflow as tf
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')

a = tf.constant(5, name="input_a")
b = tf.constant(3, name="input_b")
c = tf.multiply(a, b, name="mul_c")
d = tf.add(a, b, name="add_d")
e = tf.add(c, d, name="add_e")
sess = tf.Session()
sess.run(e)
sess.run(c)
output = sess.run(e)

# TensorBoard config
writer = tf.summary.FileWriter('./my_graph', sess.graph)
writer.close()
sess.close()




