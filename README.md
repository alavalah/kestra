# 🇺🇸 Border Crossing Data ETL Pipeline with Kestra

An end-to-end **ETL data pipeline** that extracts U.S. Border Crossing Entry Data, performs advanced transformation and feature engineering, loads it into a **MySQL** database, and visualizes key insights using **Power BI / Looker Studio**. Orchestrated using **Kestra**.

---
---

## 🧰 Tech Stack

| Component      | Tool / Library                             |
|----------------|---------------------------------------------|
| Orchestration  | [Kestra](https://kestra.io/)                |
| Language       | Python 3.10                                 |
| Libraries      | pandas, numpy, geopandas, scikit-learn, shapely, sqlalchemy, pymysql |
| Database       | MySQL 8.0                                   |
| Visualization  | Power BI / Google Looker Studio             |

---

## 📊 Dataset

- **Source**: [Border Crossing Entry Data](https://raw.githubusercontent.com/codewithharsha/ETL-Pipeline/main/Border_Crossing_Entry_Data.csv)
- **Description**: Tracks the number of people/vehicles entering the U.S. by port, date, and measure.

---

## 🔁 Workflow Breakdown

### 1️⃣ Extract (Python)
- Downloads CSV from public GitHub URL
- Saves raw dataset locally

### 2️⃣ Transform (Python)
- Cleans missing values, removes duplicates
- Converts date/time formats
- Adds features: `Season`, `Year`, `Month`, `Traffic_Level`
- Normalizes values using `MinMaxScaler`
- Converts WKT `Point` data into geometry for geospatial insights

### 3️⃣ Load (Python + SQLAlchemy)
- Loads transformed data into a MySQL table (`border_crossing_data`)
- Uses chunked insert for large dataset handling

### 4️⃣ Visualization
- Data connected live to Power BI or Looker Studio
- Key dashboards:
  - Monthly crossing trends
  - Traffic level breakdown
  - Top ports by volume
  - Seasonal patterns

---

## ⚙️ Running the Pipeline

### 1. Spin up MySQL with Docker
```bash
docker run --name mysql-etl \
  -e MYSQL_ROOT_PASSWORD=your_password \
  -e MYSQL_DATABASE=etl_pipeline \
  -p 3306:3306 \
  -d mysql:8.0
docker-compose up -d  # Inside the Kestra project folder
```
## Output Images

<img src="https://github.com/alavalah/kestra/blob/main/Kestra%20etl.png?raw=true" width="500"/>
<img src="https://github.com/alavalah/kestra/blob/main/Kestra%20logs.png?raw=true" width="500"/>
<img src="https://github.com/alavalah/kestra/blob/main/Kestra%20ouput%20logs.png?raw=true" width="500"/>
<img src="https://github.com/alavalah/kestra/blob/main/Broder%20crossing%20data%20visualization.png?raw=true" width="500"/>
