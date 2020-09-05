#Em um zoológico, há 15 leões, 26 zebras, 14 macacos e 29 serpentes. Quantos animais há nesse zoológico? Qual o total de patas?

leao = 15
zebra = 26
macacos = 14
serpentes = 29

quantidadeAnimais = leao + zebra + macacos + serpentes

totalDePatas = ((leao + zebra)* 4) + (macacos * 2)

print('Total de Animais: ' + str(quantidadeAnimais))
print('Total de patas do Zoológico: ' + str(totalDePatas))