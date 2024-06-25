import MySQLdb

# Database connection settings
db_settings = {
    'host': '35.238.101.214',
    'user': 'Pintu SHakya',
    'password': 'Shambhu@123',
    'database': 'data',
    'port': 3306,
}

try:
    connection = MySQLdb.connect(**db_settings)
    print("Connection successful!")
    connection.close()
except MySQLdb.OperationalError as e:
    print(f"Error: {e}")
