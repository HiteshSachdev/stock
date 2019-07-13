import csv


def get_all_stocks():
    with open("stocks.csv") as stocks_info:
        stocks = []
        reader = csv.DictReader(stocks_info, delimiter='|')
        for row in reader:
            stock = {
                "name": row['stock_name'],
                "date": row['stock_date'],
                "price": row['stock_price']
            }
            stocks.append(stock)
        return stocks
