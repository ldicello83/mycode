#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""
message = "Based upon your input, your postage rate is "
weight = float(input("What is your package weight in ounces?"))
if weight <= 4:
    message = message + "42 cents"
elif weight > 15:
    message = message + "$1.39"
elif weight > 4:
    message = message + "87 cents"
else:
    message = messahge + "needs special handling"
print(message)
