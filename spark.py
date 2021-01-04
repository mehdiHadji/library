"""
Concatenate two columns in pyspark with single space
"""


from pyspark.sql.functions import concat, lit, col


df = df.select("*", concat(col("first_name"),lit(" "),col("last_name")).alias("full_name"))


"""
Concatenate two columns in pyspark without space 
"""


df = df.select("*", concat(col("first_name"),col("last_name")).alias("full_name"))


"""
Count of the distinct values: 
"""

df.select(F.countDistinct("colName")).show()


"""
Count occurences of each distinct value in a given column
"""

df.groupBy('colName').count().show()


"""
Count occurences of each distinct value in a given column, ordered by descending
"""

df.groupBy('colName').count().orderBy('count', ascending=False).show()


"""
Select data from dataframe with (current_date - a given number of days i.e 366)
"""

df = df.filter(df.date_col > date_sub(current_date(), 366))
