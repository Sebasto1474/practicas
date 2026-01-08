class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        header = str(self.name).center(30, "*")
        lines = ""
        for trf in self.ledger:
            description = str(trf["description"])
            amount = trf["amount"]
            formatted_description = description[:23].ljust(23)
            formatted_amount =  f"{amount:.2f}".rjust(7)
            linea = formatted_description + formatted_amount
            lines += linea + "\n"
        total = f"Total: {self.get_balance():.2f}"
        return f"{header}\n{lines}{total}"


    def deposit(self, amount, description=""):
        trf = {"amount": amount, "description": description}
        self.ledger.append(trf)

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) is False:
            return False
        self.ledger.append({"amount": -amount, "description": description})
        return True

    def get_balance(self):
        balance = 0
        for amount in self.ledger:
            value = amount["amount"]
            balance += value
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount) is False: 
            return False
        self.withdraw(amount, f"Transfer to {category.name}")
        category.deposit(amount, f"Transfer from {self.name}")
        return True

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

def create_spend_chart(categories):
    title = "Percentage spent by category"
    withdraws_per_category = []
    for category in categories:
        withdraws_for_category = 0
        for amount in category.ledger:
            if amount["amount"] < 0:
                withdraws_for_category += -amount["amount"]
        withdraws_per_category.append(withdraws_for_category)
    total_withdraws = sum(withdraws_per_category)
    percentages = []
    for withdraw in withdraws_per_category:
        percentages.append(int((withdraw / total_withdraws) * 100 / 10) * 10)
    chart = title + "\n"
    for level in range(100, -10, -10):
        line = f"{level:>3}|"
        for percentage in percentages:
            if percentage > level:
                line += " o "
            else:
                line += "   "
        chart += line + "\n"
    num_categories = len(categories)
    dashes = "-" * (num_categories * 3 + 1)
    hor_line = "    " + dashes + "\n"
    chart += hor_line
    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        name_line = "     "
        for category in categories:
            if i < len(category.name):
                name_line += category.name[i] + "  "
            else:
                name_line += "   "
        chart += name_line + "\n"
    chart = chart.rstrip("\n")
    return chart


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(600, 'restaurant and more food for dessert')
clothing = Category('Clothing')
auto = Category("Auto")
auto.deposit(200, "deposit")
clothing.deposit(200,"deposit")
auto.withdraw(100, "gasoline")
clothing.withdraw(150, "H&M")
print(food, "\n")
print(clothing, "\n")
print(auto, "\n")
print(create_spend_chart([food,clothing, auto]))
