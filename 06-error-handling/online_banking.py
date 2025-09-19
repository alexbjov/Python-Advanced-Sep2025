class MoneyNotEnoughError(Exception):
	pass

class PINCodeError(Exception):
	pass

class UnderageTransactionError(Exception):
	pass

class MoneyIsNegativeError(Exception):
	pass

LEGAL_AGE = 18
user_data = input().split(', ')
user_pin = user_data[0]
user_balance = int(user_data[1])
user_age = int(user_data[2])

command = input()
while command != 'End':
	tokens = command.split('#')
	action = tokens[0]
	money = int(tokens[1])

	if action == 'Send Money':
		pin = tokens[2]
		if money > user_balance:
			raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

		if user_pin != pin:
			raise PINCodeError("Invalid PIN code")

		if user_age < LEGAL_AGE:
			raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

		user_balance -= money
		print(f"Successfully sent {money:.2f} money to a friend")
		print(f"There is {user_balance:.2f} money left in the bank account")

	elif action == 'Receive Money':
		if money < 0:
			raise MoneyIsNegativeError("The amount of money cannot be a negative number")

		money_to_bank_account = money / 2
		user_balance += money_to_bank_account
		print(f"{money_to_bank_account:.2f} money went straight into the bank account")

	command = input()
