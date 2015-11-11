# Bayesian Text Classification

Bayes classifiers are a popular statistical technique of e-mail filtering. They typically use bag of words features to identify spam e-mail, an approach commonly used in text classification.

Bayes classifiers work by correlating the use of tokens (typically words, or sometimes other things), with spam and non-spam e-mails and then using Bayes' theorem to calculate a probability that an email is or is not spam.

Bayes spam filtering is a baseline technique for dealing with spam that can tailor itself to the email needs of individual users and give low false positive spam detection rates that are generally acceptable to users. It is one of the oldest ways of doing spam filtering, with roots in the 1990s.

Source: https://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering

## Features
Calculates misclassification rate, gini index, and entropy.

## How to Run
1. Open settings.txt and set directory for spam and ham emails
2. To change discriminates goto tokens.py (ln 48-50)
2. Run bayesian_text_classification.py

