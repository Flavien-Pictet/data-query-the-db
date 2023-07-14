# pylint:disable=C0111,C0103

def query_orders(db):
    # return a list of orders displaying each column
    query = "SELECT * FROM Orders ORDER BY OrderID"
    db.execute(query)
    order = db.fetchall()
    return order

def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between
    # date_from and date_to (excluding date_from and including date_to)
    query = f"""
    SELECT *
    FROM orders
    WHERE OrderDate > ? AND OrderDate <= ?
    """

    db.execute(query, (date_from, date_to))
    orders = db.fetchall()
    return orders


def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    query = '''SELECT *,
            julianday (ShippedDate) -
            julianday (OrderDate)
            AS TimeDelta
            FROM orders
            ORDER BY TimeDelta ASC'''

    db.execute(query)
    waiting_time = db.fetchall()
    return waiting_time
