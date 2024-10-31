def convert_f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
f2 = float(input('Temp in fahrenheit: '))
if f2 < -459.67:
    print("Temp is too low")
    quit()
c2 = convert_f_to_c(f2) #I did this as a guess, but I'm not 100% on why it works
print(f2, 'Degrees Celsius')