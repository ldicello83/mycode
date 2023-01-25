#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""

message = 'Based upon your score, your grade is: '
score = float(input("What is your score?"))
if score >= 90:
    message = message + "A"
elif score >= 80:
    message = message + "B"
elif score >= 70:
    message = messge + "C"
elif score >= 60:
    message = message + "D"
elif score <= 59:
    message = message + "F"
else:
    message - message + "undetermined"
print(message)
