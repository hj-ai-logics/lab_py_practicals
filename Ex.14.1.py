# Survey Analytics Tool

products = ["Laptop", "Mobile", "Tablet", "Laptop", "Mobile",
            "Laptop", "Tablet", "Mobile", "Laptop"]

votes = {}

for product in products:
    votes[product] = votes.get(product, 0) + 1

print("Survey Results:")
for product, count in votes.items():
    print(product, ":", count, "votes")

winner = max(votes, key=votes.get)

print("\nWinner:", winner)
print("Total Votes:", votes[winner])
