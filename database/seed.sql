
-- insert data into regions table
INSERT INTO regions (name)
VALUES 
    ('USA'),
    ('IN'),
    ('UK'),
    ('Russia'),
    ('China');



INSERT INTO customers (first_name, last_name, email, region_id)
VALUES
    ('Amit', 'Bhagat', 'amitrbhagat679@gmail.com', 1),
    ('Rahul', 'Sharma', 'rahul.sharma01@gmail.com', 2),
    ('Priya', 'Patel', 'priya.patel02@gmail.com', 3),
    ('Sneha', 'Joshi', 'sneha.joshi03@gmail.com', 4),
    ('Arjun', 'Mehta', 'arjun.mehta04@gmail.com', 5),
    ('Neha', 'Deshmukh', 'neha.deshmukh05@gmail.com', 1),
    ('Rohit', 'Kulkarni', 'rohit.kulkarni06@gmail.com', 2),
    ('Pooja', 'Shinde', 'pooja.shinde07@gmail.com', 3),
    ('Vikram', 'Jadhav', 'vikram.jadhav08@gmail.com', 4),
    ('Ananya', 'Gupta', 'ananya.gupta09@gmail.com', 5),
    ('Karan', 'Verma', 'karan.verma10@gmail.com', 1),
    ('Riya', 'Nair', 'riya.nair11@gmail.com', 2),
    ('Siddharth', 'Rao', 'siddharth.rao12@gmail.com', 3),
    ('Kavya', 'Iyer', 'kavya.iyer13@gmail.com', 4),
    ('Aditya', 'Singh', 'aditya.singh14@gmail.com', 5),
    ('Meera', 'Kadam', 'meera.kadam15@gmail.com', 1),
    ('Akash', 'Pawar', 'akash.pawar16@gmail.com', 2),
    ('Isha', 'Malhotra', 'isha.malhotra17@gmail.com', 3),
    ('Nikhil', 'Chavan', 'nikhil.chavan18@gmail.com', 4),
    ('Tanvi', 'Bhosale', 'tanvi.bhosale19@gmail.com', 5),
    ('Varun', 'Desai', 'varun.desai20@gmail.com', 1),
    ('Simran', 'Kaur', 'simran.kaur21@gmail.com', 2),
    ('Manish', 'Yadav', 'manish.yadav22@gmail.com', 3),
    ('Shreya', 'Mishra', 'shreya.mishra23@gmail.com', 4),
    ('Abhishek', 'Joshi', 'abhishek.joshi24@gmail.com', 5),
    ('Divya', 'Saxena', 'divya.saxena25@gmail.com', 1),
    ('Harsh', 'Agarwal', 'harsh.agarwal26@gmail.com', 2),
    ('Nandini', 'Reddy', 'nandini.reddy27@gmail.com', 3),
    ('Yash', 'Thakur', 'yash.thakur28@gmail.com', 4),
    ('Maya', 'Shah', 'maya.shah29@gmail.com', 5);


INSERT INTO products (name, category, price)
VALUES
    -- Electronics
    ('Wireless Earbuds', 'Electronics', 29.99),
    ('Bluetooth Speaker', 'Electronics', 59.99),
    ('Mechanical Keyboard', 'Electronics', 89.99),
    ('Smartphone', 'Electronics', 699.99),
    ('Laptop', 'Electronics', 1199.99),
    ('4K Monitor', 'Electronics', 449.99),
    ('Basic T-Shirt', 'Apparel', 19.99),
    ('Jeans', 'Apparel', 49.99),
    ('Hoodie', 'Apparel', 69.99),
    ('Running Shoes', 'Apparel', 119.99),
    ('Winter Jacket', 'Apparel', 199.99),
    ('Premium Suit', 'Apparel', 599.99),
    ('Coffee Mug', 'Home', 12.99),
    ('Desk Lamp', 'Home', 34.99),
    ('Bed Sheet Set', 'Home', 59.99),
    ('Office Chair', 'Home', 149.99),
    ('Vacuum Cleaner', 'Home', 299.99),
    ('Smart Refrigerator', 'Home', 1299.99),
    ('Water Bottle', 'Sports', 14.99),
    ('Yoga Mat', 'Sports', 24.99),
    ('Resistance Bands', 'Sports', 29.99),
    ('Basketball', 'Sports', 39.99),
    ('Tennis Racket', 'Sports', 129.99),
    ('Mountain Bike', 'Sports', 899.99),
    ('Python Programming', 'Books', 24.99),
    ('Database Design', 'Books', 39.99),
    ('Machine Learning Guide', 'Books', 59.99),
    ('System Design Handbook', 'Books', 49.99),
    ('AI Engineering', 'Books', 79.99),
    ('Software Architecture', 'Books', 99.99);



INSERT INTO orders (customer_id, order_date, status)
VALUES
    (22, '2025-01-12', 'cancelled'),
    (3, '2025-01-16', 'returned'),
    (3, '2025-01-31', 'completed'),
    (29, '2025-02-10', 'completed'),
    (28, '2025-02-18', 'completed'),
    (10, '2025-02-25', 'completed'),
    (1, '2025-03-02', 'completed'),
    (17, '2025-03-08', 'completed'),
    (25, '2025-03-14', 'completed'),
    (6, '2025-03-20', 'returned'),
    (14, '2025-03-25', 'completed'),
    (30, '2025-03-30', 'completed'),
    (8, '2025-04-04', 'completed'),
    (19, '2025-04-09', 'completed'),
    (2, '2025-04-15', 'completed'),
    (11, '2025-04-20', 'cancelled'),
    (24, '2025-04-27', 'completed'),
    (5, '2025-05-03', 'completed'),
    (13, '2025-05-09', 'completed'),
    (27, '2025-05-15', 'returned'),
    (16, '2025-05-21', 'completed'),
    (7, '2025-05-28', 'completed'),
    (21, '2025-06-04', 'completed'),
    (4, '2025-06-10', 'completed'),
    (18, '2025-06-16', 'completed'),
    (9, '2025-06-22', 'cancelled'),
    (26, '2025-06-29', 'completed'),
    (12, '2025-07-05', 'completed'),
    (23, '2025-07-11', 'returned'),
    (15, '2025-07-17', 'completed'),
    (20, '2025-07-23', 'completed'),
    (1, '2025-07-29', 'completed'),
    (6, '2025-08-04', 'completed'),
    (14, '2025-08-10', 'completed'),
    (28, '2025-08-16', 'returned'),
    (3, '2025-08-22', 'completed'),
    (11, '2025-08-28', 'completed'),
    (25, '2025-09-03', 'completed'),
    (17, '2025-09-09', 'cancelled'),
    (30, '2025-09-15', 'completed'),
    (8, '2025-09-21', 'completed'),
    (19, '2025-09-27', 'completed'),
    (2, '2025-10-03', 'returned'),
    (24, '2025-10-09', 'completed'),
    (5, '2025-10-15', 'completed'),
    (13, '2025-10-21', 'completed'),
    (27, '2025-10-27', 'completed'),
    (16, '2025-11-02', 'completed'),
    (7, '2025-11-08', 'cancelled'),
    (21, '2025-11-14', 'completed'),
    (4, '2025-11-20', 'completed'),
    (18, '2025-11-26', 'returned'),
    (9, '2025-12-02', 'completed'),
    (26, '2025-12-08', 'completed'),
    (12, '2025-12-14', 'completed'),
    (23, '2025-12-20', 'completed'),
    (15, '2025-12-26', 'cancelled'),
    (20, '2025-12-30', 'completed'),
    (29, '2026-01-03', 'completed'),
    (10, '2026-01-09', 'returned'),
    (22, '2026-01-15', 'completed'),
    (3, '2026-01-21', 'completed'),
    (28, '2026-01-27', 'completed'),
    (1, '2026-02-02', 'completed'),
    (17, '2026-02-08', 'completed'),
    (25, '2026-02-14', 'cancelled'),
    (6, '2026-02-20', 'completed'),
    (14, '2026-02-26', 'returned'),
    (30, '2026-03-04', 'completed'),
    (8, '2026-03-10', 'completed'),
    (19, '2026-03-16', 'completed'),
    (2, '2026-03-22', 'completed'),
    (11, '2026-03-28', 'completed'),
    (24, '2026-04-03', 'returned'),
    (5, '2026-04-09', 'completed'),
    (13, '2026-04-15', 'completed'),
    (27, '2026-04-21', 'completed'),
    (16, '2026-04-27', 'cancelled'),
    (7, '2026-05-03', 'completed'),
    (21, '2026-05-09', 'completed'),
    (4, '2026-05-15', 'returned'),
    (18, '2026-05-21', 'completed'),
    (9, '2026-05-27', 'completed'),
    (26, '2026-06-02', 'completed'),
    (12, '2026-06-05', 'completed'),
    (23, '2026-06-08', 'cancelled'),
    (15, '2026-06-11', 'completed'),
    (20, '2026-06-14', 'completed'),
    (29, '2026-06-16', 'returned'),
    (11, '2026-06-20', 'returned'),
    (1, '2026-06-26', 'completed'),
    (30, '2026-06-28', 'completed'),
    (6, '2026-06-28', 'completed'),
    (24, '2026-07-01', 'completed'),
    (7, '2025-01-20', 'completed'),
    (15, '2025-02-05', 'completed'),
    (20, '2025-02-15', 'returned'),
    (4, '2025-02-22', 'completed'),
    (18, '2025-03-05', 'completed'),
    (26, '2025-03-12', 'completed'),
    (12, '2025-03-18', 'completed'),
    (23, '2025-03-24', 'cancelled'),
    (15, '2025-04-01', 'completed'),
    (20, '2025-04-12', 'completed'),
    (29, '2025-04-18', 'completed'),
    (10, '2025-04-25', 'returned'),
    (22, '2025-05-01', 'completed'),
    (3, '2025-05-07', 'completed'),
    (28, '2025-05-13', 'completed'),
    (1, '2025-05-19', 'completed'),
    (17, '2025-05-25', 'cancelled'),
    (25, '2025-06-01', 'completed'),
    (6, '2025-06-07', 'completed'),
    (14, '2025-06-13', 'returned'),
    (30, '2025-06-19', 'completed'),
    (8, '2025-06-25', 'completed'),
    (19, '2025-07-01', 'completed'),
    (2, '2025-07-07', 'completed'),
    (11, '2025-07-13', 'completed'),
    (24, '2025-07-19', 'returned'),
    (5, '2025-07-25', 'completed'),
    (13, '2025-08-01', 'completed'),
    (27, '2025-08-07', 'cancelled'),
    (16, '2025-08-13', 'completed'),
    (7, '2025-08-19', 'completed'),
    (21, '2025-08-25', 'completed'),
    (4, '2025-09-01', 'returned'),
    (18, '2025-09-07', 'completed'),
    (9, '2025-09-13', 'completed'),
    (26, '2025-09-19', 'completed'),
    (12, '2025-09-25', 'completed'),
    (23, '2025-10-01', 'completed'),
    (15, '2025-10-07', 'cancelled'),
    (20, '2025-10-13', 'completed'),
    (29, '2025-10-19', 'completed'),
    (10, '2025-10-25', 'returned'),
    (22, '2025-11-01', 'completed'),
    (3, '2025-11-07', 'completed'),
    (28, '2025-11-13', 'completed'),
    (1, '2025-11-19', 'completed'),
    (17, '2025-11-25', 'completed'),
    (25, '2025-12-01', 'cancelled'),
    (6, '2025-12-07', 'completed'),
    (14, '2025-12-13', 'completed'),
    (30, '2025-12-19', 'returned'),
    (8, '2025-12-25', 'completed'),
    (19, '2025-12-31', 'completed'),
    (2, '2026-01-07', 'completed'),
    (11, '2026-01-13', 'completed'),
    (24, '2026-01-19', 'cancelled'),
    (5, '2026-01-25', 'completed'),
    (13, '2026-01-31', 'returned'),
    (27, '2026-02-06', 'completed'),
    (16, '2026-02-12', 'completed'),
    (7, '2026-02-18', 'completed'),
    (21, '2026-02-24', 'completed'),
    (4, '2026-03-02', 'cancelled'),
    (18, '2026-03-08', 'completed'),
    (9, '2026-03-14', 'returned'),
    (26, '2026-03-20', 'completed'),
    (12, '2026-03-26', 'completed'),
    (23, '2026-04-01', 'completed'),
    (15, '2026-04-07', 'completed'),
    (20, '2026-04-13', 'returned'),
    (29, '2026-04-19', 'completed'),
    (10, '2026-04-25', 'completed'),
    (22, '2026-05-01', 'cancelled'),
    (3, '2026-05-07', 'completed'),
    (28, '2026-05-13', 'completed'),
    (1, '2026-05-19', 'returned'),
    (17, '2026-05-25', 'completed'),
    (25, '2026-06-01', 'completed'),
    (6, '2026-06-07', 'completed'),
    (14, '2026-06-13', 'completed'),
    (30, '2026-06-19', 'returned'),
    (8, '2026-06-25', 'completed');



INSERT INTO order_items (order_id, product_id, quantity, unit_price)
SELECT
    o.id AS order_id,
    selected.id AS product_id,
    FLOOR(RANDOM() * 5 + 1)::INTEGER AS quantity,
    selected.price AS unit_price
FROM orders o
CROSS JOIN LATERAL (
    SELECT id, price
    FROM products
    ORDER BY RANDOM()
    LIMIT FLOOR(RANDOM() * 2 + 2)::INTEGER
) selected;


SELECT * FROM regions;
SELECT * FROM customers;
SELECT * FROM products;
SELECT * FROM orders;
SELECT * from order_items;


SELECT order_id, SUM(quantity * unit_price) AS order_total
FROM order_items
GROUP BY order_id
LIMIT 10;


SELECT r.name, SUM(oi.quantity * oi.unit_price) AS total_revenue
FROM regions r
JOIN customers c ON c.region_id = r.id
JOIN orders o ON o.customer_id = c.id
JOIN order_items oi ON oi.order_id = o.id
WHERE o.status = 'completed'
GROUP BY r.name
ORDER BY total_revenue DESC;

SELECT DATE_TRUNC('month', order_date) AS month, COUNT(*) AS order_count
FROM orders
GROUP BY month
ORDER BY month;