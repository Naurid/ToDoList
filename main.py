from Functions import GetList, WriteList, DisplayList, GetIndex
import time

time = time.strftime("%H:%M:%S %d/%m/%Y")
print(time)
while True:
    userAction = input("Type add, show, edit, complete, done or exit ")
    userInput = userAction.split(" ")
    userOrder = userInput[0]

    if "add" in userOrder:
        onGoingTasks = GetList("Files/Todos.txt")
        userAction = userAction.strip("add").strip()
        userAction = userAction.capitalize()
        onGoingTasks.append(f"{userAction}\n")
        WriteList("Files/Todos.txt", onGoingTasks)
    elif "show" in userOrder:
        onGoingTasks = GetList("Files/Todos.txt")
        DisplayList(onGoingTasks)
    elif "edit" in userOrder:
        if len(userInput) == 1:
            onGoingTasks = GetList("Files/Todos.txt")
            DisplayList(onGoingTasks)
            index = GetIndex("edit")
            onGoingTasks[index] = input("New task ") + "\n"
            WriteList("Files/Todos.txt", onGoingTasks)
        else:
            onGoingTasks = GetList("Files/Todos.txt")
            taskToEdit = userAction.strip("edit").strip()
            taskToEdit = taskToEdit.capitalize() + "\n"
            if taskToEdit not in onGoingTasks:
                print("No such task in TODO List")
                continue
            onGoingTasks[onGoingTasks.index(taskToEdit)] = (input("New Task: ") + "\n").capitalize()
            WriteList("Files/Todos.txt", onGoingTasks)
    elif "complete" in userOrder:
        if len(userInput) == 1:
            onGoingTasks = GetList("Files/Todos.txt")
            DisplayList(onGoingTasks)
            index = GetIndex("complete")
            doneTasks = GetList("Files/DoneTasks.txt")
            doneTasks.append(onGoingTasks[index])
            onGoingTasks.remove(onGoingTasks[index])
            WriteList("Files/DoneTasks.txt", doneTasks)
            WriteList("Files/Todos.txt", onGoingTasks)
        else:
            onGoingTasks = GetList("Files/Todos.txt")
            taskToComplete = userAction.strip("complete").strip()
            taskToComplete = taskToComplete.capitalize() + "\n"
            doneTasks = GetList("Files/DoneTasks.txt")
            doneTasks.append(onGoingTasks[onGoingTasks.index(taskToComplete)])
            onGoingTasks.remove(onGoingTasks[onGoingTasks.index(taskToComplete)])
            WriteList("Files/DoneTasks.txt", doneTasks)
            WriteList("Files/Todos.txt", onGoingTasks)
    elif "done" in userOrder:
        doneTasks = GetList("Files/DoneTasks.txt")
        DisplayList(doneTasks)
    elif "exit" in userOrder:
        break
    else:
        print("This command is not valid")

print("Exiting program...")
