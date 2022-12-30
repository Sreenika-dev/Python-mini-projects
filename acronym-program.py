inPhrase =  input("Enter your full phrase here: ")
splitPhrase = inPhrase.split()
storeAcr = ""

for item in splitPhrase:
    storeAcr += item[0].upper()
print(storeAcr)