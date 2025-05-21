import mysql.connector
from dotenv import load_dotenv
import os

# Load variables from .env file into environment
load_dotenv()

# Fetch credentials from environment variables
config = {
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME')
}

# Anslut till databasen
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Skapa tabellen för produkter i kylen
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    weight_grams INT NOT NULL,
    calories_per_100g INT NOT NULL,
    protein_per_100g FLOAT NOT NULL,
    expiration_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

# Skapa tabellen för recept
cursor.execute("""
CREATE TABLE IF NOT EXISTS recipes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);
""")

# Kopplingstabell mellan recept och ingredienser
cursor.execute("""
CREATE TABLE IF NOT EXISTS recipe_ingredients (
    recipe_id INT,
    product_name VARCHAR(255),
    required_grams INT,
    PRIMARY KEY (recipe_id, product_name),
    FOREIGN KEY (recipe_id) REFERENCES recipes(id) ON DELETE CASCADE
);
""")

# Valfri tabell för inköpslista
cursor.execute("""
CREATE TABLE IF NOT EXISTS shopping_list (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    needed_grams INT NOT NULL,
    added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

conn.commit()
cursor.close()
conn.close()

print("MySQL-databasen 'fridge' är klar med alla tabeller.")

