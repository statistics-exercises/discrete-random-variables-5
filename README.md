# Generating binomial random variables

The videos and lectures this week have focussed on the binomial, geometric and negative binomial random variable.  We have seen that to generate all of these random variables you have to perform multiple Bernoulli trials.  In the programming exercises we are thus going to learn how to use the code for generating Bernoulli trials that we have learned about last week in order to generate binomial, geometric and negative binomial random variables.

In this first exercise you are going to generate binomial random variables.  To complete the exercise you must:

- Write a function called `bernoulli` that takes in a parameter called `p`. This parameter gives the probability that the trial is successful - and that the function thus returns a 1.

- Use your bernoulli function in a second program called `binomial`.  This `binomial` function should take two parameters as input `n` (the number of trials to perform) and `p` (the probability of success in each individual trial).  The function should then return a binomial random variable.

Remember that the binomial random variable simply counts the number of successes when you perform __n__ independent and identical Bernoulli trials. 

The idea that you will need to use to complete the function is explained in [this video](https://www.youtube.com/watch?v=RNQFAH2wCos)
