from __init__ import encryptor, decryptor
choice = str(f'{input("Message: ")}')
shift = int(input("Shift Offset: "))

app = encryptor(shift)
mes = app.encrypt(choice)
print(mes)
