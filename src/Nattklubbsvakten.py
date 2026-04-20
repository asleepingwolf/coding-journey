print("Välkommen til klubb python!")
name = input("Vad heter du? ")
age = input("Hur gammal är du? ")
if int(age) > 17:
    print("Välkommen in", name,'!')
elif name == "VIP":
    print("Välkommen in!")
else:
    print("Kom tillbaka när du är över 18!")