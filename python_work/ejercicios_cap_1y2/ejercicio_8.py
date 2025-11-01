#Remover prefijos y sufijos
#url = "https://www.python.org/"
#Elimina "https://" y "/" dejando solo:
#"www.python.org"

url = "https://www.python.org/"

print(url.removeprefix("https://").removesuffix("/"))