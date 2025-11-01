#Limpieza de texto
#Corrige esta cadena:
#texto = "   \n\tPython es increíble\t\n   "

texto = "   \n\tPython es increíble\t\n   "

print(texto.strip().removesuffix("\t\n").removeprefix("\t"))