import json


def Text_up(text):
    return list(map(lambda x: x.upper(), text.split()))


def Crypt_Caesar(text, key=1):
    text = Text_up(text)

    text_true = []
    for word in text:
        final = ''
        for symbol in word:
            final += chr((ord(symbol) + key - 13) % 26 + ord('A'))
        text_true.append(final)

    if len(text_true) != 0:
        return ' '.join(text_true)
    else:
        return 'Введите данные корректно'


def Decrypt_Caesar(text, key=1):
    text = Text_up(text)

    text_true = []
    for word in text:
        final = ''
        for symbol in word:
            final += chr((ord(symbol) - key - 13) % 26 + ord('A'))
        text_true.append(final)
    if len(text_true) != 0:
        return ' '.join(text_true)
    else:
        return 'Введите данные корректно'


def Decrypt_Vegenere(text, key='A'):
    text_full = Text_up(text)
    text_true = []
    for word in text_full:
        key *= len(word) // len(key) + 1
        d = ""
        key = key.upper()
        for i, j in enumerate(word):
            gg = (ord(j) + ord(key[i]))
            d += chr(gg % 26 + 65)
        text_true.append(d)

    if len(text_true) != 0:
        return ' '.join(text_true)
    else:
        return 'Введите данные корректно'


def Crypt_Vigenere(text, key='A'):
    text_full = Text_up(text)
    text_true = []
    for word in text_full:
        key *= len(word) // len(key) + 1
        d = ""
        key = key.upper()
        for i, j in enumerate(word):
            gg = (ord(j) - ord(key[i]))
            d += chr(gg % 26 + 65)
        text_true.append(d)

    if len(text_true) != 0:
        return ' '.join(text_true)
    else:
        return 'Введите данные корректно'


def Crypt_Morze(text):
    text = text.upper()
    with open('import_info.json', 'r', encoding='utf-8') as f_obj:
        CODE = json.load(f_obj)['Morze']

    return ' '.join(CODE.get(i) for i in text)


def Decrypt_Morze(text):
    with open('import_info.json', 'r', encoding='utf-8') as f_obj:
        CODE = json.load(f_obj)['Morze']
    CODE_REVERSED = {value: key for key, value in CODE.items()}

    return ''.join(CODE_REVERSED.get(i) for i in text.split())


def Crypt_replace(text):
    text = Text_up(text)
    text_true = []
    with open('import_info.json', 'r', encoding='utf-8') as f_obj:
        keys = json.load(f_obj)['Replaces_keys']

    for word in text:
        crypt = ""
        for i in word:
            if i in keys:
                crypt += keys[i]
        text_true.append(crypt)

    if len(text_true) != 0:
        return ' '.join(text_true).replace(' ', '~')
    else:
        return 'Введите корректно'


def Decrypt_replace(text):
    text = text.split()
    text_true = []
    with open('import_info.json', 'r', encoding='utf-8') as f_obj:
        keys_0 = json.load(f_obj)['Replaces_keys']
    keys = {value: key for key, value in keys_0.items()}
    for word in text:
        decrypt = ""
        for i in word:
            if i in keys:
                decrypt += keys[i]
        text_true.append(decrypt)

    if len(text_true) != 0:
        return ''.join(text_true).replace('~', ' ')
    else:
        return 'Введите корректно'


def Crypt_omofon(text):
    from random import randint
    text = Text_up(text)
    crypt_full = []
    with open('import_info.json', 'r', encoding='utf-8') as f_obj:
        keys = json.load(f_obj)['Omofon_keys']

    for word in text:
        crypt = ""
        for i in word:
            if i in keys:
                lenght = len(keys[i])
                crypt += keys[i][randint(0, lenght - 1)]
        crypt_full.append(crypt)
    if len(crypt_full) != 0:
        return " ".join(crypt_full)
    else:
        return 'Введите корректно'


def Decrypt_omofon(text):
    text = text.split()
    decrypt_full = []
    with open('import_info.json', 'r', encoding='utf-8') as f_obj:
        keys = json.load(f_obj)['Omofon_keys']
    for word in text:
        decrypt = ""
        for i in word:
            for j in keys:
                if i in keys[j]:
                    decrypt += j
        decrypt_full.append(decrypt)
    if len(decrypt_full) != 0:
        return " ".join(decrypt_full)
    else:
        return 'Введите корректно'


def Crypt_file(file, password):
    import pyAesCrypt
    from os import remove
    bufferSize = 64 * 1024
    pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, bufferSize)
    remove(file)


def Decrypt_file(file, password):
    import pyAesCrypt
    from os import remove
    from os.path import splitext
    bufferSize = 64 * 1024
    pyAesCrypt.decryptFile(str(file), str(splitext(file)[0]), password, bufferSize)
    remove(file)


def Decrypt_Gronsfeld(text, key):
    text_true = []
    text = Text_up(text)
    for message in text:
        key_1 = key
        key_1 *= len(message) // len(key) + 1
        final = ''
        for index, symbol in enumerate(message):
            temp = ord(symbol) - int(key_1[index]) - 13
            final += chr(temp % 26 + ord('A'))
        text_true.append(final)
    if len(text_true) != 0:
        return ' '.join(text_true)
    else:
        return 'Введите данные корректно'


def Crypt_Gronsfeld(text, key):
    text_true = []
    text = Text_up(text)
    for message in text:
        key_1 = key
        key_1 *= len(message) // len(key) + 1
        final = ''
        for index, symbol in enumerate(message):
            temp = ord(symbol) + int(key_1[index]) - 13
            final += chr(temp % 26 + ord('A'))
        text_true.append(final)

    if len(text_true) != 0:
        return ' '.join(text_true)
    else:
        return 'Введите данные корректно'


def Crypt_pseudosim(text):
    with open('import_info.json', 'r', encoding='utf-8') as f_obj:
        keys = json.load(f_obj)['Pseudosim_keys']
    text_true = []
    text = Text_up(text)
    for message in text:
        final = ''
        for symbol in message:
            if symbol in keys:
                final += keys[symbol]
        text_true.append(final)

    if len(text_true) != 0:
        return ''.join(text_true)
    else:
        return 'Введите данные коректно'


def Decrypt_pseudosim(text):
    def regular(text):
        from re import findall
        template = r"\w{3}"
        return findall(template, text)

    with open('import_info.json', 'r', encoding='utf-8') as f_obj:
        keys = json.load(f_obj)['Pseudosim_keys']
    final = ''
    for threeSymbols in regular(text):
        for key in keys:
            if threeSymbols == keys[key]:
                final += key

    if len(final) != 0:
        return final
    else:
        return 'Введите данные коректно'


def Derypt_Binary_code(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


def Crypt_Binary_code(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
