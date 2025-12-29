#Q:Write a Python program to find all the factors of a given natural number.


from functools import reduce

def test(n):
    return set(reduce(list.__add__,
    ([i,n//i] for i in range(1,int(n**0.5) + 1) if n % i == 0)))



'''
Explanation of the test function:
sqrt(x) * sqrt(x) = x. So if the two factors are the same, they're both 
the square root. If you make one factor bigger, you have to make the other 
factor smaller. This means that one of the two will always be less than or 
equal to sqrt(x), so you only have to search up to that point to find one 
of the two matching factors. You can then use x / fac1 to get fac2.

The reduce(list.__add__, ...) is taking the little lists of [fac1, fac2] 
and joining them together in one long list.

The [i, n/i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0 returns 
a pair of factors if the remainder when you divide n by the smaller one 
is zero (it doesn't need to check the larger one too; it just gets that 
by dividing n by the smaller one.)

The set(...) on the outside is getting rid of duplicates, which only 
happens for perfect squares. For n = 4, this will return 2 twice, so 
set gets rid of one of them.
'''

n = 1
print("\nOriginal Number:",n)
print("Factors of the said number:", test(n))

n = 12
print("\nOriginal Number:",n)
print("Factors of the said number:", test(n))

n = 100
print("\nOriginal Number:",n)
print("Factors of the said number:", test(n))