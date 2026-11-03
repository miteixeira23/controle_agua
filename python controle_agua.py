
from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=True)

# Lista com os níveis do reservatório
niveis = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)"
]

# Função para definir a cor de cada nível
def definir_cor(nivel):

    if nivel == 1:
        return Fore.RED

    elif nivel == 2:
        return Fore.YELLOW

    elif nivel == 3:
        return Fore.GREEN

    elif nivel == 4:
        return Fore.CYAN

    elif nivel == 5:
        return Fore.BLUE

    else:
        return Fore.WHITE


# Simulação dos níveis de água do reservatório
niveis_atuais = [1, 2, 3, 4, 5]

print("===================================")
print(" SISTEMA DE MONITORAMENTO DE ÁGUA")
print("===================================\n")

# Percorre os níveis e exibe os alertas
for nivel in niveis_atuais:

    cor = definir_cor(nivel)

    mensagem = niveis[nivel - 1]

    print(cor + mensagem + Style.RESET_ALL)

print("\nMonitoramento finalizado!")


