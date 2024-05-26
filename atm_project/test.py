import random
import mysql.connector


names = [
    "John", "Jane", "Michael", "Emily", "Daniel", "Olivia", "David", "Sophia", "James", "Isabella",
    "Robert", "Mia", "Mary", "Amelia", "William", "Charlotte", "Joseph", "Harper", "Charles", "Evelyn",
    "Thomas", "Abigail", "Henry", "Ella", "Samuel", "Scarlett", "Christopher", "Avery", "George", "Grace",
    "Anthony", "Chloe", "Andrew", "Victoria", "Joshua", "Lily", "Jonathan", "Hannah", "Matthew", "Aria",
    "Ryan", "Sofia", "Elijah", "Zoe", "Alexander", "Layla", "Benjamin", "Riley", "Nathan", "Nora"
]

surnames = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin",
    "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson",
    "Walker", "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores",
    "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell", "Carter", "Roberts"
]

prefixes = ["4169", "5669", "7664", "9889"]

cardnums = [random.choice(prefixes) + ''.join([str(random.randint(0, 9)) for _ in range(12)]) for _ in range(50)]
pins = [f"{random.randint(1000, 9999):04d}" for _ in range(50)]
balances = [random.randint(100, 99999) for _ in range(50)]







# Establish a connection to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sAlam123m#m",
    database="atm"
)

cursor = conn.cursor()

# SQL query to insert data
sql = "INSERT INTO people (Name, Surname, cardnum, pin, balance) VALUES (%s, %s, %s, %s, %s)"

# Data to be inserted
data = list(zip(names, surnames, cardnums, pins, balances))

# Execute the query for each record
for record in data:
    cursor.execute(sql, record)

# Commit the transaction
conn.commit()

# Close the connection
cursor.close()
conn.close()

print("Data inserted successfully.")


