from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split

import os
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.0-preview2 pyspark-shell'

spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()


lines = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "temperaturas") \
    .option("startingOffsets", "latest") \
    .load()
lines.printSchema()

# separar por linhas
words = lines.select(
   explode(
       split(lines.value, " ")
   ).alias("word")
)


wordCounts = words.groupBy("word").count()


query = wordCounts \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()