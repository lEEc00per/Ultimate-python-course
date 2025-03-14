def f_to_c(f):
    return 5*(f-32)/9

f = (int(input("● Enter temperature in F: ")))
c = f_to_c(f)
print(f"✦ Round Figure: {round(c, 2)} °C.")
# OR 
print(f"✦ Correct Measurement: {c}°C")