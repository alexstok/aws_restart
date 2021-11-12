# python3.6
# coding: utf-8

# armazenar a sequência de pré-pró-insulina humana em uma variável chamada pré-pró-insulina:
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# armazenar os restantes elementos da sequência de insulina humana em variáveis:
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = "giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"
insulin = bInsulin + aInsulin

## Armazene valores AA pKR e termos N / C em dicionários:
pKR = {'y':10.07,'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}

## Conte a ocorrência de cada pKR AA na sequência e anexe os termos N/C:
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

## Calcule a carga líquida de acordo com a equação de Henderson-Hesselbach:
pH = 0
while (pH <= 14):
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) for x in ['y','c','d','e']}.values()))
    )
    print ('{0:.2f}'.format(pH), netCharge)
    pH = pH + 1