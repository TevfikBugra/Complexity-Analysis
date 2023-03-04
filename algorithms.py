import random
import time

# a)

# O(n^2)
def max_profit (price):
    lowest = price[0]
    profit = 0
    for i in range(len(price)):
        if price[i] < lowest:
            lowest = price[i]
        for k in range(i,len(price)):
            if price[k]-lowest > profit:
                profit = price[k]-lowest
    return profit
              
#print(max_profit(price))

# b)
# O(n)
def max_profit_quick (price):
    min_until = price[0]
    min_until_dict = dict()
    max_from = price[len(price)-1]
    max_from_dict = dict()
    for i in range(len(price)):
        if price[i] < min_until:
            min_until = price[i]
        min_until_dict[i] = min_until
    reversed_price = price[::-1]
    for k in range(len(price)):
        if reversed_price[k] > max_from:
            max_from = reversed_price[k]
        max_from_dict[len(price)-k-1] = max_from
    profit = 0
    for i in range(len(price)):
        if max_from_dict[i]-min_until_dict[i] > profit:
            profit = max_from_dict[i]-min_until_dict[i]
    return profit    

#print(max_profit_quick(price))

# c)
def average_time_check(n=1000,k=10):
# n = length of random number list
# k = iteration count
# prints average times of max_profit and max_profit_quick functions
    max_profit_list = []
    max_profit_quick_list =[]
    for a in range(k):
        randomlist = []
        for i in range(n):
            number = random.randint(0, 10*n)
            randomlist.append(number)
        start = time.time()
        max_profit(randomlist)
        max_profit_list.append(time.time() - start)
        start = time.time()
        max_profit_quick(randomlist)
        max_profit_quick_list.append(time.time() - start)
    print("n =",n)
    print('max_profit:', sum(max_profit_list)/len(max_profit_list))
    print('max_profit_quick:',sum(max_profit_quick_list)/len(max_profit_quick_list))

average_time_check(2120,10)