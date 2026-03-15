filename="task.text"

print("|____________What new tasks you wan't to save now😊😊_____________|")

task= []

print("1.Add new tasks.")
print("2.Remov the task.")
print("3.End code")


choice= int(input("Select the task number you wan't to run(1 to 3): "))

number_of_task= int(input("How many taks are there which you wan't to add or remove: "))

if choice==1:
    for i in range(0,number_of_task):
        new_element=input("Enter new task: ")
        
        task.append(new_element)
        
    print(task)
elif choice==2:
    for i in range(0,number_of_task):
        index= int(input("Task number you wan't to remove: "))
        
        task.pop(index)
        
    print(task)
elif choice== 3:
        print("End Task.")
else:
        
        print("Invalid Input.")

print("|_______________________________________Code ended___________________________________________________________|")