# Program Assignment 6: Corrosion Risk Assessment
humidity = float(input("Enter Relative Humidity (%): "))
temperature = float(input("Enter Temperature (°C): "))
pH = float(input("Enter pH value: "))
salt = input("Is salt present? (Yes/No): ").strip().lower()

risk = "Low"

if humidity > 70 and temperature > 30:
    risk = "Moderate"
if humidity > 80 and (pH < 5 or pH > 9 or salt == "yes"):
    risk = "High"

print(f"Corrosion Risk: {risk}")
