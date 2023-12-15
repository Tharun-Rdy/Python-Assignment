import mysql.connector
global tasks
tasks=[]
try:
     con=mysql.connector.connect(host='localhost', database='todolistmanagerdb',user='tharun',password='9490263169*')
     cursor=con.cursor()
     cursor.execute("Create table todolist(Task_Name Varchar(15),Priority Varchar(8),Due_Date int(10),Status varchar(15))")
     print("Table Created Successfully..")
     data="insert into todolist(Taskname, Priority, Duedate, Status) VALUES(%s,%s,%s,%s)"
     def add_tasks():
           loop_status=True
           while loop_status:
                Taskname=input("Enter the Task Name:")
                Priority=input("Enter the Priority of the Task:")
                Duedate=int(input("Enter the Duedate of the Task(YYYY-MM-DD):"))
                Status=input("Enter the Status of the Task:")
                in_dict={"Task":Taskname,"Priority":Priority,"Duedate":Duedate,"status":Status}
                tasks.append(in_dict)
                choice=input("Do you want to add new task again[Yes/No]")
                if choice.upper()=='NO':
                     loop_status=False
                print(tasks,end="\n")

     cursor.execute(data)
     con.commit()
     print("Data entered successfully")
     cursor.execute("select * from todolist")
     char=cursor.fetchall()
     for row in char:
          print("Employee Number:",row[0])
          print("Employee Name:",row[1])
          print("Empl",row[2])
          print("Emp",row[3])
          print()

except mysql.connector.DatabaseError as x:
      if con:
          con.rollback()
          print("There is a problem with sql:",x)
finally:
     if cursor:
          cursor.close()
     if con:
          con.close()
add_tasks()
