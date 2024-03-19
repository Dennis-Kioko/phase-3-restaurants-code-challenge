from __init__ import CURSOR, CONN

class Customer:
    all = {}

    def __init__(self, first_name, last_name, id=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
    
    def __repr__(self):
        return f"Customer {self.id}: {self.first_name} {self.last_name}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS customers;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        if self.id:
            sql = """
                UPDATE customers SET first_name=?, last_name=? WHERE id=?
            """
            CURSOR.execute(sql, (self.first_name, self.last_name, self.id))
        else:
            sql = """
                INSERT INTO customers (first_name, last_name) VALUES (?, ?)
            """
            CURSOR.execute(sql, (self.first_name, self.last_name))
            self.id = CURSOR.lastrowid
        CONN.commit()
        type(self).all[self.id] = self

    @classmethod
    def create(cls, first_name, last_name):
        customer = cls(first_name, last_name)
        customer.save()
        cls.all[customer.id] = customer
        return customer

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        # Importing Restaurant locally
        from restaurant import Restaurant
        reviews = self.reviews()
        if not reviews:
            return None
        max_rating_review = max(reviews, key=lambda x: x.star_rating)
        return max_rating_review.restaurant()

    def add_review(self, restaurant, rating):
        # Importing Review locally
        from review import Review
        review = Review.create(restaurant.id, self.id, rating)
        review.save()

    def delete_reviews(self, restaurant):
        sql = """
            DELETE FROM reviews
            WHERE restaurant_id = ? AND customer_id = ?
        """
        CURSOR.execute(sql, (restaurant.id, self.id))
        CONN.commit()

    def reviews(self):
        # Importing Review locally
        from review import Review
        return [review for review in Review.all.values() if review.customer_id == self.id]

    def restaurants(self):
        # Importing Restaurant locally
        from restaurant import Restaurant
        return [Restaurant.all[review.restaurant_id] for review in self.reviews()]
