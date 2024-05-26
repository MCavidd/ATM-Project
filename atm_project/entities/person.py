from mysql.connector import Error
from entities.number import Number
from helpers.connect import get_connection

class Person:
    def __init__(self):
        pass

    def add_to_db(self, name, surname, cardnum, pin, balance):
        try:
            connection = get_connection()
            if connection and connection.is_connected():
                cursor = connection.cursor()

                # Insert the person into the "people" table
                insert_query = """
                INSERT INTO people (Name, Surname, cardnum, pin, balance)
                VALUES (%s, %s, %s, %s, %s)
                """
                cursor.execute(insert_query, (name, surname, cardnum, pin, balance))

                # Commit the transaction
                connection.commit()
                print("Person added successfully")

        except ValueError as ve:
            print("Validation Error:", ve)
        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def delete_person() -> None:
        name = input("Enter the name of the person: ")
        surname = input("Enter the surname of the person: ")
        cardnum = input("Enter the 16-digit card number: ")

        try:
            connection = get_connection()
            if connection and connection.is_connected():
                cursor = connection.cursor()

                # Verify if the person exists and retrieve their details including id
                select_query = """
                SELECT id, Name, Surname, cardnum, pin, balance FROM people
                WHERE Name = %s AND Surname = %s AND cardnum = %s
                """
                cursor.execute(select_query, (name, surname, cardnum))
                person = cursor.fetchone()

                if person:
                    # Delete the person from the "people" table
                    delete_query = """
                    DELETE FROM people
                    WHERE id = %s
                    """
                    cursor.execute(delete_query, (person[0],))  # person[0] is the id

                    # Insert the deleted person's information into the "delete2" table
                    insert_delete_query = """
                    INSERT INTO `delete2` (id, Name, Surname, cardnum, pin, balance)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(insert_delete_query, person)  # Use the fetched person details including id

                    # Commit the transaction
                    connection.commit()
                    print("Person deleted successfully")
                else:
                    print("Person not found")

        except Error as e:
            print("Error while connecting to MySQL:", e)
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
