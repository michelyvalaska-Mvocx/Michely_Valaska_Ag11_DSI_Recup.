from colorama import init, Fore, Style
init(autoreset=True)

# Lista com as mensagens dos níveis
niveis = [
    "Muito baixo (crítico)",
    "Baixo",
    "Médio",
    "Alto",
    "Muito alto (alerta)"
]

# Função que define a cor conforme o nível
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

# Simulação - exibe todos os níveis
print("=== Monitoramento do Reservatório ===")
for nivel in range(1, 6):
    cor = definir_cor(nivel)
    mensagem = niveis[nivel - 1]
    print(f"{cor}Nível {nivel} - {mensagem}{Style.RESET_ALL}")

print("Monitoramento finalizado.")
