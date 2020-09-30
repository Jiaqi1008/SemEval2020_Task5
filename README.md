# SemEval2020_Task5
This is the repository for SemEval 2020 Task 5 Counterfactual Detection. The related paper is `SemEval-2020 Task 5 Counterfactual Recognition.pdf`. Also, my report `ELEC896 report.pdf` for Master thesis can be a detail reference for this task. 

We collected counterfactual sentences online from three domains, finance, politics and health and then labeled them on the crowdsource platform, Amazon Turk. After that, we processed the results to build our dataset. Data and baseline model for Subtask 1 and Subtask 2 can be found in the folds `Subtask1_data` and `Subtask2_data`. 
## Data collection and parsing ##
From the collected corpus in three domains, Finance, Health and Politics, `sentence_pattern.py` is introduced to select the candidate sentences likely to be counterfactual. Then `turk_generate.py` is used to transform the selected sentences into the batch form Turk platform wants.
## Turk UI ##
The workers' UI can be seen in `Work UI.html`. Before we got the workers into the tasks, we gave them a tutorial for the each task and then made sure that they were all clear on what we wanted. Tutorial can be found in `Subtask1 UI.html` and `Subtask2 UI.html` respectively. Actually, we planned to established a third task, but due to the problem of short of time, it had been merged into Subtask 2, but you can still find `Subtask3 UI.html`. 
## Results processing ##
The results from Turk should be first processed by `process_from_Turk.py`. Following we furtherly process the results we get by `process.py`. After that we get the dataset we can use. Also, with `log_generation.py` we can get detailed information of the data in a log.
