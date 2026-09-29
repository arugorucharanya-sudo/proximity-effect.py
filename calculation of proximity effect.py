Proximity Effect Calculation

 Input values
Rdc = float(input("Enter DC resistance of conductor (ohm): "))
k = float(input("Enter proximity effect factor: "))

 Calculate AC resistance
Rac = Rdc * (1 + k)

 Calculate percentage increase
percentage_increase = ((Rac - Rdc) / Rdc) * 100

 Display results
print("\n--- Proximity Effect Calculation ---")
print("DC Resistance =", Rdc, "ohm")
print("Proximity Effect Factor =", k)
print("AC Resistance =", round(Rac, 4), "ohm")
print("Increase in Resistance =", round(percentage_increase, 2), "%")
