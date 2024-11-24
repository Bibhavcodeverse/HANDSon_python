letter= "Hey my name is {1} and I am from {0}"

country ="Indian"
name="Harry"

print(letter.format(country,name))

print(f"Hey my name is {name} and I am from {country}")

price =49.09999

txt = f"For only {price: .2f} dollars!"

print(txt)

print(type(f"{2*30}"))
