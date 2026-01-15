import nmap
import google.generativeai as genai
import traceback

# --- CONFIGURAÇÃO ---
# COLE SUA CHAVE DO GEMINI ABAIXO DENTRO DAS ASPAS
MINHA_API_KEY = "" 

# Configura o Gemini
genai.configure(api_key=MINHA_API_KEY)

# Usa o modelo Gemini 2.5 Flash 
try:
    model = genai.GenerativeModel('gemini-2.5-flash')
except:
    # Fallback se der erro no modelo novo
    model = genai.GenerativeModel('gemini-1.5-flash')

def realizar_scan(ip_alvo):
    print(f"\n[1/3] Iniciando Scan no alvo: {ip_alvo}...")
    print("      (Aguarde... o Nmap está trabalhando)")
    
    nm = nmap.PortScanner()
    
    try:
        # Scan sem Ping (-Pn), com Versão (-sV) e Rápido (-F)
        nm.scan(ip_alvo, arguments='-Pn -sV -F')
    except Exception as e:
        print(f"Erro crítico ao chamar Nmap: {e}")
        return None

    lista_hosts = nm.all_hosts()
    if not lista_hosts:
        print("Erro: O Nmap rodou mas não retornou nenhum IP.")
        return None
    
    host_encontrado = lista_hosts[0]
    print(f"      -> Alvo identificado: {host_encontrado}")

    resultados = []
    
    # Varredura de protocolos
    if host_encontrado in nm.all_hosts():
        for proto in nm[host_encontrado].all_protocols():
            lport = nm[host_encontrado][proto].keys()
            for port in lport:
                estado = nm[host_encontrado][proto][port]['state']
                servico = nm[host_encontrado][proto][port]['name']
                versao = nm[host_encontrado][proto][port].get('product', '') + " " + nm[host_encontrado][proto][port].get('version', '')
                
                if estado == 'open':
                    info = f"Porta: {port}/{proto} | Serviço: {servico} | Versão: {versao}"
                    resultados.append(info)
                    print(f"      [+] Porta ABERTA: {port} ({servico})")
    
    return resultados

def consultar_gemini(dados_scan):
    print("\n[2/3] Enviando dados para a Inteligência Artificial...")
    
    if not dados_scan:
        return "Nenhuma vulnerabilidade crítica detectada nas portas principais."

    texto_scan = "\n".join(dados_scan)
    
    prompt = f"""
    Atue como Especialista em Cibersegurança. Analise este scan:
    {texto_scan}
    
    Gere um relatório curto com:
    1. Riscos de cada porta aberta.
    2. Soluções práticas.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro na IA: {e}"

def main():
    try:
        print("--- SCANNER DE VULNERABILIDADES + IA (VERSÃO 1.0) ---")
        
        # Pergunta o IP
        ip = input("Digite o IP alvo (Ex: scanme.nmap.org): ").strip()
        if not ip: ip = "scanme.nmap.org"

        # Executa
        resultados = realizar_scan(ip)
        
        if resultados:
            analise = consultar_gemini(resultados)
            print("\n" + "="*60)
            print("[3/3] RELATÓRIO DE INTELIGÊNCIA:")
            print("="*60)
            print(analise)
            print("="*60)
        else:
            print("\n[!] Nenhuma porta 'open' encontrada para análise.")

    except Exception as e:
        print(f"\n[!!!] ERRO FATAL: {e}")
        traceback.print_exc()

    finally:
        print("\n------------------------------------------------")
        input("Pressione ENTER para fechar o programa...")

if __name__ == "__main__":
    main()