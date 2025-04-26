task = []

def addTask(taskName):
    task.append(taskName)

for i in range(5):
    taskName = input("Enter task name : ")
    task.append(taskName)

print(task)

taskName = input("Enter task name to remove : ")

task.remove(taskName)
print(task)
