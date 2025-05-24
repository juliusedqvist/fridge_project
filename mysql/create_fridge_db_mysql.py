import mysql.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch credentials from environment variables
config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME')
}

# Connect to the database
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Drop tables if they exist (order matters because of foreign keys)
drop_tables = [
    "DROP TABLE IF EXISTS Recipe_Item;",
    "DROP TABLE IF EXISTS Meal_Prep_Recipe;",
    "DROP TABLE IF EXISTS Food_Item;",
    "DROP TABLE IF EXISTS Recipe;",
    "DROP TABLE IF EXISTS Meal_Prep;"
]

for stmt in drop_tables:
    cursor.execute(stmt)

# Create tables
cursor.execute("""
CREATE TABLE Food_Item (
    Food_Id INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Weight FLOAT NOT NULL,
    KcalPer100g FLOAT NOT NULL,
    ProteinPer100g FLOAT NOT NULL,
    Exp_Date DATE NOT NULL,
    State VARCHAR(50) NOT NULL DEFAULT 'available'
);
""")

cursor.execute("""
CREATE TABLE Recipe (
    Recipe_Id INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE Recipe_Item (
    Food_Id INT,
    Recipe_Id INT,
    QuantityInGrams FLOAT NOT NULL,
    PRIMARY KEY (Food_Id, Recipe_Id),
    FOREIGN KEY (Food_Id) REFERENCES Food_Item(Food_Id),
    FOREIGN KEY (Recipe_Id) REFERENCES Recipe(Recipe_Id)
);
""")

cursor.execute("""
CREATE TABLE Meal_Prep (
    Meal_Prep_Id INT PRIMARY KEY AUTO_INCREMENT,
    Count INT NOT NULL,
    Total_Kcal FLOAT,
    Total_Protein FLOAT,
    Food_Weight FLOAT,
    Created_At TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
""")

cursor.execute("""
CREATE TABLE Meal_Prep_Recipe (
    Meal_Prep_Id INT,
    Recipe_Id INT,
    Portions INT NOT NULL,
    PRIMARY KEY (Meal_Prep_Id, Recipe_Id),
    FOREIGN KEY (Meal_Prep_Id) REFERENCES Meal_Prep(Meal_Prep_Id),
    FOREIGN KEY (Recipe_Id) REFERENCES Recipe(Recipe_Id)
);
""")

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

print("MySQL database is ready with all tables.")

