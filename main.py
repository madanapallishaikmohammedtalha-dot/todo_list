from menu import show_menu
from add_task import add_task
from view_tasks import view_tasks
from delete_task import delete_task

while True:
    show_menu()
    c = input("Choice: ")
    if c == "1":
        add_task()
    elif c == "2":
        view_tasks()
    elif c == "3":
        delete_task()
    elif c == "4":
        break