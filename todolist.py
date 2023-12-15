global tasks
tasks=[]
def add_tasks():
     loop_status=True
     while loop_status:
          #Taking the Input from the user....
          Task=input("Enter the Task Name:")
          Priority=input("Enter the Priority of the Task:")
          Duedate=input("Enter the Duedate of the Task(YYYY-MM-DD):")
          Status=input("Enter the Status of the Task:")
          #Add the Task details to the Tasks List as a dictionary format..
          in_dict={"Task":Task,"Priority":Priority,"Duedate":Duedate,"Status":Status}
          tasks.append(in_dict)
          choice=input("Do you want to add new task again[Yes/No]")
          if choice.upper()=='NO':
            loop_status=False
            print(tasks,end="\n")
add_tasks()