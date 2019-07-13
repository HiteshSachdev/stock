from datetime import datetime

import stock as stock_details
import analyze_stock

stocks = stock_details.get_all_stocks()


def process_user_request():
    user_stock = input("Welcome Agent! Which stock do you need to process?:- ")
    for stock in stocks:
        stock_name = stock.name
        stock_found = False
        if user_stock in stock_name:
            if len(user_stock) < len(stock_name):
                user_response = input("Oops! Do you mean {name}? y or n:- ".format(name=stock_name))
                if user_response == 'y':
                    user_stock = stock_name
                    stock_found = True
                    break
                else:
                    continue
            else:
                stock_found = True
                break
    if not stock_found:
        print("Sorry! We were not able to find your stock.")
        user_response = input("Do you want to try again? y or n:- ")
        if user_response:
            process_user_request()
        else:
            return
    start_date = input("From which date do you want to start:- ")
    end_date = input("Till which date do you want to analyze:- ")
    start_date = datetime.strptime(start_date, "%d-%b-%Y")
    end_date = datetime.strptime(end_date, "%d-%b-%Y")


process_user_request()
