# fazer funcao pra calcular o gasto
# fazer funcao pro menu
# garantir que letras minusculas e maiusculas sejam aceitas
# simular tempo de espera pro calculo ( enfeite )
import time

# fucao pro gasto 
def calcular_gasto_calorico(peso, genero, frequencia):
    if genero == 'H':
        base = (0.063 * peso + 2.896) * 239
    else:  # genero == 'M'
        base = (0.062 * peso + 2.036) * 239

    fatores = {
        'L': 1.11,
        'M': 1.25,
        'I': 1.48
    }
    return base * fatores[frequencia]

# funcao pro menu
def main():
    escolha = input('[E]ntrar [S]air \n').strip().upper() # garantir que letras minusculas e maiusculas sejam aceitas

    while escolha == 'E':
        nome = input('Qual seu nome? ')
        idade = int(input('Qual sua idade? '))
        peso = float(input('Qual seu peso (kg)? '))
        altura = float(input('Qual sua altura (cm)? '))
        genero = input('Qual seu gênero, [H]omem ou [M]ulher? ').strip().upper()
        frequencia = input(
            'Sua frequência de atividade física é [L]eve, [M]oderada ou [I]ntensa? '
        ).strip().upper()

        print("\nCalculando...\n")  # simular tempo de espera pro calculo
        time.sleep(2)

        gasto = calcular_gasto_calorico(peso, genero, frequencia)
        print(f"{nome}, seu gasto calórico diário é de {gasto:.2f} kcal.\n")

        escolha = input('[RE]petir [S]air \n').strip().upper()


if __name__ == "__main__":
    main()