from tasks import tasks
def view_tasks():
    for i, t in enumerate(tasks):
        print(i+1, t)