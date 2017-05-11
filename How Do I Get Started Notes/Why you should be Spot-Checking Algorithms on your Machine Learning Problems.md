Spot-checking algorithms is about getting a quick assessment of a bunch of different algorithms on your machine learning problem so that you know what algorithms to focus on and what to discard.

![image alt text](image_0.jpg)

Photo by [withassociates](http://www.flickr.com/photos/withassociates/4385364607/sizes/l/), some rights reserved

In this post you will discover the 3 benefits of spot-checking algorithms, 5 tips for spot-checking on your next problem and the top 10 most popular data mining algorithms that you could use in your suite of algorithms to spot-check.

## Spot-Checking Algorithms

[Spot-checking algorithms](http://machinelearningmastery.com/how-to-evaluate-machine-learning-algorithms/) is a part of the process of applied machine learning. On a new problem, you need to quickly determine which type or class of algorithms is good at picking out the structure in your problem and which are not.

The alternative to spot checking is that you feel overwhelmed by the vast number of algorithms and algorithm types that you could try that you end up trying very few or going with what has worked for you in the past. This results in wasted time and sub-par results.

## Benefits of Spot-Checking Algorithms

There are 3 key benefits of spot-checking algorithms on your machine learning problems:

* Speed: You could spend a lot of time playing around with different algorithms, tuning parameters and thinking about what algorithms will do well on your problem. I have been there and end up testing the same algorithms over and over because I have not been systematic. A single spot-check experiment can save hours, days and even weeks of noodling around.

* Objective: There is a tendency to go with what has worked for you before. We pick our favorite algorithm (or algorithms) and apply them to every problem we see. The power of machine learning is that there are so many different ways to approach a given problem. A spot-check experiment allows you to automatically and objectively discover those algorithms that are the best at picking out the structure in the problem so you can focus your attention.

* Results: Spot-checking algorithms gets you usable results, fast. You may discover a good enough solution in the first spot experiment. Alternatively, you may quickly learn that your dataset does not expose enough structure for any mainstream algorithm to do well. Spot-checking gives you the results you need to decide whether to move forward and optimize a given model or backward and revisit the presentation of the problem.

I think spot checking mainstream algorithms on your problem is a no-brainer first step.

## Tips for Spot-Checking Algorithms

There are some things you can do when you are spot-checking algorithms to ensure you are getting useful and actionable results.

![image alt text](image_1.jpg)

Tips for Spot-Checking Algorithms

Photo by [vintagedept](http://www.flickr.com/photos/vintagedept/6358537847/sizes/l/), some rights reserved.

 

Below are 5 tips to ensure you are getting the most from spot-checking machine learning algorithms on your problem.

* Algorithm Diversity: You want a good mix of algorithm types. I like to include instance based methods (live LVQ and knn), functions and kernels (like neural nets, regression and SVM), rule systems (like Decision Table and RIPPER) and decision trees (like CART, ID3 and C4.5).

* Best Foot Forward: Each algorithm needs to be given a chance to put it’s best foot forward. This does not mean performing a sensitivity analysis on the parameters of each algorithm, but using experiments and heuristics to give each algorithm a fair chance. For example if kNN is in the mix, give it 3 chances with k values of 1, 5 and 7.

* Formal Experiment: Don’t play. There is a huge temptation to try lots of different things in an informal manner, to play around with algorithms on your problem. The idea of spot-checking is to get to the methods that do well on the problem, fast. Design the experiment, run it, then analyze the results. Be methodical. I like to rank algorithms by their statistical significant wins (in pairwise comparisons) and take the top 3-5 as a basis for tuning.

* Jumping-off Point: The best performing algorithms are a starting point not the solution to the problem. The algorithms that are shown to be effective may not be the best algorithms for the job. They are most likely to be useful pointers to types of algorithms that perform well on the problem. For example, if kNN does well, consider follow-up experiments on all the instance based methods and variations of kNN you can think of.

* Build Your Short-list: As you learn and try many different algorithms you can add new algorithms to the suite of algorithms that you use in a spot-check experiment. When I discover a particularly powerful configuration of an algorithm, I like to generalize it and include it in my suite, making my suite more robust for the next problem.

Start building up your suite of algorithms for spot check experiments.

## Top 10 Algorithms

There was a paper published in 2008 titled "[Top 10 algorithms in data mining](http://scholar.google.com/scholar?q=Top+10+algorithms+in+data+mining)“. Who could go past a title like that? It was also turned into a book “[The Top Ten Algorithms in Data Mining](http://www.amazon.com/dp/1420089641?tag=inspiredalgor-20)" and inspired the structure of another “Machine Learning in Action”.

![image alt text](image_2.jpg)

This might be a good paper for you to jump start your short-list of algorithms to spot-check on your next machine learning problem. The top 10 algorithms for data mining listed in the paper were.

* C4.5 This is a decision tree algorithm and includes descendent methods like the famous C5.0 and ID3 algorithms.

* k-means. The go-to clustering algorithm.

* Support Vector Machines. This is really a huge field of study.

* Apriori. This is the go-to algorithm for rule extraction.

* EM. Along with k-means, go-to clustering algorithm.

* PageRank. I rarely touch graph-based problems.

* AdaBoost. This is really the family of boosting ensemble methods.

* knn (k-nearest neighbor). Simple and effective instance-based method.

* Naive Bayes. Simple and robust use of Bayes theorem on data.

* CART (classification and regression trees) another tree-based method.

There is also a [great Quora question on this topic](http://www.quora.com/Machine-Learning/What-are-some-Machine-Learning-algorithms-that-you-should-always-have-a-strong-understanding-of-and-why) that you could mine for ideas of algorithms to try on your problem.

## Resources

* [Top 10 algorithms in data mining](http://scholar.google.com/scholar?q=Top+10+algorithms+in+data+mining) (2008)

* Quora: [What are some Machine Learning algorithms that you should always have a strong understanding of, and why?](http://www.quora.com/Machine-Learning/What-are-some-Machine-Learning-algorithms-that-you-should-always-have-a-strong-understanding-of-and-why)

