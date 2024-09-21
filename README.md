# Python-Development

# Application Instructions

This repository contains three different tasks implemented in Python and SQL. Follow the instructions below to set up and run each task.

## Prerequisites

- Python 3.x installed
- A working SQL environment (e.g., MySQL, PostgreSQL, SQLite)
- Basic text editor or IDE

---

## Task 1: Aggregate Weather Data

### Description
This Python function takes a list of weather records for various cities and provides insights such as average temperature and humidity. It gracefully handles missing data.

### How to Run
1. Save the code in a Python file, e.g., `aggregate_weather_data.py`.
2. Modify the example `weather_records` to include the data you want to analyze.
3. Run the Python file:
   
## Task 2: Prime Factorization 

### Description 
This Python function takes an integer and returns its prime factorization as a list of tuples, where each tuple contains a prime factor and its corresponding exponent.

### How to Run
1. Save the code in a Python file, e.g., prime_factorization.py.
2. Modify the n value to the integer you want to factorize.
3. Run the Python file
4. The output will display the prime factorization in the format [(prime, exponent)].
   
## Task 3: SQL Query - Increase Product Prices

### Description 
This SQL query increases the price of all products in a database table named products by 10% and displays the new prices along with the product names.

### How to Run
1. Open your SQL client or terminal.
2. Make sure the products table is set up with the following structure
   ```bash
   CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(10, 2));
3. Run the SQL Query:
   ```bash
   SELECT name, price * 1.10 AS new_price FROM products;
4. The output will display the product names with the increased prices.
