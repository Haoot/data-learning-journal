import os
os.environ['HADOOP_HOME'] = 'C:\\hadoop-3.0.0'
import pandas as pd
import time
from pyspark.sql import SparkSession

# 读取昨天的100行CSV
csv_path = 'data/random_users.csv'

# Pandas处理100行
start = time.time()
pdf = pd.read_csv(csv_path)
result_pd = pdf.groupby('city').count()
print("Pandas结果:")
print(result_pd)
print(f"Pandas耗时: {time.time() - start:.4f} 秒\n")

# Spark处理100行
spark = SparkSession.builder.appName("Local_VS_Pandas").master("local[*]").getOrCreate()
start = time.time()
df = spark.read.csv(csv_path, header=True, inferSchema=True)
df.createOrReplaceTempView("users")
result_spark = spark.sql("SELECT city, COUNT(*) FROM users GROUP BY city")
print("Spark结果:")
result_spark.show()
print(f"Spark耗时: {time.time() - start:.4f} 秒")
spark.stop()
