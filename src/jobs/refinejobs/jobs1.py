import sys
import os

print("Before Append:", sys.path)

sys.path.append(os.path.join(os.getcwd(), 'utils'))

print("After Append:", sys.path)

from utils.vaultUtils import VaultClient
from utils.snowUtils import SnowflakeConnector

VAULT_URL = "http://127.0.0.1:8200"
ROLE_ID = "6481799b-8226-29fd-ab1b-49e5f4d638cc"
SECRET_ID = "66ab291e-1482-9f09-f53a-583b0e881f87"
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
query_result = snowflake_conn.execute_query("SELECT * FROM MYDB.public.customer")

# # Print the result
print("Current Date in Snowflake:", query_result[0][0])


for row in query_result:
    print(row)

# # Close the connection
snowflake_conn.close_connection()



# project_root/
#     |- config/
#     |   |- credentials.json
#     |- src/
#         |- __init__.py
#         |- refinejobs/
#         |- job.py


