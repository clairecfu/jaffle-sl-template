import snowflake.connector

conn = snowflake.connector.connect(
    user='epd_user',
    password='RM7VsbPzdPMc-hRp-@8W',
    account='co24109.us-east-2.aws',
    warehouse='epd_developing',
    database='analytics',
    schema='jaffle_shop'
)

try:
    # Test the connection by querying Snowflake
    cursor = conn.cursor()
    cursor.execute("SELECT CURRENT_VERSION()")
    result = cursor.fetchone()
    print(f"Connection successful. Snowflake version: {result[0]}")
finally:
    conn.close()
