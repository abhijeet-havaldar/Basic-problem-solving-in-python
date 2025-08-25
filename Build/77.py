#Q:Write a Python program to find the maximum profit in one transaction i.e., buy one and sell one share of the stock from the given price value of the said array. You cannot sell a stock before you buy one

def max_profit(stock_price):
    max_profit_amt = 0

    for i in range(len(stock_price)):
        profit_amt = 0
        
        for j in range(i+1, len(stock_price)):
            profit_amt = stock_price[j] - stock_price[i]
            
            if profit_amt > max_profit_amt:
                max_profit_amt = profit_amt
    
    return max_profit_amt

print(max_profit([224, 236, 247, 258, 259, 225]))
