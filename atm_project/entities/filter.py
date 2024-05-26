from helpers.connect import get_connection

class Filter:
    @staticmethod
    def filter_by_balance() -> None:
        try:
            # Get user input for balance and filter type
            balance = float(input("Enter the balance amount: "))
            filter_type = input("Do you want to filter for balances greater or lower than the amount? (Enter 'greater' or 'lower'): ").strip().lower()

            if filter_type not in ["greater", "lower"]:
                print("Invalid filter type. Please enter 'greater' or 'lower'.")
                return

            # Establish the connection to the database
            connection = get_connection()
            if connection:
                cursor = connection.cursor(dictionary=True)

                # Construct the query based on the filter type
                if filter_type == "greater":
                    query = """
                    SELECT id, Name, Surname, cardnum, balance
                    FROM people
                    WHERE balance > %s
                    """
                else:
                    query = """
                    SELECT id, Name, Surname, cardnum, balance
                    FROM people
                    WHERE balance < %s
                    """
                
                # Execute the query
                cursor.execute(query, (balance,))
                results = cursor.fetchall()

                # Output the results
                if results:
                    for row in results:
                        print(f"================= {row['id']} ================")
                        print(f"Name: {row['Name']}")
                        print(f"Surname: {row['Surname']}")
                        print(f"Card Number: {row['cardnum']}")
                        print(f"Balance: {row['balance']}")
                        print("======================================")
                else:
                    print("No records found with the specified balance criteria.")
            else:
                print("Failed to connect to the database.")

        except ValueError:
            print("Invalid balance amount. Please enter a numeric value.")
        
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

# Example usage
if __name__ == "__main__":
    filter_instance = Filter()
    filter_instance.filter_by_balance()
