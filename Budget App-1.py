class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({
            "amount": amount,
            "description": description
        })

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, "*") + "\n"
        items = ""

        for entry in self.ledger:
            desc = entry["description"][:23]
            amount = f"{entry['amount']:.2f}"[:7]
            items += f"{desc:<23}{amount:>7}\n"

        total = f"Total: {self.get_balance()}"
        return title + items + total


def create_spend_chart(categories):
    withdrawals = []

    for category in categories:
        total = 0
        for item in category.ledger:
            if item["amount"] < 0:
                total += -item["amount"]
        withdrawals.append(total)

    total_spent = sum(withdrawals)

    percentages = [
        int((spent / total_spent) * 100) // 10 * 10
        for spent in withdrawals
    ]

    chart = "Percentage spent by category\n"

    for percent in range(100, -1, -10):
        chart += f"{percent:>3}| "
        for p in percentages:
            chart += "o  " if p >= percent else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [c.name for c in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += (name[i] if i < len(name) else " ") + "  "
        if i < max_len - 1:
            chart += "\n"

    return chart