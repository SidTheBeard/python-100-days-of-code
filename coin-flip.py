import random

def coin_flip():
	flip = random.randint(0, 1)

	return "Heads" if flip == 0 else "Tails"
	
print(coin_flip())