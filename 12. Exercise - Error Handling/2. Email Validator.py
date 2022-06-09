class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    line = input()
    if line == "End":
        break
    email = line

    email = email.split('@')
    if len(email) != 2:
        raise MustContainAtSymbolError("Email must contain @")

    if len(email[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    domain = email[1].split('.')
    if len(domain) != 2 or domain[1] not in ".com, .bg, .org, .net":
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
