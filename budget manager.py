class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []

    #Function to deposit amount, alongside an additional (optional) reasoning 
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        
    #Function to withdraw amount if enough balance is present, alongside an additional (optional) reasoning 
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    #Function to check the total balance present 
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance

#As of now, we have covered the basics: Depositing, Withdrawing, Checking Balance

    #Transfers a certain amount to a certain category after withdrawing (if available)
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.category}")
            category.deposit(amount, f"Transfer from {self.category}")
            return True
        return False
        
    #Provides information if the transaction is possible or not by looking at the balance
    def check_funds(self, amount):
        return amount <= self.get_balance()

#Now, we move on to the visuals part

    #Invoked by printing the category object
    #prints a datasheet about all transactions carried out in the category, as well as the total available balance
    #format below --.--
#___________________________________________#
#|                                          |
#|    **********categoryname***********     |
#|    Initial Deposit           X.X         |
#|    Transaction[i]           -Y.Y[i]      |
#|    Total: X.X - sum(Y.Y)                 |
#|                                          |
#___________________________________________#
    
#____________________________________________________________________________st__datasheet   
    def __str__(self):                                                           
        title = f"{self.category:*^30}\n"                                        
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:23}{item['amount']:7.2f}\n"
            total += item['amount']
        output = title + items + f"Total: {total:.2f}"
        return output
#____________________________________________________________________________en__datasheet
    

    
    #creates a graph based on percentage of total spendings spent on specific categories
    #format below --.--
#______________________________________#
#|                                     |
#|    Percentage Spent by Category     |
#|    100|                             |
#|     90|                             |
#|     80|                             |
#|     70|                             |
#|     60|                             |
#|     50|                             |
#|     40|       o                     |
#|     30| o     o                     |
#|     20| o     o                     |
#|     10| o  o  o                     |
#|      0| o  o  o                     |
#|        ----------                   |
#|         c  c  c                     |
#|         1  2  3                     |
#|                                     |
#______________________________________#
    
#___________________________________________________________________________st__chart
    def create_spend_chart(categories):
        category_names = []
        spent = []
        spent_percentages = []

        for category in categories:
            total_spent = 0
            for item in category.ledger:
                if item['amount'] < 0:
                    total_spent -= item['amount']
            spent.append(round(total_spent, 2))
            category_names.append(category.category)

        for amount in spent:
            spent_percentages.append(round(amount / sum(spent), 2) * 100)

        graph = "Percentage spent by category\n"
        labels = range(100, -10, -10)

        for label in labels:
            graph += str(label).rjust(3) + "| "
            for percent in spent_percentages:
                if percent >= label:
                    graph += "o  "
                else:
                    graph += "   "
            graph += "\n"

        graph += "    " + "-" * (3 * len(category_names) + 1) + "\n"

        longest_name_length = max([len(name) for name in category_names])

        for i in range(longest_name_length):
            name_line = "     "
            for name in category_names:
                if i < len(name):
                    name_line += name[i] + "  "
                else:
                    name_line += "   "
            if i < longest_name_length - 1:
                name_line += "\n"
            graph += name_line

        return graph
#___________________________________________________________________________en__chart



#Things you can do:
#  - Mention Category [ category = Category("desiredcategory") ]
#  - Deposit Money [ category.deposit ( X , Y ) ]
#  - Withdraw Money [ category.withdrw ( X , Y ) ]
#  - Calculate Balance [ category.get_balance () ]
#  - Transfer Money [ category.transfer ( X , Y {categorytotransferto} ) ]
#  - Check if X amount is available or not [ category.check_funds ( X ) ]
#  - Check all transactions [ print(category) ]
#  - Check percentage of transction vs category [ create_spend_chart([list of categories]) ]
