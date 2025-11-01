bicycles = ["trek", "cannodable", "redline", "specialized"]
print(bicycles)

##Para trabajar con un elemento de la lista:
print(bicycles[0].title())

#Para mostrar el ultimo elemento (-1)
print(bicycles[-1].title())

#Usar valores individuales de una lista
bicycles = ["trek", "cannodable", "redline", "specialized"]
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)