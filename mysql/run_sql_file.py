import mysql.connector
import sys
import os
from tabulate import tabulate

# ----- KONFIGURATION -----
config = {
    'user': 'fridge',
    'password': 'hallon',
    'host': 'localhost',
    'database': 'fridge_project'
}

def run_sql_file(file_path):
    if not os.path.isfile(file_path):
        print(f"Filen '{file_path}' hittades inte.")
        return

    with open(file_path, 'r') as file:
        sql_commands = file.read()

    # Dela upp SQL-kommandon
    statements = [s.strip() for s in sql_commands.split(';') if s.strip()]

    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        for statement in statements:
            try:
                if statement.lower().startswith("select"):
                    cursor.execute(statement)
                    rows = cursor.fetchall()
                    headers = [i[0] for i in cursor.description]
                    print(tabulate(rows, headers=headers, tablefmt="pretty"))
                else:
                    cursor.execute(statement)
                    print(f"✔️  Utfört: {statement[:60]}...")
            except mysql.connector.Error as err:
                print(f"❌ Fel vid körning av: {statement[:60]}...\n   → {err}")

        conn.commit()
        cursor.close()
        conn.close()
        print("✅ Färdig.")
    except mysql.connector.Error as err:
        print(f"❌ Databasanslutningsfel: {err}")

# ----- HUVUDPROGRAM -----
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Användning: python run_sql_file.py path/to/file.sql")
    else:
        run_sql_file(sys.argv[1])

