import pandas as pd
import random
from datetime import datetime, timedelta

# Simulate data
currencies = ["USD", "EUR", "SGD", "JPY", "GBP"]
payment_methods = ["Credit Card", "PayPal", "Bank Transfer"]
statuses = ["Completed", "Pending", "Failed"]

data = []
for _ in range(1000):
    transaction = {
        "transaction_id": random.randint(100000, 999999),
        "timestamp": datetime.now() - timedelta(days=random.randint(1, 30)),
        "amount": round(random.uniform(10, 1000), 2),
        "currency": random.choice(currencies),
        "payment_method": random.choice(payment_methods),
        "status": random.choice(statuses),
    }
    data.append(transaction)

df = pd.DataFrame(data)
df.to_csv("transactions.csv", index=False)
