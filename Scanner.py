import socket

def escanear_portas(ip, porta_inicio, porta_fim, timeout):
    print(f"\n[+] Escaneando {ip} da porta {porta_inicio} até {porta_fim}...\n")
    portas_abertas = []

    for porta in range(porta_inicio, porta_fim + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        resultado = s.connect_ex((ip, porta))
        if resultado == 0:
            try:
                servico = socket.getservbyport(porta)
            except:
                servico = "Desconhecido"
            print(f"[ABERTA] Porta {porta} ({servico})")
            portas_abertas.append(porta)
        else:
            print(f"[FECHADA] Porta {porta}")
        s.close()

    print(f"\n[+] Escaneamento finalizado. Portas abertas: {len(portas_abertas)}")

def main():
    ip = input("Digite o IP ou domínio alvo: ")
    try:
        porta_inicio = int(input("Digite a porta inicial: "))
        porta_fim = int(input("Digite a porta final: "))
        timeout = float(input("Digite o timeout (segundos, ex: 1.0): "))
    except ValueError:
        print("Erro: Insira números válidos para portas e timeout.")
        return

    if porta_inicio < 1 or porta_fim > 65535 or porta_inicio > porta_fim:
        print("Erro: Intervalo de portas inválido.")
        return

    escanear_portas(ip, porta_inicio, porta_fim, timeout)

if __name__ == "__main__":
    main()
