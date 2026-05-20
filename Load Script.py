# Import berbagai library yang digunakan untuk membangun pipeline data
import pandas as pd
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
import bcrypt
from pyspark.sql import SparkSession

# Inisialisasi Spark
spark = SparkSession.builder \
    .appName("ReadParquet") \
    .getOrCreate()

# Mendefinisikan connection string (URI) untuk menghubungkan aplikasi ke MongoDB Atlas
URI_ATLAS = "mongodb+srv://development:development@cluster0.nvsap4g.mongodb.net/?appName=Cluster0"

try:
    client = MongoClient(
        URI_ATLAS,
        server_api=ServerApi(version="1", strict=True, deprecation_errors=True),
    )
except Exception as e:
    print("Error:", e)

# Untuk melihat database apa saja yang ada di MongoDB kita
client.list_database_names()

# Membaca file Parquet hasil data cleaning ke dalam DataFrame PySpark
df = spark.read.parquet('clean_amazon')

# Mengubah DataFrame PySpark menjadi list of dictionary (format Python)
list_data = [row.asDict() for row in df.collect()]

# Memilih database bernama "Milestone_3" di MongoDB
selected_db = client["Milestone_3"]
# Memilih collection bernama "M3" di dalam database tersebut
selected_collection = selected_db["M3"]

# Melakukan insert banyak data sekaligus ke MongoDB (bulk insert)
result = selected_collection.insert_many(list_data)

# Menampilkan status apakah proses insert berhasil atau tidak (True/False)
print(f"Berhasil menambahkan data? {result.acknowledged}")
# Menampilkan jumlah data yang berhasil dimasukkan ke MongoDB
print(f"Jumlah data yang bertambah: {len(result.inserted_ids)}")