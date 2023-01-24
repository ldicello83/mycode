#!/usr/bin/python3
munsters = {'endDate': 1966, 'startDate': 1964, 'names':['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']}
print( "Munsters Characters: ", munsters.get("names") )
print( "Start Date ", munsters.get("startDate"))
print( "End Date ", munsters.get("endDate"))
munsters['episodes'] = 70
print( "Episodes ", munsters.get("episodes"))
names = ['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']
for x in names:
    print(x, "is a character on the Munsters")

