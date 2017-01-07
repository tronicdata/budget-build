#!/usr/bin/env python
"""
Beginning of the budget app, working out some ideas.
@author: Larry Buffaloboy
@creation Date: 12/7/2016
"""
import os
import json

clear = lambda: os.system('clear')
income = 1750

expenses = {

		"Envelopes": {
		
			"Rent": 1523,
			"Food": 300,
			"Gas" : 100,
			"Haircut": 20,
		},

		"Online":{
		
			"Internet": 70,
			"Utilities": 100,
			"Metro": 100,
			"Savings": 0,
			"Loans": 300,
			"Vehicle Insurance": 145,
			"Child Care": 545
		}
	}

class Budget(object):

	def __init__(self, workingIncome, cashOnHand=0, savings=1000):
		self.expenses = expenses
		self.workingIncome = workingIncome
		self.cashOnHand = cashOnHand
		self.totalIncome = workingIncome + cashOnHand
		self.savings = savings
		self.getTotalExpenses()
		self.getLeftOverAmount()
		self.getEnvelopeTotal()

	def getTotalExpenses(self):
		self.totalExpenses = 0
		for i in self.expenses:
			for j in self.expenses[i]:
				self.totalExpenses += self.expenses[i][j] 

	def getLeftOverAmount(self):
		self.leftOverAmount = self.totalIncome - self.totalExpenses

	def getEnvelopeTotal(self):
		self.cashToTakeOut = 0
		for i in self.expenses["Envelopes"]:
			self.cashToTakeOut += self.expenses["Envelopes"][i]

	def addExpense(self, name, amount, category):
		self.expenses[category][name] = int(amount)
		self.getTotalExpenses()
		self.getEnvelopeTotal()

	def setExpense(self, name, amount):
		hasKey = False

		for i in self.expenses:
			if self.expenses[i].has_key(name):
				hasKey = True
				self.expenses[i][name] = int(amount)
				break

		if hasKey:
			print("Expense Updated: " + name + " = " + str(amount))
			self.getTotalExpenses()

		else:
			print("Expense name does not exist. Maybe try 'addExpense' for new expenses.")
					

	def listExpenses(self):
		for i in self.expenses:
			for j in self.expenses[i]:
				print("" + j + " = $" + str(self.expenses[i][j]) + "")

	def __str__(self):
		return "Budget[workingIncome=" + str(self.workingIncome) + \
		", cashOnHand=" + str(self.cashOnHand) + "]"
	

def main():

	going = 0
	global bud

	while going >= 0:
		
		if(going == 0): 
		
			print("Would you like to start a new budget?[y/n]")
			s = raw_input('-->')

			if( s == "y"):
				print("We will Continue!!")
				
				print("How much is in your checking account currently?")
				bankAmount = raw_input('-->$')

				print("Online Checking Amount = %s" %bankAmount)

				print("Ok. Any Cash on hand? [y/n]")
				cashOrNah = raw_input('-->')
				cash = 0

				if ( cashOrNah == "y"):
				
					print("How much did you count?")
					cash = raw_input('-->$')
					print("Cash on hand = %s" % cash )
					bud = Budget( int(bankAmount), int(cash) )
					print("Budget Created!")
					going = 1

				elif ( cashOrNah == "n"):
					
					print("Broke ass...")
					bud = Budget( int(bankAmount) )
					print("Either way, Your Budget has been created. Your welcome.")
					going = 1
				
				else:
					print("What are you stupid? Type 'y' or 'n' when I ask you the first time.")
					print("And since you want to be fresh, we can just start this over...")
					going = 0

			elif ( s == "n"): 
				print("This is over bro")
				going = -1
		
		elif ( going == 1 ):
				
			print("Now choose an option:")
			print("1) Total Income \n" \
				"2) Total Expenses \n" \
				"3) List Expenses \n" \
				"4) Envelope Total \n" \
				"5) Update Expense \n" \
				"6) Add Expense \n" \
				"7) Clear Log \n" \
				"0) Exit")
			choice = raw_input("-->")
			choice = int(choice)	
			if( choice == 0):
				print("Have a great day!!")
				going = -1
			
			elif ( choice == 1 ):
				print("Total Income = %.2f" % bud.totalIncome )

			elif ( choice == 2 ):
				print("Total Expenses = %.2f" % bud.totalExpenses )

			elif ( choice == 3 ):
				bud.listExpenses()

			elif ( choice == 4 ):
				print("Envelope Total = %.2f" % bud.cashToTakeOut )
			
			elif ( choice == 5 ):
				print("Which expense amount did you want to update?")
				name = raw_input("-->")
				print("And the new Amount?")
				amount = raw_input('-->')
				bud.setExpense(name, amount)
		
			elif ( choice == 6 ):
				print("What is the name of your new Expense?")
				name = raw_input("-->")
				print("And the amount?")
				amount = raw_input("-->")
				print("Is it a (1)Cash OR (2)Online Expense?")
				category = raw_input("-->")
				if ( category == "1" ):
					category = "Envelopes"
					bud.addExpense(name, amount, category)

				elif ( category == "2" ):
					category = "Online"
					bud.addExpense(name, amount, category)

				else:
					print("Wrong Input. Transaction Cancelled...")
					
			elif ( choice == 7 ):
				clear()
			
			elif ( choice == 8 ):
				with open('printing.txt', 'w') as f:
					json.dump(bud.expenses, f)
				f.closed
			

		
		

if __name__ == "__main__":
	main()
