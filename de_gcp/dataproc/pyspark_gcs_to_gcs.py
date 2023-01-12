from pyspark.sql import SparkSession

spark = SparkSession.builder \
.appName('spark_gcs_to_gcs') \
.getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("WARN")

BUCKET_NAME="joe-test-bucket-737803"
MASTER_NODE_INSTANCE_NAME="joe-dataproc-cluster-m"
files_rdd = sc.textFile(f'gs://{BUCKET_NAME}/csv_files/*.csv')
selected_col_rdd = files_rdd.map(lambda x: x.type in ['Run', 'Ride', 'BackcountrySki'])

columns = ["id","start_date_local","type"]
df = selected_col_rdd.toDF(columns)
df.createOrReplaceTempView('activity_count_df')

sql = """
  SELECT
  id,
  count(*) as count
  FROM activities_df
  WHERE type IN ('Run','Ride','BackcountrySki')
  GROUP BY type
  """
activity_count_df = spark.sql(sql)
activity_count_df.show(5)
activity_count_df.write.save(f'gs://{MASTER_NODE_INSTANCE_NAME}/activity_count_df', format='csv', mode='overwrite')
