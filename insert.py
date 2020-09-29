from __future__ import print_function
from os.path import join, dirname, abspath
import xlrd
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="hasanyoneseenmomar"
)

def read():
    fname = join(dirname(dirname(abspath(__file__))), 'barCrawl', 'data.xls')

    # Open the workbook
    book = xlrd.open_workbook(fname)

    # name each sheet
    drinks = book.sheet_by_name("drinks")
    bars = book.sheet_by_name("bars")

    # create a python dictionary with each row of the drinks spreadsheet
    drinks_qty = drinks.nrows
    drink_objs = []
    for i in range(1, drinks_qty):
        drink = drinks.row(i)[0].value
        drink_type = drinks.row(i)[1].value
        price = drinks.row(i)[2].value
        ounces = drinks.row(i)[3].value
        apv = drinks.row(i)[4].value
        bar_id = int(drinks.row(i)[5].value)
        obj = {"drink": drink, "drink_type": drink_type, "ounces": ounces, "price": price, "apv": apv, "bar_id": bar_id}
        # add new object to an array
        drink_objs.append(obj)

    insert_drinks(drink_objs)

    # create a python dictionary with each row of the drinks spreadsheet
    bars_qty = bars.nrows
    bar_objs = []
    for x in range(1, bars_qty):
        bar = bars.row(x)[0].value
        vibes = int(bars.row(x)[1].value)
        comments = bars.row(x)[2].value
        obj = {"bar": bar, "vibes": vibes, "comments": comments}
        bar_objs.append(obj)
    
    insert_bars(bar_objs)

def insert_drinks(drink_objs):
    cursor = mydb.cursor()
    # select database
    cursor.execute("USE bar_crawl;")

    for drink_obj in drink_objs:
        sql = "INSERT INTO drinks (drink, drink_type, price, ounces, apv, bar_id) VALUES (%s, %s, %s, %s, %s, %s)"
        vals = (drink_obj['drink'], drink_obj['drink_type'] ,drink_obj['price'], drink_obj['ounces'], drink_obj['apv'], drink_obj['bar_id'])
        cursor.execute(sql, vals)
        mydb.commit()

    #print contents of updated table

    cursor.execute("SELECT * FROM drinks;")
    
    for x in cursor:
        print(x)

def insert_bars(bar_objs):
    cursor = mydb.cursor()

    # select database
    cursor.execute("USE bar_crawl;")

    for bar_obj in bar_objs:
        sql = "INSERT INTO bars (bar, vibes, comments) VALUES (%s, %s, %s)"
        vals = (bar_obj['bar'], bar_obj['vibes'] ,bar_obj['comments'])
        cursor.execute(sql, vals)
        mydb.commit()

    # print contents of updated table
    cursor.execute("SELECT * FROM bars;")
    
    for x in cursor:
        print(x)
    

if __name__ == '__main__':
    read()