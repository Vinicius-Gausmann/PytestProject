from cryptographyFramework import *

initializeRead()
user = "Fulano"
password = "1234"
line1 = readNextLine()
print(line1)
print(decryptMessage(user, password, line1))
line2 = readNextLine()
print(line2)
print(decryptMessage(user, password, line2))
line3 = readNextLine()
print(line3)
print(decryptMessage(user, password, line3))