P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

SI = (P * R * T) / 100
print(f"Simple Interest: ₹{SI}")


P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

SI = (P * R * T) / 100
CI = P * ((1 + R / 100) ** T) - P

print(f"Simple Interest: ₹{SI}")
print(f"Compound Interest: ₹{CI:.2f}")
