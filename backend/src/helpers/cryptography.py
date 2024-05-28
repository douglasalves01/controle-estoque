import numpy as np

def desc_cripto(descricao):
    print(descricao)
    alfanumerico = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                    'M': 12,
                    'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
                    'Y': 24, 'Z': 25, ' ': 26, '1': 27, '2': 28, '3': 29, '4': 30, '5': 31, '6': 32, '7': 33, '8': 34,
                    '9': 35, '0': 36}
    alfanumerico_invertido = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
                              11: 'L', 12: 'M',
                              13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W',
                              23: 'X',
                              24: 'Y', 25: 'Z', 26: ' ', 27: '1', 28: '2', 29: '3', 30: '4', 31: '5', 32: '6', 33: '7',
                              34: '8',
                              35: '9', 36: '0'}

    matriz_cod = np.array([[2, 1],
                           [7, 4]])
    v = []

    # Ensure length is even
    if len(descricao) % 2 != 0:
        descricao += ' '

    for i in descricao:
        if i in alfanumerico:
            v.append(alfanumerico[i])

    matriz = np.array(v).reshape(2, -1)
    resultado = (np.dot(matriz_cod, matriz)) % 37

    string = ''
    for lin in resultado:
        for col in lin:
            if col in alfanumerico_invertido:
                string += alfanumerico_invertido[col]
    return string

def desc_decripto(string):
    print(string,"teste aqui ")
    alfanumerico = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                    'M': 12,
                    'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
                    'Y': 24, 'Z': 25, ' ': 26, '1': 27, '2': 28, '3': 29, '4': 30, '5': 31, '6': 32, '7': 33, '8': 34,
                    '9': 35, '0': 36}
    alfanumerico_invertido = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K',
                              11: 'L', 12: 'M',
                              13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W',
                              23: 'X',
                              24: 'Y', 25: 'Z', 26: ' ', 27: '1', 28: '2', 29: '3', 30: '4', 31: '5', 32: '6', 33: '7',
                              34: '8',
                              35: '9', 36: '0'}

    matriz_cod = np.array([[4, 36],
                           [30, 2]])
    v = []

    for i in string:
        if i in alfanumerico:
            v.append(alfanumerico[i])

    matriz = np.array(v).reshape(2, -1)
    resultado = (np.dot(matriz_cod, matriz)) % 37

    descricao = ''
    for lin in resultado:
        for col in lin:
            if col in alfanumerico_invertido:
                descricao += alfanumerico_invertido[col]
    
    return descricao

# descricao = input("DE UMA BREVE DESCRIÇÃO DO PRODUTO: ").upper()
# descCripto = desc_cripto(descricao)
# descDecripto = desc_decripto(descCripto)

# print(descricao)
# print(descCripto)
# print(descDecripto)