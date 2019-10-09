# Lesson 1: Intro to ML
By the end of this lesson, you will have built your first machine learning model! Don't worry about being unfamiliar with machine learning or even coding in general. I've designed this workshop for people who don't know the first thing about programming.

## Today's Schedule

- Introductions

- Getting Slack

- Downloading Software

- What is Machine Learning?

- The Naive Bayes Classifer

- Build a Naive Bayes Classification Model

## Introductions

My name is **Moeyyad** Qureshi, and I'll be taking you through this workshop. We will be going from Zero knowledge of programming to building an Artificial Intelligence. There is no prerequiste knowledge for being here, just be willing to learn :)

My credentials are two co-op terms of working as a Machine Learning Engineer / Data Scientist. One term was spent at a startup in Chile working closely with Natural Language Processing (or NLP for short), the other term was spent at Shopify doing R&D. 

## Why Learn about Machine Learning?

Machine learning has certainly become a buzzword in the tech industry, mainly as it can be used to solve a lot of different problems. In fact, you encouter machine learning everyday! Google search engine, Facebook feed, Netflix movie recommendations, etc.

Getting into machine learning will not only open more career opportunities, but also gives you a lot of insight into the digital products that power the world.

## Slack

[Write down your name and email here to get access](https://docs.google.com/spreadsheets/d/13LUO-CWHUQF-RUSJjOAyUVVyCdsOsd-Q42asabKGn_Q/edit?usp=sharing)

## Software

Okay, here is when things get messy, don't freak out if you can't get something to download properly. Just raise your hand and ask me, or ask the person beside you to help.

IF you are a Windows user, install [Git Bash](https://git-scm.com/downloads) and use that when I say to use your terminal.

Install Python 3.6.6 [Here](https://www.python.org/downloads/). **DO NOT** install version 3.7, there is an issue that breaks sklearn which is what we need to do the machine learning, it is also not supported by PRAW which we will use to interact with Reddit. Python is the programming language we will use.

**If you are a Windows User and python doesn't work in terminal:** Follow this link: [Click Me](https://superuser.com/questions/143119/how-do-i-add-python-to-the-windows-path). **For the last step, put Python36 instead of Python27** and restart your computer

To check if python install correctly, type `python3` into your terminal if Mac, or `python -i` if Windows to see if it works. Type in `quit()` to exit the python shell.

Installing Python should've installed PIP, which is a package manager that makes it easy to download python libraries. In terminal, type `pip3 --version` (Mac) or `python -m pip --version` (Windows) and a message should pop-up. Let me know if you have any problems.

Next type into terminal `pip3 install praw` and `pip3 install sklearn` (Mac) or `python -m pip install praw` and `python -m pip install sklearn` (Windows). Let me know if you get any errors.

To make sure everything installed properly, type `python3` (Mac) or `python -i` (Windows) followed by `import sklearn` and `import praw`. If no 'module not found' errors popup, you should be good :) 

## What Exactly IS Machine Learning?

Machine learning is teaching computers to learn rules and patterns by without being explicitly told. This is done by giving a machine learning model lots of data which they will analyze using an algorithm. Different machine learning models use different algorithms, and some algorithms are better suited to solving certain types of problems.

For example, we might not program driving rules into a self-driving-car, we just give the car lots of driving data and it figures out the driving rules.

One practical use of machine learning is when there are too many rules for us to explicitly tell the computer, for example we can't build a chess engine using one big if-statement!

Machine learning isn't as complicated as it sounds. A lot of machine learning is just building a matrix (a grid of numbers) that helps the computer make decisions!

## Naive Bayes Classifier

Naive Bayes is one specific type of machine learning model, best suited to classification problems. 

[How it works](https://monkeylearn.com/blog/practical-explanation-naive-bayes-classifier/)


## Let's build a Email Spam Detection machine learning model

We want to know if an email is either spam or not spam, so this is a classification problem. Let's solve this using Naive Bayes! Go to the spam_detection.py file in this folder.
