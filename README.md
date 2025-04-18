# 🇺🇸 Border Crossing Data ETL Pipeline with Kestra

An end-to-end **ETL data pipeline** that extracts U.S. Border Crossing Entry Data, performs advanced transformation and feature engineering, loads it into a **MySQL** database, and visualizes key insights using **Power BI / Looker Studio**. Orchestrated using **Kestra**.

---

## 🚀 Project Architecture


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
<img src="https://github.com/yourusername/yourrepo/blob/main/screenshots/monthly_trend.png" width="500"/> <img src="https://github.com/yourusername/yourrepo/blob/main/screenshots/traffic_levels.png" width="500"/>

---

Let me know:
- If you want this customized for **Looker Studio only**
- Want me to generate badge icons (like GitHub stars, license, etc.)
- Or want the actual `.md` file to download directly

Would you like a sample diagram image for the architecture too?
