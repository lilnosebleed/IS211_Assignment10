import sqlite3

def main():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    while True:
        ## asks the user for a person's ID number
        user_input = input("Enter a person's ID number (or -1 to exit): ")
        
        ## checks if the user wants to exit
        if user_input == '-1':
            print("Exiting program.")
            break
            
        try:
            person_id = int(user_input)
        except ValueError:
            print("Error: Please enter a valid number.")
            continue

        ## looks up the person in the database
        cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
        person = cursor.fetchone()

        ## if the person exists, print their data and lookup their pets
        if person:
            first_name, last_name, age = person
            print(f"{first_name} {last_name}, {age} years old")
            
            ## uses a JOIN function to get the pet data linked to the specific person
            cursor.execute("""
                SELECT pet.name, pet.breed, pet.age, pet.dead 
                FROM pet
                JOIN person_pet ON pet.id = person_pet.pet_id
                WHERE person_pet.person_id = ?
            """, (person_id,))
            
            pets = cursor.fetchall()
            
            for pet in pets:
                pet_name, breed, pet_age, dead = pet
                
                ## Ccecks the dead integer to format the sentence perfectly
                if dead == 1:
                    print(f"{first_name} {last_name} owned {pet_name}, a {breed}, that was {pet_age} years old")
                else:
                    print(f"{first_name} {last_name} owns {pet_name}, a {breed}, that is {pet_age} years old")
        
        ## if the person lookup came back completely empty
        else:
            print("Error: Person not found in the database.")

    conn.close()
    
    print("Running query_pets.py")
if __name__ == "__main__":
    main()
