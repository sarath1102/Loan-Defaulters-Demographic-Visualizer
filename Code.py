from pyspark.sql import SparkSession
from pyspark.sql.functions import col, abs, floor

# Initialize a Spark session
spark = SparkSession.builder.appName("SelectColumns").getOrCreate()

# S3 input and output paths
input_s3_path = "s3://cloud-assignment-2023/application_data.csv"
output_s3_path = "s3://cloud-assignment-2023/application_data_inc_null"
output_s3_path2 = "s3://cloud-assignment-2023/application_data_nonull"
output_s3_path3 = "s3://cloud-assignment-2023/application_data_nonull_and_eliminated_outliers"

# Define columns to select
columns_to_select = ["SK_ID_CURR", "TARGET", "NAME_CONTRACT_TYPE","CODE_GENDER","AMT_INCOME_TOTAL","AMT_CREDIT","AMT_ANNUITY","NAME_INCOME_TYPE","NAME_EDUCATION_TYPE","DAYS_BIRTH","OCCUPATION_TYPE"]

# Read the CSV file into a DataFrame
df = spark.read.csv(input_s3_path, header=True, inferSchema=True)

# Select only the specified columns
selected_df = df.select(columns_to_select)


df_modified = selected_df.withColumn("DAYS_BIRTH", floor(abs(col("DAYS_BIRTH") / 365)))

df_filtered = df_modified.filter(df["TARGET"] == 1)



#df_copy = df_filtered.withColumn("AMT_INCOME_TOTAL_DUP", col("AMT_INCOME_TOTAL"))

# Write the result to a new CSV file in the same S3 bucket
#df_copy.coalesce(1).write.csv(output_s3_path, header=True, mode="overwrite")



df_no_null = df_filtered.na.drop()

df_filtered_no_null = df_no_null.filter(col("AMT_INCOME_TOTAL") < 336825)
df_filtered_no_null.coalesce(1).write.csv(output_s3_path3, header=True, mode="overwrite")

# Stop the Spark session
spark.stop()
