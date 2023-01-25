#!/user/bin/env python3
"""RZFeeser@alta3.com | Alta3 Research
   Using the CSV library to work with CSV data."""

# standard library import  csv is a toolbox; 
import csv

# open our csv data (we want to loop across this)
with open("csv_users.txt", "r") as csvfile:
    # counter to create unique file names
    i = 0
    # loop across our open file line by line; use reader tool to manipulate file
    for row in csv.reader(csvfile):
        i = i + 1  # or can do i += 1
        filename = f"admin.rc{i}"  # this f string says "fill in the value of f" admin.rc1 admin.rc2

        # open a file via "with"; this will autoclose when indentations end.
        with open(filename, "w") as rcfile:
            # use the standard library print function to print our data
            # out to the open file open rcfile (open in write mode)
            print("export OS_AUTH_URL=" + row[0], file=rcfile)
            print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
            print("export OS_PROJECT_NAME=" + row[1], file=rcfile)
            print("export OS_PROJECT_DOMAIN_NAME=" + row[2], file=rcfile)
            print("export OS_USERNAME=" + row[3], file=rcfile)
            print("export OS_USER_DOMAIN_NAME=" + row[4], file=rcfile)
            print("export OS_PASSWORD=" + row[5], file=rcfile)

