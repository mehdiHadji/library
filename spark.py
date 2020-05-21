"""
Concatenate two columns in pyspark with single space
"""


from pyspark.sql.functions import concat, lit, col


df = df.select("*", concat(col("first_name"),lit(" "),col("last_name")).alias("full_name"))


"""
Concatenate two columns in pyspark without space 
"""


df = df.select("*", concat(col("first_name"),col("last_name")).alias("full_name"))
