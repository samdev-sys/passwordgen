import pyshorteners
import pyshorteners.shorteners


url=input("ingresa url:\n")

print("url recortada:",pyshorteners.Shortener().tinyurl.short(url))
