# HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to  the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

# Given the number of trailing days  and a client's total daily expenditures for a period of  days, find and print the number of times the client will receive a notification over all  days.

# For example,  and . On the first three days, they just collect spending data. At day , we have trailing expenditures of . The median is  and the day's expenditure is . Because , there will be a notice. The next day, our trailing expenditures are  and the expenditures are . This is less than  so no notice will be sent. Over the period, there was one notice sent



import math
import os
import random
import re
import sys

def activity_notifications(expenditure, d):
    notifications = 0
    size = len(expenditure)
    for index in range(size - d):
        period = sorted(expenditure[index:d+index])
        if d % 2 == 0: 
            median_double = period[int(d/2) - 1] + period[int(d/2)]
        else:
            median_double = period[int(d/2)] * 2
        if expenditure[d+index] >= median_double:
            notifications += 1
    return notifications

assert activity_notifications([1, 2, 3, 4, 4], 4) == 0
assert activity_notifications([2, 3, 4, 2, 3, 6, 8, 4, 5], 5) == 2



