# Takes output predicted by ML model 
# Outputs how much profit user would have made if he/she would have used model to trade

# Importing required modules
import pandas as pd
import matplotlib.pyplot as plt
from pred import *

# Function   :- fetches output predicted by ML model
# Returns    :- DataFrame containing output predicted by model
def get_pred(sn, s, e):
    return calls(sn, s, e)

# Function   :- calculates and finds how much profit or loss would have happened if user invested according ML model
# Parameters :- t - DataFrame containing output of ML model
def simulator(t, m):
    # m - amount which user want to invest
    # c - count of stock
    om = m
    c = 0
    d = {}
    print(f'Default Money = {m}')
    print("\n")
    # calculating profit or loss according output predicted by ML model
    for i in range(len(t)):
        if (t['pred'][i] > 0):
            if m > t['Close'][i]:
                m = m - t['Close'][i]
                c = c + 1

        else:
            if c > 0:
                m = m + t['Close'][i]
                c = c - 1

    d["Money"] = m
    d["Stock"] = c
    d["Stock Price"] = t["Open"][-1]
    d["Profit"] = c*t["Open"][-1] + m - om

    print(f'Money = {m}')
    print(f'Stock = {c}')
    print(f'Stock Price = {t["Open"][-1]}')

    print(f'Profit = {c*t["Open"][-1] + m - 10000}')

    return d

# def graph(t):
#     plt.figure(figsize = (12,5))
#     t['Adj Close'].plot()
#     plt.savefig("output.jpg")

# Function   :- fetches output predicted by ML model and give it to simulator()
def execute_s(sn, s, e, m):
    df = get_pred(sn, s, e)
    d = simulator(df, m)
    #graph(df)

    return d

if __name__ == '__main__':
    start_date = datetime.date(2015, 1, 1)
    end_date = datetime.date(2020, 1, 1)

    d = execute('AAPL', start_date, end_date, 10000)