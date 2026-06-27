from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, isnan, count
from pyspark.ml.feature import StringIndexer, OneHotEncoder, VectorAssembler, StandardScaler
from pyspark.ml import Pipeline

# -----------------------------------
# 1. Create Spark Session
# -----------------------------------
spark = SparkSession.builder \
    .appName("Data Preprocessing Pipeline") \
    .getOrCreate()

# -----------------------------------
# 2. Load Dataset
# -----------------------------------
df = spark.read.csv("data.csv", header=True, inferSchema=True)

print("Initial Data:")
df.show()

# -----------------------------------
# 3. Handle Missing Values
# -----------------------------------
# Count nulls
print("Missing Values Count:")
df.select([count(when(col(c).isNull(), c)).alias(c) for c in df.columns]).show()

# Fill missing values
df = df.fillna({
    "Age": df.selectExpr("avg(Age)").first()[0],
    "Salary": df.selectExpr("avg(Salary)").first()[0],
    "Gender": "Unknown"
})

# -----------------------------------
# 4. Remove Duplicates
# -----------------------------------
df = df.dropDuplicates()

# -----------------------------------
# 5. Feature Engineering
# -----------------------------------
# Example: Create new feature
df = df.withColumn("Salary_Age_Ratio", col("Salary") / col("Age"))

# 6. Encode Categorical Data
indexer = StringIndexer(inputCol="Gender", outputCol="Gender_Index")
encoder = OneHotEncoder(inputCol="Gender_Index", outputCol="Gender_Encoded")

assembler = VectorAssembler(
    inputCols=["Age", "Salary", "Salary_Age_Ratio"],
    outputCol="Features"
)

#
scaler = StandardScaler(
    inputCol="Features",
    outputCol="Scaled_Features",
    withStd=True,
    withMean=True
)

# 8. Build Pipeline
pipeline = Pipeline(stages=[
    indexer,
    encoder,
    assembler,
    scaler
])

model = pipeline.fit(df)
processed_df = model.transform(df)

# 9. Final Output
print("Processed Data:")
processed_df.select("Scaled_Features", "Gender_Encoded").show(truncate=False)

# 10. Save Processed Data
processed_df.write.mode("overwrite").parquet("processed_data")

# Stop Spark
spark.stop()


# CSV → Clean → Remove duplicates → Create features → Encode → Scale → Save