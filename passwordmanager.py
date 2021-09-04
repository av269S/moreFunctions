def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")
def view():
	with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw)\
def forgotpassword():
	pass

MASTERPASSWORD = ''

while True:
  MASTERPASSWORD_INPUT = input("Please Enter your Master Password(forgot, q):")
	if MASTERPASSWORD_INPUT == MASTERPASSWORD:
		while True:
			MODE = input("Would you like to add a password or view existing passwords?(add, view, q): ").lower()
			if MODE == 'add':
				add()
			elif MODE == 'view':
				view()
			elif MODE == 'q':
				print("Quitted Application.")
				break
			else:
				print("Invalid Input. Please try again")
				continue
	elif MASTERPASSWORD_INPUT == 'forgot':
		forgotpassword()
	elif MASTERPASSWORD_INPUT == 'q':
		print("Quitted Application.")
		break
	else:
		print("Invalid Input. Please try again")
		continue
