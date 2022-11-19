from MensagemNamorados import MensagemDiaDosNamorados
from MensagemNatal import MensagemNatal
from MensagemAniversario import MensagemAniversario

listMsg = []
m1 = MensagemDiaDosNamorados('Artur', 'Valéria')
m2 = MensagemNatal('Demétrios', 'Aluísio')
m3 = MensagemAniversario('Iara', 'Valéria')

listMsg.append(m1)
listMsg.append(m2)
listMsg.append(m3)

for msg in listMsg:
    print(msg)
