import kagglehub #Library untuk download dataset langsung dari Kaggle
import os #Library untuk operasi sistem (path, file, dll)
from pyspark.sql import SparkSession #Untuk membuat session PySpark

#Membuat Spark Session (entry point untuk menggunakan PySpark)
spark = SparkSession.builder \
    .appName("AmazonSalesAnalysis") \
    .getOrCreate() #Membuat atau mengambil session yang sudah ada

#Download dataset dari Kaggle menggunakan kagglehub
path = kagglehub.dataset_download("rohiteng/amazon-sales-dataset")

#Membaca file CSV ke dalam DataFrame PySpark
df = spark.read.csv(
    path + "/Amazon.csv",
    header=True,
    inferSchema=True
)

#Menyimpan DataFrame ke format Parquet
df.write.mode("overwrite").parquet("amazon_parquet")
#mode("overwrite") artinya jika folder sudah ada, akan ditimpa

#Membaca kembali file Parquet ke DataFrame
df = spark.read.parquet('amazon_parquet')
#Biasanya dilakukan karena Parquet lebih cepat untuk diproses dibanding CSV