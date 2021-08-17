org={}

def add_oganization():
	org['name']=input("Enter organization name")
	org['email']=input("Enter email")
def edit_oganization():
	print("Press 1 for Edit Organization name ")
	print("Press 2 for Edit Organization email")
	choi = int(input("Enter choice"))
	#id=int(input("Enter the organization id"))
	if choi == 1:
		org['name'] = input("Enter new organization name")
	elif choi == 2:
		org['email'] = input("Enter new organization email")	
	else:
		print("Invalid choice")	
	
def org_menu():
	print("Press 1 for Add Organization")
	print("Press 2 for Edit Organization")
	print("Press 3 Display Organization details")
	print("Press 4 for exit")
	while True:
	
		choic = int(input("Enter choice"))
		if choic == 1:
			add_oganization()
		elif choic == 2:
			edit_oganization()
		elif choic == 3:
			print(org)
		elif choic == 4:
			break
		else:
			print("Invalid choice")

