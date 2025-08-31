# fazer funcao pra calcular o gasto
# fazer funcao pro menu
# garantir que letras minusculas e maiusculas sejam aceitas
# simular tempo de espera pro calculo ( enfeite )

# fucao pro gasto 
def calcular_gasto_calorico(peso, genero, frequencia):
    # Constantes diferentes para homens e mulheres
    if genero == 'H':
        base = (0.063 * peso + 2.896) * 239
    else:  # genero == 'M'
        base = (0.062 * peso + 2.036) * 239

    # Fatores de multiplicação pela frequência
    fatores = {
        'L': 1.11,
        'M': 1.25,
        'I': 1.48
    }
    return base * fatores[frequencia]

