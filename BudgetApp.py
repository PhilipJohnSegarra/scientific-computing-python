class Category:
    def __init__(self, categoryname):
        self.categoryName = categoryname
        self.ledger = []
    pass

    def __str__(self):
        firstSide = ('*' * (15 - len(self.categoryName)//2)) if len(self.categoryName) % 2 == 0 else ('*' * ((15 - len(self.categoryName)//2) - 1))
        topheader = firstSide + self.categoryName + ('*' * (15 - len(self.categoryName)//2))
        body = '\n'
        total = 'Total: ' + str("{:.2f}".format(self.get_balance()))
        offset = 0
        for record in self.ledger:
            offset = len(topheader) - (len(record['description'][:23]) + len(str("{:.2f}".format(record['amount']))))
            body += record['description'][:23] + str(' ' * offset) + str("{:.2f}".format(record['amount']))
            body += '\n'
        return topheader + body + total

    def deposit(self, amount, description = ''):
        self.ledger.append({"amount": amount, "description": description})
    
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -(amount), "description": description})
            return True
        return False

    def get_balance(self):
        Total = 0
        for budget in self.ledger:
            Total += budget['amount']
        return Total

    def transfer(self, amount, category):
        transferSuccessful = self.withdraw(amount, f"Transfer to {category.categoryName}")
        if transferSuccessful:
                category.deposit(amount, f'Transfer from {self.categoryName}')
                return True
        return False
        #True if the transfer took place, and False otherwise

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True
        

def create_spend_chart(categories):
    category_dict= []
    grandTotal = 0
    bottomBar = '    '
    for category in categories:
        totalSpent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                totalSpent += item['amount']
                #print(item['amount'])
        category_dict.append((category.categoryName, (totalSpent)))

    #add each total spent to grand total
    for item in category_dict:
        grandTotal += item[1]
        bottomBar += '---'
    bottomBar += '-'
    #print result
    print(' Percentage spent by category')
    Value = 100
    for i in range(11):
        datapoint = ''
        for items in category_dict:
            if (items[1] / grandTotal * 100) >= Value:
                datapoint += 'o'
                datapoint += '  '
            elif (items[1] / grandTotal * 100) < Value:
                datapoint += ' '
                datapoint += '  '
        print(' '+' ' * (3 - len(str(Value))) + str(Value) + '|', datapoint)
        Value -= 10
    
    #print bottom bar to display items
    print(' '+bottomBar)
    maxItemLen = 0
    for item in category_dict:
        if len(item[0]) > maxItemLen:
            maxItemLen = len(item[0])
    iterator = 0
    for i in range(maxItemLen):
        characters = '     '
        for item in category_dict:
            try:
                if item[0][iterator] is not None:
                    characters += item[0][iterator]
                    characters += '  '
            except IndexError:
                characters += ' '
                characters += '  '
        iterator += 1
        print(' ' + characters)
    


food = Category('Food')
bills = Category('Bills')
bills.deposit(800, 'Electricity')
bills.withdraw(640, 'Maintenance')
food.deposit(300, 'restaurant and more food for dessert')
food.withdraw(80, 'hello')
wants = Category('Wants')
wants.deposit(500, 'For PC')
wants.withdraw(350, 'Buy PC')
#print(food)
#print(bills)

create_spend_chart([food, bills, wants])

