class Amount:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        return repr((self.currency, self.amount))

    def add(self, that):
        if self.currency == that.currency:
            self.amount += that.amount
        else:
            # raise Exception('Currency Does not match')
            raise CurrencyDoesNotMatchException(self.currency + " " + that.currency)


amount1 = Amount('LKR', 10)
amount2 = Amount('EUR', 5)
amount3 = Amount('USD', 15)
amount4 = Amount('LKR', 10)

amount1.add(amount4)  # add two amounts
print(amount1)


# amount1.add(amount2) throw exception


class CurrencyDoesNotMatchException(Exception):
    def __init__(self, message):
        super().__init__(message)
