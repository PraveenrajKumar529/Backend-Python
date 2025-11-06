import random
# Initialize counters
heads = 0
tails = 0

# Simulate 100 coin flips
for i in range(100):
    flip = random.choice(['Heads', 'Tails'])
    if flip == 'Heads':
        heads += 1
    else:
        tails += 1

# Display results
print("🪙 Coin Flip Simulation (100 flips)")
print("--------------------------------")
print(f"Heads: {heads}")
print(f"Tails: {tails}")