def geometric_progression(start, step):
    current = start
    while True:
        yield current
        current *= step


progression_1 = geometric_progression(-2, -5)
for _ in range(6):
    print(next(progression_1))

print("\n")

progression_2 = geometric_progression(10, 3)
for _ in range(5):
    print(next(progression_2))