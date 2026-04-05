# Se asumen que las dependencias necesarias para PySpark ya están instaladas y configuradas.
from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder \
    .appName('Negocio') \
    .getOrCreate()

# Formato de lectura de datos desde PostgreSQL (se asume que la BDD es Postgres) utilizando JDBC
df = spark.read.format('jdbc') \
    .option('url', 'jdbc:postgresql://localhost:5432/db_name') \
    .option('dbtable', 'fact_usage') \
    .option('user', db_user) \
    .option('password', db_password) \
    .option("driver", jdbc_driver) \
    .load()

df_plans = spark.read.format('jdbc') \
    .option('url', 'jdbc:postgresql://localhost:5432/db_name') \
    .option('dbtable', 'dim_plan') \
    .option('user', db_user) \
    .option('password', db_password) \
    .option("driver", jdbc_driver) \
    .load()

df_date = spark.read.format('jdbc') \
    .option('url', 'jdbc:postgresql://localhost:5432/db_name') \
    .option('dbtable', 'dim_date') \
    .option('user', db_user) \
    .option('password', db_password) \
    .option("driver", jdbc_driver) \
    .load()

result = df \
    .join(df_plans, "plan_id") \
    .join(df_date, "usage_date") \
    .filter(F.year(F.col("date")) == 2025) \
    .groupBy("plan_name") \
    .agg(F.avg("revenue").alias("avg_revenue"))