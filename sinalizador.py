import requests
import ipaddress

def buscar_dados(alvo):
    """
    Recebe um IP ou domínio e consulta a geolocalização via IP-API.
    """
    # Tenta validar se é um endereço IP
    try:
        ip = ipaddress.ip_address(alvo)
        
        # Checa se o IP é privado (rede local)
        if ip.is_private:
            print(f"\n[!] {alvo} é um IP PRIVADO (Rede Local).")
            print("Eles não possuem localização pública, pois existem em cada casa!")
            return
    except ValueError:
        # Se não for um IP, assume que é um domínio (ex: google.com)
        pass

    print(f"[*] Consultando: {alvo}...")

    try:
        # Requisição para a API
        url = f"http://ip-api.com/json/{alvo}"
        resposta = requests.get(url, timeout=5)
        dados = resposta.json()

        # Verifica se a API retornou sucesso
        if dados.get('status') == 'success':
            print("\n--- DADOS ENCONTRADOS ---")
            print(f"País: {dados.get('country', 'N/D')}")
            print(f"Região: {dados.get('regionName', 'N/D')}")
            print(f"Cidade: {dados.get('city', 'N/D')}")
            print(f"Provedor: {dados.get('isp', 'N/D')}")
            print("-" * 25 + "\n")
        else:
            print("[!] Não foi possível localizar este alvo.")
            
    except Exception as e:
        print(f"[!] Erro de conexão: {e}")

if __name__ == "__main__":
    entrada = input("Digite o IP ou domínio para consultar: ")
    if entrada:
        buscar_dados(entrada)
