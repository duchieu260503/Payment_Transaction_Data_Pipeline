import psycopg2
import pandas as pd

conn = psycopg2.connect("dbname=postgres user=postgres password=1 host=localhost port=5432")
cur = conn.cursor()

df = pd.read_csv("transactions.csv")

for _, row in df.iterrows():
    cur.execute("INSERT INTO transactions VALUES (%s, %s, %s, %s, %s, %s)",
                (row["transaction_id"], row["timestamp"], row["amount"], row["currency"],
                 row["payment_method"], row["status"]))

conn.commit()
cur.close()
conn.close()
