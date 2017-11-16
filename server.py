from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date, time
from model import app, Orders


def count_waiting_time(order):
    if order:
        return datetime.now().hour*60 + datetime.now().minute -\
               order.created.hour+order.created.minute
    else:
        return 0

@app.route('/')
def score():
    confirmed_orders = Orders.query.order_by(
                                            Orders.status).filter(Orders.confirmed.isnot(None))
    today_confirmed_orders = [order for order in confirmed_orders if 
                              order.confirmed.day == datetime.now().day and 
                              order.confirmed.month == datetime.now().month ]
    unconfirmed_order = Orders.query.order_by(
                                              Orders.created).filter(Orders.confirmed.is_(None)).first()
    unconf_order_waiting_time = count_waiting_time(unconfirmed_order)
    unconfimed_orders = Orders.query.order_by(
                                              Orders.created).filter(Orders.confirmed.is_(None)).count()
    return render_template('score.html',
                           count_today_confirmed_orders = len(today_confirmed_orders),
                           count_unconfirmed_orders = unconfimed_orders,
                           unconf_order_waiting_time = int(unconf_order_waiting_time))


if __name__ == "__main__":
    app.run()
