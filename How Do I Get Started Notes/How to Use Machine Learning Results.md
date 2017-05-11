Once you have [found](http://machinelearningmastery.com/how-to-evaluate-machine-learning-algorithms/) and [tuned](http://machinelearningmastery.com/how-to-improve-machine-learning-results/) a viable model of your problem it is time to make use of that model. You may need to revisit your [why](http://machinelearningmastery.com/how-to-define-your-machine-learning-problem/) and remind yourself what form you need a solution for the problem you are solving.

The problem is not addressed until you do something with the results. In this post you will learn tactics for presenting your results in answer to a question and considerations when turning your prototype model into a production system.

![image alt text](image_0.jpg)

Presentation of Results

Photo attributed to [Phil Sexton](http://www.flickr.com/photos/john_hall_associates/3175199088/sizes/l/), some rights reserved

Depending on the type of problem you are trying to solve, the presentation of results will be very different. There are two main facets to making use of the results of your machine learning endeavor:

* Report the results

* Operationalize the system

## **Report Results**

Once you have discovered a good model and a good enough result (or not, as the case may be), you will want to summarize what was learned and present it to stakeholders. This may be yourself, a client or the company for which you work.

Use a powerpoint template and address the sections listed below. You might like to write up a one-pager and use part section as a section header. Try to follow this process even on small experimental projects you do for yourself such as tutorials and competitions. It is easy to spend an inordinate number of hours on a project and you want to make sure to capture all the great things you learn along the way.

Below are the sections you can complete when reporting the results for a project.

* **Context** (Why): Define the environment in which the problem exists and set up the motivation for **the** research question.

* **Problem** (Question): Concisely describe the problem as a question that you went out and answered.

* **Solution** (Answer): Concisely describe the solution as an answer to the question you posed in the previous section. Be specific.

* **Findings**: Bulleted lists of discoveries you made along the way that interest the audience. They may be discoveries in the data, methods that did or did not work or the model performance benefits you achieved along your journey.

* **Limitations**: Consider where the model does not work or questions that the model does not answer. Do not shy away from these questions, defining where the model excels is more trusted if you can define where it does not excel.

* **Conclusions** (Why+Question+Answer): Revisit the why, research question and the answer you discovered in a tight little package that is easy to remember and repeat for yourself and others.

The type of audience you are presenting to will define the amount of detail you go into. Having the discipline to complete your projects with a report on results, even on small side projects will accelerate your learning in field. On such small side projects, I highly recommend sharing results of side projects on blogs or with communities and elicit feedback that you can capture and take with you into the start of your next project.

## **Operationalize**

You have found a model that is good enough at addressing the problem you face that you would like to put it into production. This may be an operational installation on your workstation in the case of a fun side project, all the way up to integrating the model into an existing enterprise application. The scope is enormous. In this section you will learn three key aspects to operationalizing a model that you could consider carefully before putting a system into production.

Three areas that you should think carefully about are the algorithm implementation, the automated testing of your model and the tracking of the models performance through time. These three issues will very likely influence the type of model you choose.

### **Algorithm Implementation**

It is likely that you were using a research library to discover the best performing method. The algorithm implementations in research libraries can be excellent, but they can also be written for the general case of the problem rather than the specific case with which you are working.

Think very hard about the dependencies and technical debt you may be creating by putting such an implementation directly into production. Consider locating a production-level library that supports the method you wish to use. You may have to repeat the process of algorithm tuning if you switch to a production level library at this point.

You may also consider implementing the algorithm yourself. This option may introduce risk depending on the complexity of the algorithm you have chosen and the implementation tricks it uses. Even with open source code, there may be a number of complex operations that may be very difficult to internalize and reproduce confidently.

### **Model Tests**

Write automated tests that verify that the model can be constructed and achieve a minimum level of performance repeatedly. Also write tests for any data preparation steps. You may wish to control the randomness used by the algorithm (random number seeds) for each unit test run so that tests are 100% reproducible.

### **Tracking**

Add infrastructure to monitor the performance of the model over time and raise alarms if accuracy drops below a minimum level. Tracking may occur in real-time or with samples of live data on a re-created model in a separate environment. A raised alarm may be an indication that that structure learned by the model in the data have changed (concept drift) and that the model may need to be updated or tuned.

There are some model types that can perform online learning and update themselves. Think carefully in allowing models to update themselves in a production environment. In some circumstances, it can be wiser to manage the model update process and switch out models (their internal configuration) as they are verified to be more performant.

## **Summary**

In this post you learned that a project is not considered complete until you deliver the results. Results may be presented to yourself or to your clients and there is a minimum structure to follow when presenting results.

You also learned three concerns when using a learned model in a production environment, specifically the nature of the algorithm implementation, model tests and on going tracking.

