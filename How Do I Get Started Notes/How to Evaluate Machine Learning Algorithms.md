Once you have [defined your problem](http://machinelearningmastery.com/how-to-define-your-machine-learning-problem/) and [prepared your data](http://machinelearningmastery.com/how-to-prepare-data-for-machine-learning/) you need to apply machine learning algorithms to the data in order to solve your problem. You can spend a lot of time choosing, running and tuning algorithms. You want to make sure you are using your time effectively to get closer to your goal.

In this post you will step through a process to rapidly test algorithms and discover whether or not there is structure in your problem for the algorithms to learn and which algorithms are effective.

![image alt text](image_0.jpg)

Test Harness

Photo attributed to [NASA Webb Telescope](http://www.flickr.com/photos/nasawebbtelescope/8721550190/sizes/l/), some rights reserved

## Test Harness

You need to define a test harness. The test harness is the data you will train and test an algorithm against and the performance measure you will use to assess its performance. It is important to define your test harness well so that you can focus on evaluating different algorithms and thinking deeply about the problem.

The goal of the test harness is to be able to quickly and consistently test algorithms against a fair representation of the problem being solved. The outcome of testing multiple algorithms against the harness will be an estimation of how a variety of algorithms perform on the problem against a chosen performance measure. You will know which algorithms might be worth tuning on the problem and which should not be considered further.

The results will also give you an indication of how learnable the problem is. If a variety of different learning algorithms university perform poorly on the problem, it may be an indication of a lack of structure available to algorithms to learn. This may be because there actually is a lack of learnable structure in the selected data or it may be an opportunity to try different transforms to expose the structure to the learning algorithms.

### Performance Measure

The performance measure is the way you want to evaluate a solution to the problem. It is the measurement you will make of the predictions made by a trained model on the test dataset.

Performance measures are typically specialized to the class of problem you are working with, for example classification, regression, and clustering. Many standard performance measures will give you a score that is meaningful to your problem domain. For example, classification accuracy for classification (total correct correction divided by the total predictions made multiple by 100 to turn it into a percentage).

You may also want a more detailed breakdown of performance, for example, you may want to know about the false positives on a spam classification problem because good email will be marked as spam and cannot be read.

There are many standard performance measures to choose from. You rarely have to devise a new performance measure yourself as you can generally find or adapt one that best captures the requirements of the problem being solved. Look to similar problems you uncovered and at the performance measures used to see if any can be adopted.

### Test and Train Datasets

From the transformed data, you will need to select a test set and a training set. An algorithm will be trained on the training dataset and will be evaluated against the test set. This may be as simple as selecting a random split of data (66% for training, 34% for testing) or may involve more complicated sampling methods.

A trained model is not exposed to the test dataset during training and any predictions made on that dataset are designed to be indicative of the performance of the model in general. As such you want to make sure the selection of your datasets are representative of the problem you are solving.

### Cross Validation

A more sophisticated approach than using a test and train dataset is to use the entire transformed dataset to train and test a given algorithm. A method you could use in your test harness that does this is called cross validation.

It first involves separating the dataset into a number of equally sized groups of instances (called folds). The model is then trained on all folds exception one that was left out and the prepared model is tested on that left out fold. The process is repeated so that each fold get’s an opportunity at being left out and acting as the test dataset. Finally, the performance measures are averaged across all folds to estimate the capability of the algorithm on the problem.

For example, a 3-fold cross validation would involve training and testing a model 3 times:

* #1: Train on folds 1+2, test on fold 3

* #2: Train on folds 1+3, test on fold 2

* #3: Train on folds 2+3, test on fold 1

The number of folds can vary based on the size of your dataset, but common numbers are 3, 5, 7 and 10 folds. The goal is to have a good balance between the size and representation of data in your train and test sets.

When you’re just getting started, stick with a simple split of train and test data (such as 66%/34%) and move onto cross validation once you have more confidence.

## Testing Algorithms

When starting with a problem and having defined a test harness you are happy with, it is time to spot check a variety of machine learning algorithms. Spot checking is useful because it allows you to very quickly see if there is any learnable structures in the data and estimate which algorithms may be effective on the problem.

Spot checking also helps you work out any issues in your test harness and make sure the chosen performance measure is appropriate.

The best first algorithm to spot check is a random. Plug in a random number generator to generate predictions in the appropriate range. This should be the worst "algorithm result" you achieve and will be the measure by which all improvements can be assessed.

Select 5-10 standard algorithms that are appropriate for your problem and run them through your test harness. By standard algorithms, I mean popular methods no special configurations. Appropriate for your problem means that the algorithms can handle regression if you have a regression problem.

Choose methods from the [groupings of algorithms](http://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/) we have already reviewed. I like to include a diverse mix and have 10-20 different algorithms drawn from a diverse range of algorithm types. Depending on the library I am using, I may spot check up to a 50+ popular methods to flush out promising methods quickly.

If you want to run a lot of methods, you may have to revisit data preparation and reduce the size of your selected dataset. This may reduce your confidence in the results, so test with various data set sizes. You may like to use a smaller size dataset for algorithm spot checking and a fuller dataset for algorithm tuning.

## Summary

In this post you learned about the importance of setting up a trust worthy test harness that involves the selection of test and training datasets and a performance measure meaningful to your problem.

You also learned about the strategy of spot checking a diverse range of machine learning algorithms on your problem using your test harness. You discovered that this strategy can quickly highlight whether there is learnable structure in your dataset (and if not you can revisit data preparation) and which algorithms perform generally well on the problem (that may be candidates for further investigation and tuning).

## Resources

If you are looking to dive deeper into this topic, you can learn more from the resources below.

* [Data Mining: Practical Machine Learning Tools and Techniques](http://www.amazon.com/dp/0123748569?tag=inspiredalgor-20) (affiliate link), Chapter 5: Credibility: Evaluating what’s been learned

* [Machine Learning: Neural and Statistical Classification](http://www.amazon.com/dp/8188689734?tag=inspiredalgor-20) (affiliate link), Chapter 7: Methods for Comparison

