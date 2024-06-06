def GetList(fileName):
    with open(fileName, "r") as file:
        list = file.readlines()
        file.close()
        return list

def WriteList(fileName, listToWrite):
    with open(fileName, "w") as file:
        file.writelines(listToWrite)
        file.close()

def DisplayList(list):
    for index, item in enumerate(list):
        print(f"{index + 1}.{item.strip("\n").capitalize()}")

def GetIndex(userAction):
    index = int(input(f"Write the index of the task you wish to {userAction}: "))
    index -= 1
    return index