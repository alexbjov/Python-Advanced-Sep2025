class PasswordTooShortError(Exception):
	pass

class PasswordTooCommonError(Exception):
	pass

class PasswordNoSpecialCharactersError(Exception):
	pass

class PasswordContainsSpacesError(Exception):
	pass

PASS_MIN_LENGTH = 8
special_chars = {'@', '*', '&', '%'}

password = input()
while password != 'Done':

	if len(password) < PASS_MIN_LENGTH:
		raise PasswordTooShortError('Password must contain at least 8 characters')

	if password.isdigit() or password.isalpha():
		raise PasswordTooCommonError('Password must be a combination of digits, letters, and special characters')

	counter_special_chars = 0
	for special_char in special_chars:
		counter_special_chars += password.count(special_char)

	if counter_special_chars == 0:
		raise PasswordNoSpecialCharactersError ('Password must contain at least 1 special character')

	elif counter_special_chars == len(password):
		raise PasswordTooCommonError('Password must be a combination of digits, letters, and special characters')

	if ' ' in password:
		raise PasswordContainsSpacesError('Password must not contain empty spaces')

	print('Password is valid')

	password = input()
