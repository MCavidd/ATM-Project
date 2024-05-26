# number.py
class Number:
    def __init__(self, cardnum):
        if not self.is_valid_card_number(cardnum):
            raise ValueError("Card number must be exactly 16 digits")
        self.cardnum = cardnum

    @staticmethod
    def is_valid_card_number(cardnum):
        return len(cardnum) == 16 and cardnum.isdigit()



