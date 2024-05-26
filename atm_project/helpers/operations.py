class Operations:
    def __init__(self) -> None:
        pass

    def main_operations(self) -> None:
        
        return input('''
    Choose an operation please --->
        Operations:
            1 -> Add a person to Bank
            2 -> Delete a person from Bank
            3 -> Login
            4 -> Search Person
            5 -> Search Deleted Person
            6 -> Filter
            exit -> Exit
    ''')
        
        
    
    def login_operations(self) -> None:
        return print('''
    Which operation do you want to continue?
        Operations:
            1 -> Cash In
            2 -> Withdraw
            3 -> Transaction
            4 -> Edit PIN
            ''')
