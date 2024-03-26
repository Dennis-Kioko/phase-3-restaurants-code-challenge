# Phase 3 Code Challenge: Restaurants

## Overview

In this assignment, we'll be working with a restaurant review domain. We have three models: `Restaurant`, `Review`, and `Customer`.

For our purposes:
- A `Restaurant` has many `Review`s.
- A `Customer` has many `Review`s.
- A `Review` belongs to a `Restaurant` and to a `Customer`.

**Note**: Before starting coding, it's recommended to draw your domain on paper or a whiteboard to identify a single source of truth for your data.

## Topics
- Table Relationships
- Class and Instance Methods
- Database Querying
- SQLite3 and the Cursor Object

## Instructions
Build out all of the methods listed in the deliverables. 

**Remember!**
- This code challenge does not have tests. You cannot run `pytest`.
- You'll need to create your own sample instances for testing your code.
- Prioritize writing methods that work over writing more methods that don't work.
- Writing error-free code is important. Prioritize getting things working over code cleanliness initially.

## What You Need to Have
You need:
- Test data and models for the initial `Restaurant` and `Customer` models.
- An SQL table with data for some `Restaurant`s and `Customer`s.

## Deliverables
Write the following methods in the classes. Feel free to build out any helper methods if needed.

### Database Setup
Before working on the rest of the deliverables, create all tables.

- A `Review` belongs to a `Restaurant` and a `Customer`.
- The `reviews` table should have:
  - A `star_rating` column that stores an integer.

### Object Relationship Methods

#### Review
- `Review.customer()`: Returns the `Customer` instance for this review.
- `Review.restaurant()`: Returns the `Restaurant` instance for this review.

#### Restaurant
- `Restaurant.reviews()`: Returns all reviews for the restaurant.
- `Restaurant.customers()`: Returns all customers who reviewed the restaurant.

#### Customer
- `Customer.reviews()`: Returns all reviews by the customer.
- `Customer.restaurants()`: Returns all restaurants reviewed by the customer.

### Aggregate and Relationship Methods

#### Customer
- `Customer.full_name()`: Returns the full name of the customer.
- `Customer.favorite_restaurant()`: Returns the restaurant with the highest star rating from this customer.
- `Customer.add_review(restaurant, rating)`: Adds a new review for the given restaurant.
- `Customer.delete_reviews(restaurant)`: Removes all reviews for a specific restaurant.

#### Review
- `Review.full_review()`: Returns a formatted string of the review.

#### Restaurant
- `Restaurant.fanciest()`: Returns the restaurant with the highest price.
- `Restaurant.all_reviews()`: Returns a list of strings with all reviews for the restaurant.

## Note
Check that these methods work before proceeding.

