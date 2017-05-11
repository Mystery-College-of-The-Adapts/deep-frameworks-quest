## **_The Systematic Process For Working Through _**

## **_Predictive Modeling Problems That _**

## **_Delivers Above Average Results_**

Over time, working on applied machine learning problems you develop a pattern or process for quickly getting to good robust results.

Once developed, you can use this process again and again on project after project. The more robust and developed your process, the faster you can get to reliable results.

The skeleton of my process for working a machine learning problem.

You can use this as a starting point or template on your next project.

## **5-Step Systematic Process**

I liked to use a 5-step process:

1. Define the Problem

2. Prepare Data

3. Spot Check Algorithms

4. Improve Results

5. Present Results

There is a lot of flexibility in this process. For example, the "prepare data" step is typically broken down into analyze data (summarize and graph) and prepare data (prepare samples for experiments). The “Spot Checks” step may involve multiple formal experiments.

It’s a great big production line that I try to move through in a linear manner. The great thing in using automated tools is that you can go back a few steps (say from "Improve Results" back to “Prepare Data”) and insert a new transform of the dataset and re-run experiments in the intervening steps to see what interesting results come out and how they compare to the experiments you executed before.



The process I use has been adapted from the standard data mining process of knowledge discovery in databases (or KDD), See the post [What is Data Mining and KDD ](http://machinelearningmastery.com/what-is-data-mining-and-kdd/)for more details.

## **1. Define the Problem**

I like to use a three step process to define the problem. I like to move quickly and I use this mini process to see the problem from a few different perspectives very quickly:

* **Step 1: What is the problem?** Describe the problem informally and formally and list assumptions and similar problems.

* **Step 2: Why does the problem need to be solved?** List your motivation for solving the problem, the benefits a solution provides and how the solution will be used.

* **Step 3: How would I solve the problem?** Describe how the problem would be solved manually to flush domain knowledge.

You can learn more about this process in the post:

* [How to Define Your Machine Learning Problem](http://machinelearningmastery.com/how-to-define-your-machine-learning-problem/)

## **2. Prepare Data**

I preface data preparation with a data analysis phase that involves summarizing the attributes and visualizing them using scatter plots and histograms. I also like to describe in detail each attribute and relationships between attributes. This grunt work forces me to think about the data in the context of the problem before it is lost to the algorithms

The actual data preparation process is three step as follows:

* **Step 1: Data Selection**: Consider what data is available, what data is missing and what data can be removed.

* **Step 2: Data Preprocessing**: Organize your selected data by formatting, cleaning and sampling from it.

* **Step 3: Data Transformation**: Transform preprocessed data ready for machine learning by engineering features using scaling, attribute decomposition and attribute aggregation.

You can learn more about this process for preparing data in the post:

* [How to Prepare Data For Machine Learning](http://machinelearningmastery.com/how-to-prepare-data-for-machine-learning/)

## **3. Spot Check Algorithms**

I use 10 fold cross validation in my test harnesses by default. All experiments (algorithm and dataset combinations) are repeated 10 times and the mean and standard deviation of the accuracy is collected and reported. I also use statistical significance tests to flush out meaningful results from noise. Box-plots are very useful for summarizing the distribution of accuracy results for each algorithm and dataset pair.

I spot check algorithms, which means loading up a bunch of standard machine learning algorithms into my test harness and performing a formal experiment. I typically run 10-20 standard algorithms from all the [major algorithm families](http://machinelearningmastery.com/a-tour-of-machine-learning-algorithms/) across all the transformed and scaled versions of the dataset I have prepared.

The goal of spot checking is to flush out the types of algorithms and dataset combinations that are good at picking out the structure of the problem so that they can be studied in more detail with focused experiments.

More focused experiments with well-performing families of algorithms may be performed in this step, but algorithm tuning is left for the next step.

You can discover more about defining your test harness in the post:

* [How to Evaluate Machine Learning Algorithms](http://machinelearningmastery.com/how-to-evaluate-machine-learning-algorithms/)

You can discover the importance of spot checking algorithms in the post:

* [Why you should be Spot-Checking Algorithms on your Machine Learning Problems](http://machinelearningmastery.com/why-you-should-be-spot-checking-algorithms-on-your-machine-learning-problems/)

## **4. Improve Results**

After spot checking, it’s time to squeeze out the best result from the rig. I do this by running an automated sensitivity analysis on the parameters of the top performing algorithms. I also design and run experiments using standard ensemble methods of the top performing algorithms. I put a lot of time into thinking about how to get more out of the dataset or of the family of algorithms that have been shown to perform well.

Again, statistical significance of results is critical here. It is so easy to focus on the methods and play with algorithm configurations. The results are only meaningful if they are significant and all configuration are already thought out and the experiments are executed in batch. I also like to maintain my own personal leaderboard of top results on a problem.

In summary, the process of improving results involves:

* **Algorithm Tuning**: where discovering the best models is treated like a search problem through model parameter space.

* **Ensemble Methods**: where the predictions made by multiple models are combined.

* **Extreme Feature Engineering**: where the attribute decomposition and aggregation seen in data preparation is pushed to the limits.

You can discover more about this process in the post:

* [How to Improve Machine Learning Results](http://machinelearningmastery.com/how-to-improve-machine-learning-results/)

## **5. Present Results**

The results of a complex machine learning problem are meaningless unless they are put to work. This typically means a presentation to stakeholders. Even if it is a competition or a problem I am working on for myself, I still go through the process of presenting the results. It’s a good practice and gives me clear learnings I can build upon next time.

The template I use to present results is below and may take the form of a text document, formal report or presentation slides.

* **Context (Why)**: Define the environment in which the problem exists and set up the motivation for the research question.

* **Problem (Question)**: Concisely describe the problem as a question that you went out and answered.

* **Solution (Answer)**: Concisely describe the solution as an answer to the question you posed in the previous section. Be specific.

* **Findings**: Bulleted lists of discoveries you made along the way that interests the audience. They may be discoveries in the data, methods that did or did not work or the model performance benefits you achieved along your journey.

* **Limitations**: Consider where the model does not work or questions that the model does not answer. Do not shy away from these questions, defining where the model excels is more trusted if you can define where it does not excel.

* **Conclusions (Why+Question+Answer)**: Revisit the "why", research question and the answer you discovered in a tight little package that is easy to remember and repeat for yourself and others.

You can discover more about using the results of a machine learning project in the post:

* [How to Use Machine Learning Results](http://machinelearningmastery.com/how-to-use-machine-learning-results/)

