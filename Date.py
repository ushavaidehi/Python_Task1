from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("date type 1 =", d1)

# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("date type 2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("date type 3 =", d3)

# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("date type 4 =", d4)