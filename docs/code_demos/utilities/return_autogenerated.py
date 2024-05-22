"""ETL Helper script to demonstrate autogenerated field values being returned."""
import etlhelper as etl
from my_databases import POSTGRESDB

insert_sql = "INSERT INTO my_table (message) VALUES ('hello') RETURNING id"

with POSTGRESDB.connect("PGPASSWORD") as conn:
    result = etl.fetchone(insert_sql, conn)

print(result["id"])
