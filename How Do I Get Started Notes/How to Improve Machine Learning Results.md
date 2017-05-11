Having one or two algorithms that perform reasonably well on a problem is a good start, but sometimes you may be incentivised to get the best result you can given the time and resources you have available.

In this post, you will review methods you can use to squeeze out extra performance and improve the results you are getting from machine learning algorithms.

When tuning algorithms you must have a high confidence in the results given by your test harness. This means that you should be using techniques that reduce the variance of the performance measure you are using to assess algorithm runs. I suggest cross validation with a reasonably high number of folds (the exact number of which depends on your dataset).

![image alt text](image_0.jpg)

Tuning Fork

Photo attributed to [eurok](http://www.flickr.com/photos/21025851@N00/2169196138/sizes/l/), some rights reserved

The three strategies you will learn about in this post are:

* Algorithm Tuning

* Ensembles

* Extreme Feature Engineering

## **Algorithm Tuning**

The place to start is to get better results from algorithms that you already know perform well on your problem. You can do this by exploring and fine tuning the configuration for those algorithms.

Machine learning algorithms are parameterized and modification of those parameters can influence the outcome of the learning process. Think of each algorithm parameter as a dimension on a graph with the values of a given parameter as a point along the axis. Three parameters would be a cube of possible configurations for the algorithm, and n-parameters would be an n-dimensional hypercube of possible configurations for the algorithm.

The objective of algorithm tuning is to find the best point or points in that hypercube for your problem. You will be optimizing against your test harness, so again you cannot underestimate the importance of spending the time to build a trusted test harness.

You can approach this search problem by using automated methods that impose a grid on the possibility space and sample where good algorithm configuration might be. You can then use those points in an optimization algorithm to zoom in on the best performance.

You can repeat this process with a number of well performing methods and explore the best you can achieve with each. I strongly advise that the process is automated and reasonably coarse grained as you can quickly reach points of diminishing returns (fractional percentage performance increases) that may not translate to the production system.

The more tuned the parameters of an algorithm, the more biased the algorithm will be to the training data and test harness. This strategy can be effective, but it can also lead to more fragile models that overfit your test harness and don’t perform as well in practice.

## **Ensembles**

Ensemble methods are concerned with combining the results of multiple methods in order to get improved results. Ensemble methods work well when you have multiple "good enough" models that specialize in different parts of the problem.

This may be achieved through many ways. Three ensemble strategies you can explore are:

* **Bagging**: Known more formally as Bootstrapped Aggregation is where the same algorithm has different perspectives on the problem by being trained on different subsets of the training data.

* **Boosting**: Different algorithms are trained on the same training data.

* **Blending**: Known more formally as Stacked Aggregation or Stacking is where a variety of models whose predictions are taken as input to a new model that learns how to combine the predictions into an overall prediction.

It is a good idea to get into ensemble methods after you have exhausted more traditional methods. There are two good reasons for this, they are generally more complex than traditional methods and the traditional methods give you a good base level from which you can improve and draw from to create your ensembles.

![image alt text](image_1.jpg)

Ensemble Learning

Photo attributed to [ancasta1901](http://www.flickr.com/photos/antoniocastagna/8491556471/sizes/l/), some rights reserved

## **Extreme Feature Engineering**

The previous two strategies have looked at getting more from machine learning algorithms. This strategy is about exposing more structure in the problem for the algorithms to learn. In data preparation learned about feature decomposition and aggregation in order to better normalize the data for machine learning algorithms. In this strategy, we push that idea to the limits. I call this strategy extreme feature engineering, when really the term "feature engineering" would suffice.

Think of your data as having complex multi-dimensional structures embedded in it that machine learning algorithms know how to find and exploit to make decisions. You want to best expose those structures to algorithms so that the algorithms can do their best work. A difficulty is that some of those structures may be too dense or too complex for the algorithms to find without help. You may also have some knowledge of such structures from your domain expertise.

Take attributes and decompose them widely into multiple features. Technically, what you are doing with this strategy is reducing dependencies and non-linear relationships into simpler independent linear relationships.

This is might be a foreign idea, so here are three examples:

* **Categorical**: You have a categorical attribute that had the values [red, green blue], you could split that into 3 binary attributes of red, green and blue and give each instance a 1 or 0 value for each.

* **Real**: You have a real valued quantity that has values ranging from 0 to 1000. You could create 10 binary attributes, each representing a bin of values (0-99 for bin 1, 100-199 for bin 2, etc.) and assign each instance a binary value (1/0) for the bins.

I recommend performing this process one step at a time and creating a new test/train dataset for each modification you make and then test algorithms on the dataset. This will start to give you an intuition for attributes and features in the database that are exposing more or less information to the algorithms and the effects on the performance measure. You can use these results to guide further extreme decompositions or aggregations.

## **Summary**

I this post you learned about three strategies for getting improved results from machine learning algorithms on your problem:

* Algorithm Tuning where discovering the best models is treated like a search problem through model parameter space.

* Ensembles where the predictions made by multiple models are combined.

* Extreme Feature Engineering where the attribute decomposition and aggregation seen in data preparation is pushed to the limits.

## **Resources**

If you are looking to dive deeper into this subject, take a look at the resources below.

* [Machine Learning for Hackers](http://www.amazon.com/dp/1449303714?tag=inspiredalgor-20), Chapter 12: Model Comparison

* [Data Mining: Practical Machine Learning Tools and Techniques](http://www.amazon.com/dp/0123748569?tag=inspiredalgor-20), Chapter 7: Transformations: Engineering the input and output

* [The Elements of Statistical Learning: Data Mining, Inference, and Prediction](http://www.amazon.com/dp/0387848576?tag=inspiredalgor-20), Chapter 16: Ensemble Learning

**Update**

For 20 tips and tricks for getting more from your algorithms, see the post:

* [How To Improve Deep Learning Performance](http://machinelearningmastery.com/improve-deep-learning-performance/)

