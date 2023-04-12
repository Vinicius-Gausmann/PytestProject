from cryptographyFramework import *

initializeWrite()
user = "Fulano"
password = "1234"
encryptedText = encryptMessage(user, password, "pytest é dificil")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "HAAAAAAAAAA")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "como eu concerto esse erro???????")
saveNewLine(encryptedText)