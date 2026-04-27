import sqlite3
import matplotlib.pyplot as plt

# ==============================
# FUNCTION 1: CREATE DATABASE + TABLE
# ==============================
def create_database():
    # This creates (or opens) a database file
    conn = sqlite3.connect("population_SS.db")  # change SM to your initials
    cursor = conn.cursor()

    # Create table if it doesn't already exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    # Save changes and close
    conn.commit()
    conn.close()


# ==============================
# FUNCTION 2: INSERT 2025 DATA
# ==============================
def insert_starting_data():
    # 10 Florida cities with starting population (2025)
    cities = {
        "Jacksonville": 1000000,
        "Miami": 500000,
        "Tampa": 400000,
        "Orlando": 300000,
        "Port St. Lucie": 250000,
        "St. Petersburg": 260000,
        "Cape Coral": 240000,
        "Hialeah": 230000,
        "Tallahassee": 200000,
        "Fort Lauderdale": 180000
    }

    conn = sqlite3.connect("population_SM.db")
    cursor = conn.cursor()

    # Clear old data (so it doesn't duplicate every run)
    cursor.execute("DELETE FROM population")

    # Insert each city for the year 2025
    for city, pop in cities.items():
        cursor.execute("INSERT INTO population VALUES (?, ?, ?)",
                       (city, 2025, pop))

    conn.commit()
    conn.close()


# ==============================
# FUNCTION 3: SIMULATE 20 YEARS
# ==============================
def simulate_population():
    # Growth rates for each city
    # (positive = growth, negative = decline)
    rates = {
        "Jacksonville": 0.01,
        "Miami": 0.005,
        "Tampa": 0.012,
        "Orlando": 0.015,
        "Port St. Lucie": 0.02,
        "St. Petersburg": 0.003,
        "Cape Coral": 0.018,
        "Hialeah": -0.002,
        "Tallahassee": 0.004,
        "Fort Lauderdale": 0.006
    }

    conn = sqlite3.connect("population_SM.db")
    cursor = conn.cursor()

    # Loop through each city
    for city in rates:
        rate = rates[city]

        # Get starting population (2025)
        cursor.execute(
            "SELECT population FROM population WHERE city=? AND year=2025",
            (city,)
        )
        current_pop = cursor.fetchone()[0]

        # Simulate next 20 years (2026–2045)
        for year in range(2026, 2046):
            # New population = old population + growth
            current_pop = int(current_pop * (1 + rate))

            # Insert into table
            cursor.execute("INSERT INTO population VALUES (?, ?, ?)",
                           (city, year, current_pop))

    conn.commit()
    conn.close()


# ==============================
# FUNCTION 4: SHOW GRAPH
# ==============================
def show_graph():
    # List of cities (for user to choose)
    cities = [
        "Jacksonville", "Miami", "Tampa", "Orlando", "Port St. Lucie",
        "St. Petersburg", "Cape Coral", "Hialeah", "Tallahassee",
        "Fort Lauderdale"
    ]

    # Show options
    print("Choose a city:")
    for city in cities:
        print("-", city)

    # Ask user for input
    choice = input("Enter city name: ")

    # If invalid choice, stop
    if choice not in cities:
        print("Invalid choice.")
        return

    conn = sqlite3.connect("population_SM.db")
    cursor = conn.cursor()

    # Get all data for that city
    cursor.execute(
        "SELECT year, population FROM population WHERE city=? ORDER BY year",
        (choice,)
    )

    data = cursor.fetchall()

    conn.close()

    # Separate into lists for graph
    years = []
    populations = []

    for row in data:
        years.append(row[0])
        populations.append(row[1])

    # Plot graph
    plt.plot(years, populations)
    plt.title("Population for " + choice)
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.show()


# ==============================
# MAIN PROGRAM
# ==============================
def main():
    create_database()        # Step 1
    insert_starting_data()   # Step 2
    simulate_population()    # Step 3
    show_graph()             # Step 4


# Run the program
main()