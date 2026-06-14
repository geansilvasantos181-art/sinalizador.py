
import requests
import ipaddress

def buscar_dados(alvo):
    # Tenta validar se é um IP
    try:
        ip = ipaddress.ip_address(alvo)

        # Se for IP, checa se é privado
        if ip.is_private:
            print(f"\n[!] O IP {alvo} é um IP PRIVADO >
            print("Eles não possuem localização públic>
            return # Para o script aqui
    except ValueError:
        # Se não for um IP, assume que é um domínio (e>
        pass

    # Se não for privado (ou for um domínio), segue a >
    print(f"[*] Consultando: {alvo}...")
    try:
        url = f"http://ip-api.com/json/{alvo}"
        resposta = requests.get(url, timeout=5)
        dados = resposta.json()

        if dados.get('status') == 'success':
            print("\n--- DADOS ENCONTRADOS ---")
            print(f"País: {dados['country']}")
            print(f"Região: {dados['regionName']}")
            print(f"Cidade: {dados['city']}")
            print(f"Provedor: {dados['isp']}")
            print("-------------------------\n")
        else:
            print("[!] Não foi possível localizar este>
    except Exception as e:
        print(f"[!] Erro de conexão: {e}")

if __name__ == "__main__":
    entrada = input("Digite o IP ou domínio para consu>
    buscar_dados(entrada)
