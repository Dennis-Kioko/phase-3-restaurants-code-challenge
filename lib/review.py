from __init__ import CURSOR, CONN
from customer import Customer
from restaurant import Restaurant

class Review:
    all = {}
    
    def __init__(self, restaurant_id, customer_id, star_rating, id=None):
        self.id = id
        self.restaurant_id = restaurant_id
        self.customer_id = customer_id
        self.star_rating = star_rating
        type(self).all[self.id] = self
    
    def customer(self):
        return Customer.all[self.customer_id]
    
    def restaurant(self):
        return Restaurant.all[self.restaurant_id]
    
    def __repr__(self):
        return f"Review {self.id}: Restaurant {self.restaurant_id}, Customer {self.customer_id}, {self.star_rating} stars"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY,
            restaurant_id INTEGER,
            customer_id INTEGER,
            star_rating INTEGER,
            FOREIGN KEY (restaurant_id) REFERENCES restaurants(id),
            FOREIGN KEY (customer_id) REFERENCES customers(id))
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS reviews;
        """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        if self.id:
            sql = """
                UPDATE reviews SET restaurant_id=?, customer_id=?, star_rating=? WHERE id=?
            """
            CURSOR.execute(sql, (self.restaurant_id, self.customer_id, self.star_rating, self.id))
        else:
            sql = """
                INSERT INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)
            """
            CURSOR.execute(sql, (self.restaurant_id, self.customer_id, self.star_rating))
            self.id = CURSOR.lastrowid
        CONN.commit()

    @classmethod
    def create(cls, restaurant_id, customer_id, star_rating):
        review = cls(restaurant_id, customer_id, star_rating)
        review.save()
        return review

    def full_review(self):
        restaurant = self.restaurant()
        customer = self.customer()
        return f"Review for {restaurant.name} by {customer.full_name()}: {self.star_rating} stars."
