from yahoo_fin import stock_info as si
import math
from datetime import datetime
from datetime import date
import os
import time

# Creates path to the base folder (the folder this python file is in)
base_folder = os.path.dirname(__file__)

# Creates path to data.txt
path = os.path.join(base_folder, "data.txt")

# Open the data file for appending purposes
edit = open('data.txt', 'a')

# Requests stock name input
sname = input("What stock would you like to track today?")

# Requests interval in minutes
mins = input("What should the time interval between updates be in minutes?")

# Requests overall time
overall = input("For how many minutes would you like to track this stock?")

# Finds current time
now = datetime.now()

# Finds current time and date
dt_string = now.strftime("%d/%m/%Y/ %H:%M:%S")

# Calculates number of loops
loop_number = math.floor(int(overall) / int(mins))

# Creates statement that will seperate data for different stocks and dates
intro_statement = dt_string + " " + sname + " data\n"

# Defines function that will fetch stock value and write it to the file along with the time
# the stock value was retrieved
def fetch_value(stock):
    with open(path, 'a') as edit:
        edit.write(intro_statement)
    loop_count = 0
    while loop_count <= loop_number:
        loop_count += 1
        market = si.get_live_price(stock)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        statement = str(current_time) + ": " + str(market) + "\n"
        with open(path, 'a') as edit:
            edit.write(statement)
        time.sleep(int(mins) * 60)

fetch_value(sname)
print("Finished!")






    



