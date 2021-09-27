years = int(input())
print("exhibits =", (years * 365 * 8 * 60) // 5)
exhibit = int(input())
minutes = ((exhibit * 5))
days = (minutes // (8 * 60))
print("years =", (days // 365), "days=", days % 365,
      "minutes =", minutes % (8 * 60))
