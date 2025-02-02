# Q:Write a Python program that prints the calendar for a given month and year.
import calendar

y = int(input("input year :"))
m = int(input("input month :"))

print(calendar.month(y,m))
