import argparse
import csv


# Pass in argument using argparse module in python
parser = argparse.ArgumentParser(description=" Currency Checker Application")

#  help - this shows the message  using the --help flag
parser.add_argument("currencycode", help ="the ISO 4270 currency code to be checked")
args = parser.parse_args()


# read the csv file
csv_file = csv.reader(open('CSIC.csv', "r"), delimiter=",")

# iterate over the file
for row in csv_file:

# check whether the input flag matches data in the 3rd column of the csv file
    if args.currencycode == row[2]:
        print("Currency Supported")
        print (row)
        exit()
else  :
    print('Currency NOT supported')