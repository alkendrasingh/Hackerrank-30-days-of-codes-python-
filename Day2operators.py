mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

totalCost = mealCost * (100 + tipPercent + taxPercent) / 100.0

print(str(round(totalCost)))
