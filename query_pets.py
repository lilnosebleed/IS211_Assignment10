import sqlite3
def main():
    ## this connects to the database, or creates pets.db if it doesn't exist yet
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()
    
    ## creates the tables 
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS person (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER
        );
        CREATE TABLE IF NOT EXISTS pet (
            id INTEGER PRIMARY KEY,
            name TEXT,
            breed TEXT,
            age INTEGER,
            dead INTEGER
        );
        CREATE TABLE IF NOT EXISTS person_pet (
            person_id INTEGER,
            pet_id INTEGER
        );
    ''')
    
    ## clears out any old data just in case the script is rna more than once
    cursor.execute("DELETE FROM person")
    cursor.execute("DELETE FROM pet")
    cursor.execute("DELETE FROM person_pet")

    ## loads up the persons data
    person_data = [
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23)
    ]
    cursor.executemany("INSERT INTO person VALUES (?, ?, ?, ?)", person_data)

    ## loads up the pet data
    pet_data = [
        (1, 'Rusty', 'Dalmation', 4, 1),
        (2, 'Bella', 'Alaskan Malamute', 3, 0),
        (3, 'Max', 'Cocker Spaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'Cocker Spaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1)
    ]
    cursor.executemany("INSERT INTO pet VALUES (?, ?, ?, ?, ?)", pet_data)

    ## loads up the relationship data (which person owns which pet)
    person_pet_data = [
        (1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (4, 6)
    ]
    cursor.executemany("INSERT INTO person_pet VALUES (?, ?)", person_pet_data)

    ## saves our changes and closesw the connection
    conn.commit()
    conn.close()

    print("Running query_pets.py")
if __name__ == "__main__":
    main()
