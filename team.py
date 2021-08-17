import employee as em

teams = {} 

def manage_all_team_menu():
	print("\t1.Create Team")
	print("\t2.Display Team")
	print("\t3.Manage Team(Particular)")
	print("\t4.Delete Team")
	print("\t5.Exit")


def create_team():
	team_name = input("\tEnter team name ")
	teams[team_name] = []
def delete_team():
	team_name = input("\tEnter team name ")
	if team_name in teams.keys():
		del teams[team_name]
		print("\tDeleted the team")
	else:
		print("\tWrong team name")

def display_teams():
	for key,value in teams.items(): 
		name_string = ""
		for i in value:
			name_string = name_string +"|"+em.employees[i]["name"]
		print(f"{key} => {name_string}")

def manage_team_menu():
	print("\t1.Add Member")
	print("\t2.Delete Member")
	print("\t3.List Members")
def manage_team():
	team_name = input("\t\tEnter team name ")
	manage_team_menu()
	ch = int(input("\t\t Enter your Choice "))
	if ch == 1:
		add_member(team_name)
	elif ch == 2:
		delete_member(team_name)
	elif ch == 3:
		list_member(team_name)
	else:
		print("\tInvalid choice")
def add_member(team_name):
	em.display_employee()
	serial_no = input("\t\tEnter the serial no ofemployee ")
	if serial_no in em.employees.keys():
		teams[team_name].append(serial_no)
	else:
		print("\t\tWrong serial No.")
def list_member(team_name):
	name_string=""
	for i in teams[team_name]:
		name_string = name_string +"|"+i+"."+em.employees[i]["name"]
	print(f"{name_string}")

def delete_member(team_name):
	list_member(team_name)
	serial_no = input("\t\tEnter serial no from list")
	if serial_no in teams[team_name]:
		teams[team_name].remove(serial_no)
	else:
		print("\t\tWrong serial No.")
def manage_all_teams():
	while True:
		manage_all_team_menu()
		ch = int(input("\tEnter your choice "))
		if ch == 1:
			create_team()
		elif ch == 2:
			display_teams()
		elif ch == 3:
			manage_team()
		elif ch == 4:
			delete_team()
		elif ch == 5:
			break
		else:
			print("\tInvalid choice")
