#!/usr/bin/env python3
"""Understanding dictionaries
{key: value, key:value, ...]
using the dict.get() method"""

def main():
    """runtime function"""
## create a dictionary with 4key:value pairs
switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

#rst test - .get()" )
print( switch.get("lynx") )# display the etire dictionary
print(switch)
## prove that switch is a dictionary
print(type(switch))
#display parts of dictionary
print( switch["hostname"] )
print( switch["ip"] )

print( "First test - .get()" )
print( switch.get("lynx") )

print( "Second test - .get()" )
print( switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!") )

print( "Third test - .get()" )
print( switch.get("vendor") )

if __name__ == "_main__":
    main()
