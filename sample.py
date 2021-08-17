employees={}
teams = {} 
org={}
def change_employee_details():
	print("Enter 1 for change name")
	print("Enter 2 for change age")
	print("Enter 3 for change gender")
	print("Enter 4 for change salary")
	cho =int(input("\tEnter your choice."))
	employee_id = input("\tEnter employee id.")
	if cho == 1:
		employees[employee_id]['name'] = input("\tEnter new name") 
	elif cho == 2:
		employees[employee_id]['age'] = input("\tEnter new age")
	elif cho == 3:
		employees[employee_id]['gender'] = input("\tEnter gender")
	elif cho == 4:
		employees[employee_id]['salary'] = input("\tEnter new salary")
	else:
		print("invalid choice!!")
def display_employee():
	for id,employee in employees.items():
		print(f"\t{id} | {employee['name']} | {employee['age']} | {employee['place']} | {employee['gender']} | {employee['previous_company']} | {employee['salary']} ")
		
#def search_employee():
#	name = input("\tEnter name")
#	found = False
#	for i in employees.values():
#		if i["name"] == name: 
#			print(f"\t{i['name']} | {i['age']} | {i['place']} | {i['gender']} | {i['previous_company']} | {i['salary']} ")
#			found = True
#			break
#		if found == False :
#			print("\tNot found")
def delete_employee():
	eid = input("\tEnter employee id")
	if eid not in employees.keys():
		print("\tWrong Employee id")
	else:
		del employees[eid]
def add_employee():
	employee_id = input("\tEnter Employee id ")
	if employee_id not in employees.keys():
		name = input("\tEnter name ")
		age = int(input("\tEnter age "))
		gender = input("\tEnter the gender ")
		place = input("\tEnter place ")
		salary = int(input("\tEnter salary "))
		previous_company = input("\tEnter your previous company ")
		joining_date = input("\tEnter joining date ")
		temp ={
			"name":name,
			"age":age,
			"gender":gender,
			"place":place,
			"salary":salary,
			"previous_company":previous_company,
			"Joining_date":joining_date,
		}
		employees[employee_id] = temp
	else:
		 print("\tEmployee id  already Taken")
def manage_all_team_menu():
	print("\t1.Create Team")
	print("\t2.Display Team")
	print("\t3.Manage Team(Particular)")
	print("\t4.Delete Team")
	print("\t5.Exit")

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
			name_string = name_string +"|"+employees[i]["name"]
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
	display_employee()
	serial_no = input("\t\tEnter the serial no ofemployee ")
	if serial_no in employees.keys():
		teams[team_name].append(serial_no)
	else:
		print("\t\tWrong serial No.")
def list_member(team_name):
	name_string=""
	for i in teams[team_name]:
		name_string = name_string +"|"+i+"."+employees[i]["name"]
	print(f"{name_string}")

def delete_member(team_name):
	list_member(team_name)
	serial_no = input("\t\tEnter serial no from list")
	if serial_no in teams[team_name]:
		teams[team_name].remove(serial_no)
	else:
		print("\t\tWrong serial No.")
def main_menu():
	print("Press 1 for add employee")
	print("Press 2 for delete employee ")
	print("Press 3 for search employee")
	print("Press 4 for display  employee")
	print("Press 5 for change employee details")
	print("Press 6 fo manage teams")
	print("Press 7 for Quit")
def search_menu():
	
	print("Press 1 for search by name")
	print("Press 2 for search by age")
	print("Press 3 for search by salary")
	print("Press 4 for search  by gender")
	print("Press 5 for exit")
	while True:
	
		choice = int(input("Enter choice"))
		if choice == 1:
			search_by_name()
		elif choice == 2:
			search_by_age()
		elif choice == 3:
			search_by_salary()
		elif choice == 4:
			search_by_gender()
		elif choice == 5:
			break
		else:
			print("Invalid choice")
def search_by_name():	
	name=input("Enter the name")
	print(list(filter(lambda a:a["name"] == name, employees.values())))
	print("We Found")
	#if name in employees.values():
	#	print(list(filter(lambda a:a["name"] == name, employees.values())))
	#	print("We Found")
	#else:
		##print("Not Found")
def search_by_age():	
	age=int(input("Enter the age"))
	print(list(filter(lambda a:a["age"] == age, employees.values())))
	print("We Found")
def search_by_salary():	
	salary=int(input("Enter the salary"))
	print(list(filter(lambda a:a["salary"] == salary, employees.values())))
	print("We Found")
def search_by_gender():	
	gender=input("Enter the gender")
	print(list(filter(lambda a:a["gender"] == gender, employees.values())))
	print("We Found")
def add_oganization():
	org['name']=input("Enter organization name")
	org['email']=input("Enter email")
	pass
while True:
	add_oganization()
	main_menu()
	ch = int(input("Enter choice"))
	if ch == 1:
		add_employee()
	elif ch == 2:
		delete_employee()
	elif ch == 3:
		search_menu()
	elif ch == 4:
		display_employee()
	elif ch== 5:
		change_employee_details()
	elif ch== 6:
		manage_all_teams()
	elif ch == 7:
		break;
	else:
		print("Invalid Choice")
