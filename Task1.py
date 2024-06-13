class Task1:
    def display_menu():
        print("menu:-")
        print("1: add task")
        print("2: view tasks")
        print("3: mark as done")
        print("4: exit")

    def add(tasks):
        task = input("enter about the task: ")
        tasks.append(task)
        print("task has been added")

    def view(tasks):
        print("\ntasks:")
        for x, task in enumerate(tasks, start=1):
            print(f"{x}. {task}")

    def mark_done(tasks):
        if not tasks:
            print("nothing to mark as done")
            return

        Task1.view(tasks)
        index = int(input("enter task index to mark as done: ")) - 1

        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"task '{removed_task}' marked as done and removed")
        else:
            print("not valid")

    def save(tasks):
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + '\n')

    def load():
        try:
            with open("tasks.txt", "r") as f:
                return f.read().splitlines()
        except FileNotFoundError:
            return []

    def main():
        tasks = Task1.load()

        while True:
            Task1.display_menu()

            option = input("choose your option: ")

            if option == '1':
                Task1.add(tasks)
            elif option == '2':
                Task1.view(tasks)
            elif option == '3':
                Task1.mark_done(tasks)
            elif option == '4':
                Task1.save(tasks)
                print("exiting")
                break
            else:
                print("option chosen is not valid, select again")

if __name__ == "__main__":
    Task1.main()
