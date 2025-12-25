def caesar(text, shift, encrypt=True):
    if not isinstance(shift, int):
        return "Shift must be an integer value"
    if shift < 1 or shift > 25:
        "Shift must be an ingeger between 1 and 25"
    alphabet = "abcdefghijklmnñopqrstuvwxyz"
    if not encrypt:
        shift = - shift 
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text,shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

encrypted_text = encrypt("cacahuate", 7)
print(f"El mensaje encriptado es: {encrypted_text}")

decrypted_text = decrypt(encrypted_text, 7)
print(f"El mensaje desencriptado es: {decrypted_text}")