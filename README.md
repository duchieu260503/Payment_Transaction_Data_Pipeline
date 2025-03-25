# Payment Transaction Data Pipeline

## 📌 Project Overview
This project is an **ETL (Extract, Transform, Load) pipeline** for processing **payment transaction data** using **Apache Airflow**, **Docker**, and **PostgreSQL**. The pipeline performs the following steps:
1. **Extract:** Reads raw transaction data from a CSV file.
2. **Transform:** Applies data transformations (e.g., currency conversion, filtering, and cleaning).
3. **Load:** Inserts the processed data into a PostgreSQL database.

---

## 🚀 Project Setup

### **1️⃣ Prerequisites**
Ensure you have the following installed on your local machine:
- **Docker & Docker Compose** → [Install Docker](https://docs.docker.com/get-docker/)
- **WSL2 (For Windows users)** → [Install WSL2](https://learn.microsoft.com/en-us/windows/wsl/install)
- **PostgreSQL (Running Locally or in Docker)** → [Install PostgreSQL](https://www.postgresql.org/download/)

### **2️⃣ Project Structure**
Ensure your local directory follows this structure:
```
Payment_Transaction_Data_Pipeline/
│── dags/                          # DAGs folder (contains Python DAG scripts)
│   ├── payment_etl.py             # Your DAG script
│── data/                          # Folder to store CSV files
│   ├── transactions.csv           # Raw transaction data
│   ├── extracted.csv              # Extracted data (after extract step)
│   ├── transformed.csv            # Transformed data (after transform step)
│── logs/                          # Airflow logs
│── plugins/                       # Custom Airflow plugins (if needed)
│── docker-compose.yml             # Docker Compose config file
│── requirements.txt               # Python dependencies (optional)
│── README.md                      # Project documentation
```

### **3️⃣ Setup Docker & Airflow**

#### **📌 Step 1: Modify `docker-compose.yml`**
Ensure `docker-compose.yml` has the correct volume mounts for **DAGs and data**:
```yaml
services:
  airflow_scheduler:
    volumes:
      - ./dags:/opt/airflow/dags
      - ./data:/opt/airflow/data
  airflow_webserver:
    volumes:
      - ./dags:/opt/airflow/dags
      - ./data:/opt/airflow/data
```

#### **📌 Step 2: Start Docker Containers**
Run the following commands to initialize Airflow:
```bash
docker compose down  # Stop any running containers
docker compose up -d  # Start Airflow in detached mode
```
Wait a few minutes for Airflow to initialize.

#### **📌 Step 3: Access Airflow UI**
Open your browser and go to:
```
http://localhost:8080
```
Default credentials:
- **Username:** `airflow`
- **Password:** `airflow`

#### **📌 Step 4: Verify DAGs & Trigger Execution**
Run the following command to check available DAGs:
```bash
docker exec -it airflow_scheduler airflow dags list
```
Trigger the DAG manually:
```bash
docker exec -it airflow_scheduler airflow dags trigger payment_etl
```

#### **📌 Step 5: View Logs**
Check logs for debugging:
```bash
docker exec -it airflow_scheduler airflow tasks logs payment_etl extract
```

---

## 🛠️ PostgreSQL Database Setup
Ensure PostgreSQL is running **locally** or in **Docker**.

### **1️⃣ Running PostgreSQL Locally**
If PostgreSQL is installed on your machine, update your database credentials in `payment_etl.py`:
```python
conn = psycopg2.connect("dbname=postgres user=postgres password=yourpassword host=localhost port=5432")
```

### **2️⃣ Running PostgreSQL in Docker**
Alternatively, you can **run PostgreSQL in Docker**:
```bash
docker run --name postgres-db -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=yourpassword -p 5432:5432 -d postgres
```
Verify the container is running:
```bash
docker ps
```

Create a `transactions` table in PostgreSQL:
```sql
CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    timestamp TIMESTAMP,
    amount FLOAT,
    currency VARCHAR(10),
    payment_method VARCHAR(20),
    status VARCHAR(10)
);
```

---

## 🔄 DAG Execution Steps
1️⃣ **Extract:** Reads raw transactions from `/opt/airflow/data/transactions.csv`.
2️⃣ **Transform:** Applies data transformations and saves the processed file.
3️⃣ **Load:** Inserts the transformed data into **PostgreSQL**.

---

## 🛠️ Debugging
If you run into issues, check logs:
```bash
docker logs airflow_scheduler  # View Airflow logs
docker logs airflow_webserver   # View Webserver logs
docker logs postgres-db         # View PostgreSQL logs
```

If DAGs are not appearing in the UI, restart Airflow:
```bash
docker compose restart
```

---

## 📌 Next Steps
- **Enhance Data Processing** → Add data validation and anomaly detection.
- **Deploy in Cloud** → Run on AWS/GCP with managed Airflow & PostgreSQL.
- **Automate Alerts** → Send Slack/email alerts for failed DAGs.

---

## 🤝 Contributing
Feel free to submit pull requests or open issues!

**Happy Coding! 🚀**
