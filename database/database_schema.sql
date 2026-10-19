CREATE DATABASE smart_expense_db;

USE smart_expense_db;

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    age INT,
    city VARCHAR(50)
);

CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    transaction_date DATE,
    category VARCHAR(50),
    amount DECIMAL(10,2),
    description VARCHAR(255),
    FOREIGN KEY (user_id)
    REFERENCES users(user_id)
);
