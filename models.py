from orm import db


class Bill(db.Model):
    __tablename__ = 'bills'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    due_date = db.Column(db.String(255), nullable=False)
    submitted = db.Column(db.DateTime, server_default=db.func.now())

    def __str__(self):
        return f"<Bill: {self.name} - Amount: {self.amount} />"
    
    def __repr__(self):
        return f"<Bill: {self.name} - Amount: {self.amount} />"


class CreditCardExpense(db.Model):
    __tablename__ = 'credit_card_expenses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    desc = name = db.Column(db.String(255))
    amount = db.Column(db.Float, nullable=False)
    expense_date = db.Column(db.String(255), nullable=False)
    submitted = db.Column(db.DateTime, server_default=db.func.now())

    def __str__(self):
        return f"<CreditCardExpense: {self.name} - Amount: {self.amount} />"
    
    def __str__(self):
        return f"<CreditCardExpense: {self.name} - Amount: {self.amount} />"


# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))


# class Cart(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     products = db.relationship('Product', backref='cart')
