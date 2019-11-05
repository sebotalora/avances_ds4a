import psycopg2
import pandas as pd
engine = psycopg2.connect(
    database="nps_demo_db",
    user="postgres",
    password="pVPwCaO9cPry8FhoKA3K",
    host="nps-demo-instance.c3vr5hpxc4co.us-east-2.rds.amazonaws.com",
    port='5432'
)
df = pd.read_sql_query('select * from customer limit 100',con=engine)
print(df)