# fazer menu de entrada e receber os dados do usuario: Nome, Idade, Peso, Altura, Gênero e Frequencia de atividade fisica
escolha = input('[E]ntrar [S]air \n')
while 'E' in escolha:

    nome = input('Qual seu nome? ')
    idade = input('Qual sua idade? ')
    peso = input('Qual seu peso? ')
    altura = input('Qual sua altura? ')
    genero = input('Qual seu gênero, [H]omem ou [M]ulher? ')
    frequencia_fisica = input(
        'Sua frequencia de atividade fisica é [L]eve, [M]oderada ou [I]ntensa? ')

# pela atividade fisica e genero, multiplicar pelo valor
#printar o resultado junto com o nome do usuario

