# from sqlalchemy import create_engine
# from sqlalchemy.exc import SQLAlchemyError
# import pandas as pd

# user = 'root'
# password = '123456'
# host = 'localhost'
# port = '3306'
# database = 'etl_pipeline'

# # Create connection engine
# engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

# try:
#     with engine.connect() as connection:
#         print(" MySQL connection successful!")
#         data = pd.read_csv('processed_border_crossing_data.csv')
#         # Push to MySQL table (creates it if not exists)
#         table_name = 'border_crossing_data'
#         data.to_sql(table_name, con=engine, index=False, if_exists='replace')
#         print("Data Loaded successfully!!")

# except SQLAlchemyError as e:
#     print("MySQL connection failed:")
#     print(str(e))

# import pandas as pd
# from sqlalchemy import create_engine

# df = pd.read_csv("processed_border_crossing_data.csv")
# print("Record count to insert:", len(df))

# engine = create_engine("mysql+pymysql://root:123456@localhost:3306/etl_pipeline")
# df.to_sql("border_crossing_data", con=engine, index=False, if_exists='replace')
# print("Data inserted successfully.")

import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/etl_pipeline")

with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) AS row_count FROM border_crossing_data"))
    row = result.fetchone()
    # print(f"Inserted {row[0]} records into MySQL.")
    print(row[0])
