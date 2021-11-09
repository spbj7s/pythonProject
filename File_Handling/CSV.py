import csv
with open('emp2.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['eno','ename','esal','eaddr'])
    while True:
        eno=int(input("Enter Employee number: "))
        ename=input("enter the Employee name: ")
        esal=float(input("Enter the Salary: "))
        eaddr=input("enter the Employee Adress: ")
        w.writerow([eno,ename,esal,eaddr])
        option=input("do you want to insert one more record[Yes|No]:")
        if option.lower()=='no':
            break
print("Total Employee data written to csv file successfully")

