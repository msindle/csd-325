#added new menu so user can select Highs, Lows, or exit.
#user can now choose High Lows, or exit. 
#when user selects lows it will now show graph in blue instead of red
#program will loop until user selects the exit option
#
import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

filename = '/home/ursin/Desktop/sitka_weather_2018_simple.csv'


dates = []
highs = []
lows = []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[5])
        low = int(row[6])

        highs.append(high)
        lows.append(low)

def plot_highs():
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    plt.title("Daily High Temperatures - 2018", fontsize=20)
    plt.xlabel("")
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)")
    plt.show()

def plot_lows():
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')
    plt.title("Daily Low Temperatures - 2018", fontsize=20)
    plt.xlabel("")
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)")
    plt.show()

def main_menu():
    print("\nSitka Weather Viewer")
    print("Choose an option:")
    print("1. Highs")
    print("2. Lows")
    print("3. Exit")

while True:
    main_menu()
    choice = input("Enter your choice: ").strip().lower()

    if choice in ("1", "highs", "h"):
        plot_highs()

    elif choice in ("2", "lows", "l"):
        plot_lows()

    elif choice in ("3", "exit", "e"):
        print("\nExiting program. Laters!")
        sys.exit()

    else:
        print("Invalid choice. Please try again.")
