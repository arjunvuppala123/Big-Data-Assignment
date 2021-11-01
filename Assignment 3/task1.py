import sys
from pyspark import SparkContext
from pyspark.sql import SQLContext
import pyspark.sql.functions as F

sc=SparkContext.getOrCreate()

sql_context=SQLContext(sc)

df_path=sys.argv[2]
country=sys.argv[1]

df = sql_context.read.csv(df_path, header=True)

df = df.filter(df.Country==country) 

city_avg = df.groupBy(df.City).agg({"AverageTemperature": "avg"})
new_df = df.join(city_avg,df.City == city_avg.City,"inner").drop(df.City)

grouped_data = new_df.filter(F.col("AverageTemperature") > F.col("avg(AverageTemperature)")).groupBy(new_df.City).count().collect()

#city = []
#average = []

res = {}

for i in range(len(grouped_data)):
	res[grouped_data[i][0]] = grouped_data[i][1]

res = dict(sorted(res.items()))

for key in res:
	print(key,'\t',res[key])





