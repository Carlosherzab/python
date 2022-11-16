
e = int(input("Dime la nota del examen"))
i = int(input("Dime la nota del hito individual"))
g = int(input("Dime la nota del hito grupal"))


notas = ((e*0.50) + (i*0.30) + (g*0.20))

print(f'La nota media es {notas}')
