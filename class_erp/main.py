from user import User 
from employee import Employee 
from emp_store import employees
import search as s
import change_emp as change

def main_menu():
	print("1. Add employee")
	print("2. Delete employee")
	print("3. Search employee")
	print("4. Display all employee")
	print("5. Change a employee details") 
	print("6. exit")

while True:
	main_menu()
	
	ch = int(input("Enter your choice"))
	if ch == 1:
		
		st_temp = Employee()
		employees.append(st_temp)
		employees[-1].insert()

	elif ch == 2:
		print(employees)
		eid=input("Enter the employye id:")
		for i in employees:
			if i.empid == eid:
				employees.pop(employees.index(i))
		
	elif ch == 3:
		s.search_main()
			
		
	elif ch == 4:
		for i in employees:
			i.display()
			
	elif ch== 5:
		change.change_main()
	
	elif ch == 6:
		#Exit
		break;
	else:
		print("Invalid Choice")

























