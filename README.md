# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.**  You  _are_  allowed to use Internet documentation. If you  _do_  use existing code (either from Github, Stack Overflow, or other sources),  **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a  **public**  fork of this repo and name it  `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using  `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria 

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted. 

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in  `input.txt`  contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.**  If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.   

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

## Explanation
I was inexperienced with sentiment analysis, so I used google to search for helpful informations. Among different libraries, I found blobtext and NTLK to be the easiest ones to use, and I choose to use nltk and build-in VADER function for my code.
One of the helpful tutorials: https://www.nltk.org/howto/sentiment.html

I first tokenize the text into sentences then analyze the polarity score of each sentence. I sum those scores and simply average them to get the final score.
The results are:
#positive score 0.1461875
#negetive score 0.11078124999999998
#compound score 0.171221875

Compound score will be the final score, and value indicates that the passage is slightly positive. This score is somewhat close to my prediction. The first part seems to be negative and second part is neutral or slightly positive. Because the second part seems longer and conclusive, slightly positive or neutral is what I expected to be the overall score, and the computed score is very close to my prediction.

I only used simple average to get the overall score, so I believe there are still many aspects that I can improve such as using the length as weight or using stopwords to improve precision. Knowing there are still so much to learn makes me really want to use this opportunity to be a part of ACM.
