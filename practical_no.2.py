# Develop a “Simple Billing Calculator” for a grocery shop to calculate total bill, discount, and final payable amount.
# Arithmetic operators, relational operators, logical operators, input/output

# --- Item Inputs and Subtotals ---
wheat_qty = float(input("Enter the quantity of wheat (in kg): "))
wheat_price_per_kg = 50
net_wheat = wheat_qty * wheat_price_per_kg

maize_qty = float(input("Enter the quantity of maize (in kg): "))
maize_price_per_kg = 20
net_maize = maize_qty * maize_price_per_kg

sugar_qty = float(input("Enter the quantity of sugar (in kg): "))
sugar_price_per_kg = 45
net_sugar = sugar_qty * sugar_price_per_kg

tea_powder_qty = float(input("Enter the quantity of tea powder (in kg): "))
tea_powder_price_per_kg = 100
net_tea_powder = tea_powder_qty * tea_powder_price_per_kg

# --- Total Calculation ---
total_bill = net_wheat + net_maize + net_sugar + net_tea_powder

# --- Bill Details Display ---
print("\n" + "*"*20 + " BILL DETAIL " + "*"*20)
print(f"Wheat       = {net_wheat}")
print(f"Maize       = {net_maize}")
print(f"Sugar       = {net_sugar}")
print(f"Tea powder  = {net_tea_powder}")
print("*"*53)

# --- Discount Logic ---
if total_bill >= 1000:
    discount_percent = 0.10
elif total_bill >= 500:
    discount_percent = 0.05
else:
    discount_percent = 0.02

discount_amount = total_bill * discount_percent
final_bill = total_bill - discount_amount

# --- Final Output ---
print(f"Total Bill: {total_bill}")
print(f"Discount ({int(discount_percent * 100)}%): {discount_amount}")
print(f"Final bill of grocery: {final_bill}")
