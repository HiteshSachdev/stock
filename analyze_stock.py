from datetime import datetime
import math

def max_difference(price_list, length):
    min_index, max_index = 0, 0
    max_diff = price_list[1] - price_list[0]
    min_element = price_list[0]

    for i in range(1, length):
        if price_list[i] - min_element > max_diff:
            max_diff = price_list[i] - min_element
            max_index, min_index = i, price_list.index(min_element)

        if price_list[i] < min_element:
            min_element = price_list[i]
    return min_index, max_index, max_diff


def analyze_stock(stocks, user_stock, start_date, end_date):
    stock_details_for_available_dates = []
    price_list, sum_of_stock_prices, sum_differences, sd = [], 0, 0
    for stock in stocks:
        stock_name = stock['name']
        stock_date = datetime.strptime(stock['date'], "%d-%b-%Y")
        stock_price = float(stock['price'])
        if user_stock == stock_name and start_date <= stock_date <= end_date:
            stock_details_for_available_dates.append({
                "stock_date": stock_date,
                "stock_price": stock_price
            })
            price_list.append(stock_price)
            sum_of_stock_prices += stock_price
    mean_of_prices = sum_of_stock_prices // len(price_list)
    min_index, max_index, profit = max_difference(price_list, len(price_list))
    for price in price_list:
        sum_differences += (price - mean_of_prices)
    sd = sum_differences*sum_differences // (len(price_list) - 1)
    sd = math.sqrt(sd)
    print("Your mean is: {mean} and standard deviation is: {sd}".format(mean=mean_of_prices, sd=sd))
    print("Here's your result:- Buy date: {bd}, Sell date: {sd}, Profit: {p} (for 100 shares)".format(
        bd=stock_details_for_available_dates[min_index]['stock_date'],
        sd=stock_details_for_available_dates[max_index]['stock_date'],
        p=profit*100
    ))


