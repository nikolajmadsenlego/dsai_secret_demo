# COMMAND ----------
# MAGIC %md
# MAGIC # Databricks Example
# MAGIC

# COMMAND ----------
dbutils.secrets.get(scope = "example", key = "example")