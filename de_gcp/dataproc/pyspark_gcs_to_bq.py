from pyspark.sql import SparkSession

spark = SparkSession.builder \
.appName('spark_gcs_to_bq') \
.getOrCreate()

sc = spark.sparkContext
sc.setLogLevel("WARN")

BUCKET_NAME="joe-test-bucket-737803"
MASTER_NODE_INSTANCE_NAME="joe-dataproc-cluster-m"
files_rdd = sc.textFile(f'gs://{BUCKET_NAME}/csv_files/*')
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

activity_count_df.write.format('bigquery') \
.option('temporaryGcsBucket', BUCKET_NAME) \
.option('table', 'strava.article_count_df') \
.mode('overwrite') \
.save()
