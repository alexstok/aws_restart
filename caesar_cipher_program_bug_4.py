# Module Lab 6: Caesar Cipher Program Solution For Instructor
#
# No Módulo Lab 6, o aluno é solicitado a depurar 4 versões diferentes do
# Programa Caesar Cipher abordado no Laboratório de Módulo 4.
#
# O aluno deve usar o depurador para ajudá-los a corrigir cada versão do
# programa.
#
# Abaixo, cada bug é comentado e junto com as linhas corretas e incorretas.

# Dobre o alfabeto fornecido.
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Receba uma mensagem para criptografar.
def getMessage():
    stringToEncrypt = input("Por favor, insira uma mensagem para criptografar: ")
    return stringToEncrypt

# Obtenha uma chave de cifra.
def getCipherKey():
    shiftAmount = input("Por favor, insira uma chave (número inteiro de 1-25): ")
    return shiftAmount

# Criptografar Mensagem
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    # Bug #2: A chamada para o superior() está desaparecido.
    uppercaseMessage = message.upper() # Correto
    #uppercaseMessage = message # Incorrecto
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        # Bug #1: String não está sendo convertida em um inteiro.
        newPosition = position + int(cipherKey) # Correcto
        #newPosition = position + cipherKey # Incorrecto
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

# Decrypt Message
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    # Bug #3: Passing in cipherKey instead of decryptKey.
    return encryptMessage(message, decryptKey, alphabet) # Correct
    #return encryptMessage(message, cipherKey, alphabet) # Incorrect

# Lógica do programa principal.
def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    # Bug #4: Print myEncryptedMessage em vez de myDecryptedMessage
    print(f'Decrypted Messgae: {myDecryptedMessage}') # Correcto
    #print(f'Decrypted Messgae: {myEncryptedMessage}') # Incorrecto

# Main Logic
runCaesarCipherProgram()