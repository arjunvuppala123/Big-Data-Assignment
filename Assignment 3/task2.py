import sys
from pyspark import SparkContext
from pyspark.sql import SQLContext
import pyspark.sql.functions as F
from pyspark.sql.types import FloatType

sc=SparkContext.getOrCreate()

sql_context=SQLContext(sc)

city_path = sys.argv[1]
global_path = sys.argv[2]

df_city = sql_context.read.csv(city_path, header=True)
df_global  = sql_context.read.csv(global_path, header=True)

df_global = df_global.withColumn('LandAverageTemperature',df_global['LandAverageTemperature'].cast(FloatType()))
df_city = df_city.withColumn('AverageTemperature',df_city['AverageTemperature'].cast(FloatType()))

new_df = df_city.join(df_global,df_city.dt == df_global.dt,"inner").drop(df_city.dt)

#new_df.AverageTemperature = new_df.AverageTemperature.cast(FloatType())
#new_df.LandAverageTemperature = new_df.LandAverageTemperature.cast(FloatType())

new_df = new_df.filter(F.col("AverageTemperature") > F.col("LandAverageTemperature"))
new_df = new_df.groupBy(new_df.dt, new_df.Country).agg({"AverageTemperature": "max"})
new_df = new_df.groupBy(new_df.Country).agg({"Country" : "count"}).collect()

res = {}

for i in range(len(new_df)):
	res[new_df[i][0]] = new_df[i][1]

res = dict(sorted(res.items()))

for key in res:
	print(key,'\t',res[key])
