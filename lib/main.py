from restaurant import Restaurant
from customer import Customer
from review import Review
import sqlite3

def reset_database():
    conn = sqlite3.connect('burudani.db')
    cursor = conn.cursor()

    # Drop existing tables
    Customer.drop_table()
    Restaurant.drop_table()
    Review.drop_table()
    
    # Create tables
    Customer.create_table()
    Restaurant.create_table()
    Review.create_table()

    # Create sample customers
    customer1 = Customer.create("Dennis", "Kioko")
    customer2 = Customer.create("Mulei", "Archy")
    customer3 = Customer.create("Joy", "Nderitu")
    customer4 = Customer.create("Aisha", "Joy")
    
    # Create sample restaurants
    restaurant1 = Restaurant.create("Panari", 40000)
    restaurant2 = Restaurant.create("Chemi Chemi", 15000)
    restaurant3 = Restaurant.create("Wild Waters", 70000)
    restaurant4 = Restaurant.create("Eden Rock", 100000)

    # Create sample reviews
    Review.create(restaurant1.id, customer1.id, 5)
    Review.create(restaurant1.id, customer2.id, 4)
    Review.create(restaurant2.id, customer3.id, 3)
    Review.create(restaurant2.id, customer4.id, 2)

reset_database()

def main():
    # Test methods
    customer1 = Customer.all[1]
    print(f"Full name of customer1: {customer1.full_name()}")
    print(f"Favorite restaurant of customer1: {customer1.favorite_restaurant()}")

    restaurant2 = Restaurant.all[2]
    customer1.delete_reviews(restaurant2)
    print("Deleted reviews for customer1 for restaurant2.")

    print(f"Reviews for restaurant2: {restaurant2.all_reviews()}")

    restaurant1 = Restaurant.all[1]
    print(f"Reviews for restaurant1: {restaurant1.all_reviews()}")

    reviews = restaurant1.all_reviews()
    print("Reviews for restaurant1:", reviews)

    restaurant2 = Restaurant.all[2]
    reviews = restaurant2.all_reviews()
    print("Reviews for restaurant2:", reviews)

    restaurant1 = Restaurant.fanciest()
    print(f"Fanciest restaurant: {restaurant1}")

    # Add reviews for the fanciest restaurant
    customer1.add_review(restaurant1, 5)
    customer2.add_review(restaurant1, 4)

    # Fetch reviews for the fanciest restaurant
    reviews = restaurant1.all_reviews()
    print("Reviews for fanciest restaurant:", reviews)

if __name__ == "__main__":
    main()
