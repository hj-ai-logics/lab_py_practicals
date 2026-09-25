seats = [
    ["O","O","O"],
    ["O","X","O"],
    ["O","O","X"]
]

for row in seats:
    print(row)

r = int(input("Enter row (1-3): ")) - 1
c = int(input("Enter column (1-3): ")) - 1

if seats[r][c] == "O":
    seats[r][c] = "X"
    print("Seat Reserved")
else:
    print("Already Reserved")
