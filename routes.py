from flask import Blueprint
from orm import db
from models import Bill


api = Blueprint('api', __name__)


@api.route('/')
def index():
    return {'msg': 'Endpoint - index'}


@api.route('/get')
def get():
    resp = {'results': []}
    query_result = db.session.query(Bill).filter(Bill.id == 1)
    for row in query_result:
        resp['results'].append(str(row))
    return {'msg': resp}


@api.route('/add')
def add():
    # '2023-03-09'
    bill = Bill(
        name='Car payment', 
        type="Car", 
        amount=324.30,
        due_date='2023-04-05'
    )
    db.session.add(bill)
    db.session.commit()
    return {'msg': 'success'}

# @api.route('/add')
# def add_product():
#     product = Product(name="Milk", price=2.50)
#     try:
#         db.session.add(product)
#         db.session.commit()
#     except Exception as e:
#         print(e)
#         return {'msg': 'Insert failed'}
#     return {'msg': 'Insert Successful!'}
