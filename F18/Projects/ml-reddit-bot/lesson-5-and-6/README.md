# Lesson 5/6: Cyberbullying Detection

By the end of this lesson, you will have a built a cyberbullying detection engine that can scan through new Reddit posts to indentify any instances of cyberbullying!

We will build a few different machine learning models and compare them to see which works best. Unlike previous lessons, we will be working with a sizable amount of data.

## Today's Lesson

Most of today will be spent live coding. I will explain the process as we develop the code. For those of you who are reading this from home, here are some [Slides](https://docs.google.com/presentation/d/1JtyxCZgrOoT88ObknnBJi-gtsclQWGEpIebIQSacIjg/edit?usp=sharing) which contain my talking points for this lesson

## Important Notice

Due to the amount of code we have to go over today, I can only provide a very small amount of help with debugging. If your code isn't running, please follow along the best you can. 

I've allocated a lot of time during next week's meeting to help get the code working for everyone. Alternatively, you can also reach out to me on Slack or stay after the lesson.

## Data Acquisition

Please download _final_labelled_data.pkl_ from the /data folder, we will be using this to train our machine learning models. I compiled this dataset through manipulating and combining data from a [Sentiment Analysis dataset](https://www.kaggle.com/kazanova/sentiment140) and a [Hate Speech and Offensive Language dataset](https://github.com/t-davidson/hate-speech-and-offensive-language/tree/master/data).

## Project Setup Instructions

1. Create a new folder on your computer

2. Create a folder named /data inside your new folder

3. Place the _final_labelled_data.pkl_ file inside your /data folder

4. Create a new python file so we can start coding, when saving for the first time, make sure you save it in the new folder (not the data folder)

5. Make sure any more data files we add later on go inside the /data folder

6. Create a folder called /models inside the new folder when we begin developing the model saving and loading capabilities of our code



## Ideas for Project Enhancement

For those of you who want to take this project further, here is a list of ideas in how you can improve the models

- Setting probability thresholds for prediction to reduce the number of false positives

- Using ensemble learning to combine different machine learning models (such as Naive Bayes classifier with the TF-IDF word vectors and the Support Vector Machine using our custom word vectors) to improve the model evaluation metrics

- Creating more detailed custom word vectors for the SVM to train on

- Using NLP techniques like target identification and sentiment analysis to filter out false positives
