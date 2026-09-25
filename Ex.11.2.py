schedule = [
    ["Math","Python","DS"],
    ["OS","AI","Math"],
    ["Python","DS","OS"]
]

for row in schedule:
    print(row)

r = int(input("Enter row (1-3): ")) - 1
c = int(input("Enter column (1-3): ")) - 1

print("Current:", schedule[r][c])

schedule[r][c] = input("Enter new subject: ")
print("Updated:", schedule[r][c])
