class Account:
    def __init__(self):
        pass

    @staticmethod
    def edit_pin(cursor, connection, cardnum):
        new_pin = input("Enter your new 4-digit PIN: ")
        confirm_pin = input("Confirm your new 4-digit PIN: ")

        if new_pin == confirm_pin and len(new_pin) == 4 and new_pin.isdigit():
            update_pin_query = """
            UPDATE people
            SET pin = %s
            WHERE cardnum = %s
            """
            cursor.execute(update_pin_query, (new_pin, cardnum))
            connection.commit()
            print("PIN updated successfully!")
        else:
            print("PINs do not match or PIN is not a 4-digit number. Please try again.")
