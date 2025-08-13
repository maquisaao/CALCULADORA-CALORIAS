# 🏋️‍♂️ Calculadora de Gasto Calórico Diário

Este projeto é um simples **programa em Python** que calcula o **gasto calórico diário** de uma pessoa com base em **peso, altura, idade, gênero** e **frequência de atividade física**.

---

## 📌 Funcionalidades
- Solicita os dados do usuário:
  - Nome
  - Idade
  - Peso
  - Altura
  - Gênero (Homem/Mulher)
  - Frequência de atividade física (Leve, Moderada ou Intensa)
- Calcula automaticamente o **consumo calórico diário** usando fórmulas específicas para cada gênero e nível de atividade.
- Permite repetir o cálculo ou encerrar o programa.

---

## 🧮 Fórmula Utilizada
- Para **Homens**:  
  `((0.063 * peso) + 2.896) * 239 * Fator_Atividade`
- Para **Mulheres**:  
  `((0.062 * peso) + 2.036) * 239 * Fator_Atividade`

**Fator de Atividade:**
| Frequência | Fator |
|------------|-------|
| Leve       | 1.11  |
| Moderada   | 1.25  |
| Intensa    | 1.48  |

---

## 💻 Exemplo de Uso
```bash
[E]ntrar [S]air
E
Qual seu nome? Ana
Qual sua idade? 28
Qual seu peso? 60
Qual sua altura? 1.65
Qual seu gênero, [H]omem ou [M]ulher? M
Sua frequencia de atividade fisica é [L]eve, [M]oderada ou [I]ntensa? M

Ana, seu gasto calorico diario é de 2035.40.
[RE]petir [S]air
