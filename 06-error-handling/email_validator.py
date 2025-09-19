class NameTooShortError(Exception):
	pass

class MustContainAtSymbolError(Exception):
	pass

class InvalidDomainError(Exception):
	pass

NAME_MIN_LENGTH = 5
allowed_domains = {'com', 'bg', 'org', 'net'}
email = input()
while email != 'End':

	if '@' not in email:
		raise MustContainAtSymbolError('Email must contain @')

	position_of_at = email.index('@')
	if position_of_at < NAME_MIN_LENGTH:
		raise NameTooShortError('Name must be more than 4 characters')

	domain = email.split('.')[-1]
	if domain not in allowed_domains:
		raise InvalidDomainError('Domain must be one of the following: .com, '
								 '.bg, .org, .net')

	print('Email is valid')

	email = input()
