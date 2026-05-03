class Account:
    def __init__(self, title: str, balance: int):
        self.title = title # Public attribute
        self._balance = balance # Protected attribute
    
    def display_balance(self) -> None:# Public method
        print(f"Balance: ${self._balance}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
