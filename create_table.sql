-- drop table transactions;

CREATE table if not exists transactions (
    transaction_id INT PRIMARY KEY,
    timestamp TIMESTAMP,
    amount FLOAT,
    currency VARCHAR(10),
    payment_method VARCHAR(20),
    status VARCHAR(10)
);
