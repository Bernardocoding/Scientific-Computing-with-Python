class Category:
  def __init__(self, label):
    self.label  = label
    self.ledger = []

  def get_balance(self):
    conta = 0
    for item in self.ledger:
      conta += item['amount']
    return conta

  def check_funds(self, amount):
    return amount <= self.get_balance()

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True

    return False

  def transfer(self, amount, objeto):
    if self.withdraw(amount, "Transfer to " + objeto.label):
      objeto.deposit(amount, "Transfer from " + self.label)
      return True

    return False

  def __str__(self):
    saida = ""
    saida += self.label.center(30,"*") + "\n"

    total = 0
    for item in self.ledger:
      total += item['amount']

      saida += item['description'].ljust(23, " ")[:23]
      saida += "{0:>7.2f}".format(item['amount'])
      saida += "\n"

    saida += "Total: " + "{0:.2f}".format(total)
    return saida

def create_spend_chart(categories):
  saida = "Percentage spent by category\n"

  # Retorna o total da despesa de cada categoria
  total      = 0
  despesas   = []
  labels     = []
  len_labels = 0

  for item in categories:
    despesa    = sum([-x['amount'] for x in item.ledger if x['amount'] < 0])
    total     += despesa

    if len(item.label) > len_labels:
      len_labels = len(item.label)

    despesas.append(despesa)
    labels.append(item.label)

  
  despesas = [(x/total)*100 for x in despesas]
  labels   = [label.ljust(len_labels, " ") for label in labels]

  
  for conta in range(100,-1,-10):
    saida += str(conta).rjust(3, " ") + '|'
    for x in despesas:
      saida += " o " if x >= conta else "   "
    saida += " \n"

  # Add each category name
  saida += "    " + "---"*len(labels) + "-\n"

  for i in range(len_labels):
    saida += "    "
    for label in labels:
      saida += " " + label[i] + " "
    saida += " \n"

  return saida.strip("\n")