
employees={}


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
def main_menu():
	print("Press 1 for Organization")
	print("Press 2 for add employee")
	print("Press 3 for delete employee ")
	print("Press 4 for search employee")
	print("Press 5 for display  employee")
	print("Press 6 for change employee details")
	print("Press 7 for manage teams")
	print("Press 8 for Quit")
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
		
		
		
		
