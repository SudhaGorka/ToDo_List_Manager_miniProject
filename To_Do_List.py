#To-Do_List Manager Program in Python:
to_do_list=[]

def display_list(to_do_list):
    print("ToDo List")
    for task in to_do_list:
        print(task)

def add_task(to_do_list,task):
    to_do_list.append(task)
    print(task," is added to the ToDo List")

def completion(to_do_list,completed_task):
    if completed_task in to_do_list:
        to_do_list.remove(completed_task)
        print(task,"is removed from the list")
    else:
        print("task not found in the list")
while True:
    print("Here is the Menu: ")
    print("1 - Add Task")
    print("2 - Display ToDo List")
    print("3 - Completed Task")
    print("4  - Quiting")

    n=int(input("Enter a number from 1-4: "))
   

    if n==1:
        task=input("Enter the Task: ")
        add_task(to_do_list,task)
        
    
    elif n==2:
        display_list(to_do_list)
    
    elif n==3:
        completed_task=input("Enter the Task which you completed: ")
        completion(to_do_list,completed_task)
    
    elif n==4:
        print("You Successfully Quit the ToDo List, GoodBye!")
        break
    else:
        print("Invalid! You Entered wrong input")

    
    

    







    
    
    


    
