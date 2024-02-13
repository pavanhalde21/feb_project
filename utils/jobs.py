
from snowUtils import SnowflakeConnector
from vaultUtils import VaultClient


VAULT_URL = "http://127.0.0.1:8200"
ROLE_ID = "8dc93e37-1c57-30e2-bb22-990cd1305732"
SECRET_ID = "7cd2c91b-f74d-b651-7671-de342b790454"
SECRET_PATH = "secret/data/snowflake"

vault_client = VaultClient(VAULT_URL, ROLE_ID, SECRET_ID, SECRET_PATH)

token = vault_client.authenticate_with_approle()


if token:
    secret_data = vault_client.get_secret(token)

    if secret_data:
        print("Secret data:", secret_data)
    else:
        print("Failed to retrieve secret.")
else:
    print("Failed to authenticate with AppRole.")



# Replace these with your Snowflake account details
account = secret_data['data']['account']
username = secret_data['data']['username']
password = secret_data['data']['password']
warehouse = 'COMPUTE_WH'
database = 'MYDB'
schema = 'PUBLIC'

# # Create an instance of SnowflakeConnector
snowflake_conn = SnowflakeConnector(account, username, password, warehouse, database, schema)

# # Connect to Snowflake
snowflake_conn.connect()

# # Execute a query
query_result = snowflake_conn.execute_query("SELECT * FROM MYDB.public.customer_data1")

# # Print the result
print("Current Date in Snowflake:", query_result[0][0])

# # Close the connection
snowflake_conn.close_connection()



# project_root/
#     |- config/
#     |   |- credentials.json
#     |- src/
#         |- jobs/
#         |- __init__.py
#           |- refinejobs/
#               |- job.py


