# Log Viewer Utility

def view_log():
    try:
        with open("diary.txt", "r") as file:
            lines = file.readlines()

        print("\n----- Log Contents -----")

        for line in lines:
            print(line, end="")

        print("\nTotal number of lines:", len(lines))

    except FileNotFoundError:
        print("Error: File not found!")


view_log()
