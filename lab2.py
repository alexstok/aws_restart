#python3.6
#coding: utf-8

# armazenar a sequência de pré-pró-insulina humana em uma variável chamada pré-pró-insulina:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# armazenar os restantes elementos da sequência de insulina humana em variáveis:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"


# Imprimir "a sequência de insulina humana" para o console usando comandos print()
print("A sequência da pré-pró-insulina humana: ")
print(preproInsulin)

# Impressão para console usando strings concatenadas
bInsulinPrint = "A sequência da cadeia b da insulina humana: " + bInsulin
print(bInsulinPrint)

# Impressão usando strings concatenadas dentro da função print (one-liner)
print("A sequência da cadeia a da insulina humana: " + aInsulin)

# Concatenando a cadeia b com a cadeia a para formar o peptídeo de insulina humana
insulin = bInsulin + aInsulin
print("A sequência da insulina humana: " + insulin)

# Calculando o peso molecular da insulina
# Criação de uma lista de pesos de aminoácidos (AA)
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19, 'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19}
        
# Conte o número de cada aminoácido
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']})

# Multiplique a contagem pelos pesos
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']}.values())

print("O peso molecular aproximado da insulina: " + str(molecularWeightInsulin))

# Calculando a porcentagem de erro
molecularWeightInsulinActual = 5807.63
print("Erro percentual: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))