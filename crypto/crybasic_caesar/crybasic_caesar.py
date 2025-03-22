def decrypt(key: int, message: str) -> str:
    message = message.upper()
    russian_lowercase = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alpha = russian_lowercase.upper()
    result = ""

    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) - key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            # Preserve spaces and punctuation
            result = result + letter

    return result

encrypted_message = "Дгьшефцагё! Иафч: шщцужр цгёщбр жеэ гшэв жеэ жеэ ёщбр гшэв шцф жеэ!"

for key in range(1, 34):
    decrypted_message = decrypt(key, encrypted_message)
    print(f"Encrypted: {encrypted_message}")
    print(f"Decrypted: {decrypted_message}\n")
