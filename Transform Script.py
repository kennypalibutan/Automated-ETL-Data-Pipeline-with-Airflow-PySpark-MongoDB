from pyspark.sql import SparkSession #Untuk membuat Spark Session (entry point PySpark)
from pyspark.sql.functions import lower, trim, col #Import fungsi untuk transformasi data

# Inisialisasi Spark
spark = SparkSession.builder \
    .appName("ReadParquet") \
    .getOrCreate() #Membuat atau mengambil Spark session yang sudah ada

#Membaca file Parquet hasil sebelumnya
df = spark.read.parquet('amazon_parquet')

# Membersihkan kolom ProductName:
# - trim(): menghapus spasi di awal & akhir
# - lower(): mengubah semua huruf menjadi lowercase
df = df.withColumn("ProductName", lower(trim(col("ProductName"))))

# Filter data:
# - Mengambil hanya nilai Discount antara 0 (inclusive) dan < 1
df = df.filter((col("Discount") >= 0) & (col("Discount") < 1))

# Filter data:
# - Hanya mengambil OrderStatus yang valid (sesuai list)
df = df.filter(col("OrderStatus").isin(["Returned", "Shipped", "Cancelled", "Delivered", "Pending"]))

# Menghapus data duplikat (berdasarkan semua kolom)
df = df.dropDuplicates()

# Mengubah tipe data kolom OrderDate menjadi timestamp
df = df.withColumn("OrderDate", col("OrderDate").cast("timestamp"))

# Menyimpan hasil data cleaning ke format Parquet
# - overwrite: jika folder sudah ada, akan ditimpa
df.write.mode("overwrite").parquet("clean_amazon")