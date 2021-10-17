import pyshorteners


link = input("Coloque a URL: ")

shortener = pyshorteners.Shortener()

linkReduzido = shortener.tinyurl.short(link)

print(linkReduzido)

