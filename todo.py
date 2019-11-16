
def print_todos(todos, completed_list, pending_list):
    
    pending = '''
    ======= Pending ======
    '''
    completed = '''
    ======= Completed ======
    '''
    
    if len(todos) == 0:
        print("You have nothing to do.")

    else:
         

        print(pending)
        for i, pending in enumerate(pending_list):
            print(f"{i}: {pending['title']}")

        print(completed)
        for i, completed in enumerate(completed_list):
            print(f"{i}: {completed['title']}")

def split_list(todos):
    completed_list = []
    pending_list = []
    for todo in todos:
        if todo['completed'] == True:
            completed_list.append(todo)
        else:
            pending_list.append(todo)
        
    return completed_list, pending_list


def add_todo(todos, item):


    dict_entry = {'title': item,'completed': False}
    todos.append(dict_entry)
   
  

def change_status(todos, index):
    try:
        todos[index]['completed'] = True
            
       
        
    except IndexError:
        print("That todo does not exist.")

def print_menu():
    message = """
    Todo App
==================
0. quit
1. print todos
2. add a todo
3. complete a todo
"""
    print(message)

def get_choice(prompt="Choose one: "):
    is_valid_choice = False
    choice = 0
    while not is_valid_choice:
        try:    
            choice = int(input(prompt))
            is_valid_choice = True
        except ValueError:
            print("Please enter a number.")
    return choice
    
def main():
    todo_list = []

    
    is_running = True
    while is_running:
        print_menu()
        choice = get_choice()
        if choice == 0:
            print("K. Byeeee!")
            is_running = False
        elif choice == 1:
            print_todos(todo_list, completed_list, pending_list)
        elif choice == 2:
            new_todo = input("Enter a todo: ")
            add_todo(todo_list, new_todo)
        elif choice == 3:            
            index = get_choice("Enter the index to complete: ")
            change_status(todo_list, index)
    return todo_list

todo_list = main()

