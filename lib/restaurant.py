from __init__ import CURSOR, CONN
from review import Review

class Restaurant:
    all = {}

    def __init__(self, name, price, id=None):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Restaurant {self.id}: {self.name}, {self.price}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS restaurants (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS restaurants;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        if self.id:
            sql = """
                UPDATE restaurants SET name=?, price=? WHERE id=?
            """
            CURSOR.execute(sql, (self.name, self.price, self.id))
        else:
            sql = """
                INSERT INTO restaurants (name, price) VALUES (?, ?)
            """
            CURSOR.execute(sql, (self.name, self.price))
            self.id = CURSOR.lastrowid
        CONN.commit()
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, price):
        restaurant = cls(name, price)
        restaurant.save()
        return restaurant

    @classmethod
    def fanciest(cls):
        sql = """
            SELECT * FROM restaurants ORDER BY price DESC LIMIT 1
        """
        CURSOR.execute(sql)
        data = CURSOR.fetchone()
        if data:
            return cls(*data)
        else:
            return None

    def reviews(self):
        sql = """
            SELECT id, customer_id, star_rating
            FROM reviews
            WHERE restaurant_id = ?
        """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()
        reviews = [Review(*row) for row in rows]  # Create Review instances from fetched data
        return reviews

    def all_reviews(self):
        return [review.full_review() for review in self.reviews()]
