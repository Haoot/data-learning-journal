from pyspark.sql import SparkSession  # ✅ from, sql, SparkSession

# 创建SparkSession（本地模式）
spark = (SparkSession.builder
         .appName("Day2_Local_Spark")
         .config("spark.master", "local[*]")
         .getOrCreate())

# 读取CSV（本地文件）
df = spark.read.csv('data/random_users.csv', header=True, inferSchema=True)
# 注册为临时表
df.createOrReplaceTempView("users")
# 运行Spark SQL
result = spark.sql("SELECT city, COUNT(*) as user_count FROM users GROUP BY city")
result.show()
# 停止Spark
spark.stop()