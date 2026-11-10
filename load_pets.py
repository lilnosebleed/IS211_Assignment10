import sqlite3

def main():
    ## connects to the database
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    ## drops old tables so we can run this script multiple times without crashing
    cursor.execute("DROP TABLE IF EXISTS person")
    cursor.execute("DROP TABLE IF EXISTS pet")
    cursor.execute("DROP TABLE IF EXISTS person_pet")

    ## creates the tables using basic execute commands
    cursor.execute("""
        CREATE TABLE person (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE pet (
            id INTEGER PRIMARY KEY,
            name TEXT,
            breed TEXT,
            age INTEGER,
            dead INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE person_pet (
            person_id INTEGER,
            pet_id INTEGER
        )
    """)

    ## inserts the data using simple, standard for loops
    persons = [
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23)
    ]
    for p in persons:
        cursor.execute("INSERT INTO person VALUES (?, ?, ?, ?)", p)

    pets = [
        (1, 'Rusty', 'Dalmation', 4, 1),
        (2, 'Bella', 'Alaskan Malamute', 3, 0),
        (3, 'Max', 'Cocker Spaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'Cocker Spaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1)
    ]
    for p in pets:
        cursor.execute("INSERT INTO pet VALUES (?, ?, ?, ?, ?)", p)

    person_pets = [
        (1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6)
    ]
    for pp in person_pets:
        cursor.execute("INSERT INTO person_pet VALUES (?, ?)", pp)

    ## 4. saves and closes
    conn.commit()
    conn.close()
    
    print("Running load_pets.py")
if __name__ == "__main__":
    main()
