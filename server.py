from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dateutil.parser import parse
from datetime import datetime, date, time


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://score:Rysherat2@shopscore.devman.org:5432/shop'
db = SQLAlchemy(app)
db.Model.metadata.reflect(db.engine)


class Orders(db.Model):
    __tablename__ = 'orders'


def count_waiting_time(order):
    if order:
        return ((datetime.now().hour*60 + datetime.now().minute) - 
                (order.created.hour+order.created.minute))
    else:
        return 0

@app.route('/')
def score():
    confirmed_orders = Orders.query.order_by(Orders.created).filter(Orders.confirmed.isnot(None))
    today_confirmed_orders = [order for order in confirmed_orders if 
                              order.confirmed.day == datetime.now().day and 
                              order.confirmed.month == datetime.now().month]
    unconfimed_order = Orders.query.order_by(Orders.created).filter(Orders.confirmed.is_(None)).first()
    waiting_time = count_waiting_time(unconfimed_order)
    unconfimed_orders = Orders.query.order_by(Orders.created).filter(Orders.confirmed.is_(None)).count()

    return render_template('score.html',
                           count_today_confirmed_orders = len(today_confirmed_orders),
                           count_unfirmed_orders = unconfimed_orders, unconfimed_order = int(waiting_time))


if __name__ == "__main__":
    app.run()
