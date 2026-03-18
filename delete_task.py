from tasks import tasks
def delete_task():
    n = int(input("Task number: "))
    tasks.pop(n-1)