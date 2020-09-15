'''3. Crie as funções abaixo e teste-as no interpretador.
a. Faça uma função que receba uma string e retorna uma string com os caracteres de
índices pares
b. Faça uma função que receba uma string e retorne uma cópia desta string invertida
c. Faça uma função que recebe o nome de uma pessoa e a data de nascimento
('dd/mm/aaaa' ), crie e retorne sua senha de acordo com a seguintes regra:
caracteres dos índices pares + dia do nascimento invertido +
caracteres dos índices pares invertidos
Exemplo: senha('Patinhas', '25/12/1900')  'Ptna52antP'
Faça um programa que pergunte o nome de uma pessoa e a data de nascimento
('dd/mm/aaaa'), mostrando a senha de acordo com a regra acima.'''
#---------------------------------------------------------------------------------
def RetornarCaracterIndicePar(texto):
    return texto[::2]

print(RetornarCaracterIndicePar('ABCD'))