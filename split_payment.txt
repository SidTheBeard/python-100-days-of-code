def payment_split():
	total = input("What was the total of the bill?")
	total = float(total)
	split_ways = input("How many of you are splitting the bill?")
	split_ways = float(split_ways)
	one_part = total / split_ways
	
	print(f"Each of the {int(split_ways)} people owe ${one_part:.2f}.")

payment_split()