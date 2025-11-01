filename = "python_notes.txt"
print(filename.removesuffix(".txt"))

##con el removesufix() y removeprefix()
filename = "https://python_notes.txt"
resultado = filename.removesuffix(".txt").removeprefix("https://")
print(resultado)