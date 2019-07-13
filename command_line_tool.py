from datetime import datetime

import stock as stock_details
import analyze_stock

stocks = stock_details.get_all_stocks()


def stock_not_found():
    print("Sorry! We were not able to find your stock.")
    user_response = input("Do you want to try again? y or n:- ")
    if user_response == 'y':
        process_user_request()
    else:
        exit(1)


def continue_process():
    user_response = input("Do you want to continue? y or n:- ")
    if user_response == 'y':
        process_user_request()
    else:
        exit(1)


def get_user_stock():
    return input("Welcome Agent! Which stock do you need to process?:- ")


def user_response_for_suggestion():
    user_response = input("Do you want me to keep suggesting you stocks? y or n:- ")
    return True if user_response == 'y' else False


def suggest_a_stock(stock_name):
    user_response = input("Oops! Do you mean {name}? y or n:- ".format(name=stock_name))
    if user_response == 'y':
        return True
    else:
        return False


def process_user_request():
    user_stock = get_user_stock()
    stock_found = False
    suggestion_count = 3
    suggested_stocks = []

    for stock in stocks:
        stock_name = stock['name']
        if user_stock.lower() in stock_name.lower():
            if len(user_stock) < len(stock_name):
                if suggestion_count > 0:
                    if stock_name not in suggested_stocks:
                        suggestion_count -= 1
                        suggested_stocks.append(stock_name)
                        if suggest_a_stock(stock_name):
                            user_stock = stock_name
                            stock_found = True
                            break
                        else:
                            continue
                    else:
                        continue
                else:
                    if user_response_for_suggestion():
                        suggestion_count = 2
                        suggested_stocks.append(stock_name)
                        suggest_a_stock(stock_name)
                        if suggest_a_stock(stock_name):
                            user_stock = stock_name
                            stock_found = True
                            break
                        suggestion_count -= 1
                        continue
                    else:
                        user_response = input("Do you want to re-enter stock name? y or n:- ")
                        if user_response == 'y':
                            user_stock = get_user_stock()
                        else:
                            break
            else:
                stock_found = True
                break

    if not stock_found:
        stock_not_found()

    start_date = input("From which date do you want to start:- ")
    end_date = input("Till which date do you want to analyze:- ")
    try:
        start_date = datetime.strptime(start_date, "%d-%b-%Y")
        end_date = datetime.strptime(end_date, "%d-%b-%Y")
    except Exception as e:
        print(e.args)
        continue_process()
    analyze_stock.analyze_stock(stocks, user_stock, start_date, end_date)

    continue_process()


process_user_request()
