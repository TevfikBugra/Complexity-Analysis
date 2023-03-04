# Complexity-Analysis 
This repository includes an assignment from IE201 Intermediate Programming course.  
  
  # Homework 1
___December 8th, 2022___

You are given a list containing prices where price[t] represents the price of gold at day t. This list contains historical prices of gold, and you are interested in calculating the maximum amount of profit you could have made in a single transaction (i.e. buy 1 gr of gold at a low price and then sell at a later day at a higher price). In other words, you need to choose a single day (b) to buy one gram of gold and a different day in the future (s) to sell it. You need to calculate the maximum possible profit (or return 0 if it is not possible to make profit). 

a)	Write a function called max_profit with O(n^2) complexity.

_def max_profit (price):_

b)	Write a function called max_profit_quick with O(n) complexity.

_def max_profit_quick (price):_

c)	Measure the time it takes to call the two functions for 20 different values of length of the price list (n) and report the results, where you generate prices randomly. Make sure that one of the 20 measurements is done for n = last 5 digits of your student ID. Choose the n values that you test so that there are measurable difference between the methods. For each value of n, test at least 10 random samples and report their average results. 

