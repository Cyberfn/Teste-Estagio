def inverter_string(s):
    inversa = ""
    for char in s:
        inversa = char + inversa
    return inversa

string = input("Informe uma string para ser invertida: ")
string_invertida = inverter_string(string)

print(f"String invertida: {string_invertida}")
