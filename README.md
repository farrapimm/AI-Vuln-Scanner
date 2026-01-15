# AI-Vuln-Scanner
Ferramenta de análise de vulnerabilidades automatizada com Python e IA (Google Gemini).
==========================================================================================================================================


# AI-Powered Vulnerability Scanner (MVP)

Ferramenta de automação de segurança desenvolvida em Python. 
O objetivo é auxiliar analistas de SOC e Blue Team na triagem inicial de ativos, automatizando a varredura de portas e a interpretação de riscos utilizando Inteligência Artificial. (Inicialmente utilizando Gemini, porem o ideal será trabalhar com o Lahma)

## Funcionalidades

- **Varredura de Rede:** Utiliza `Nmap` para identificar portas abertas e versões de serviços (banners).
- **Análise Inteligente:** Integração com a API do **Google Gemini (LLM)** para interpretar os resultados técnicos.
- **Relatório Executivo:** Gera automaticamente uma explicação dos riscos e sugestões de correção para cada porta encontrada.
- **Modo Stealth/Rápido:** Configurado para evitar bloqueios simples de ICMP (-Pn).

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.12
- **Motor de Scan:** Nmap & python-nmap
- **IA:** Google Generative AI (Gemini 2.5 Flash)
- **Empacotamento:** PyInstaller (para versão .exe)

## ⚠️ Disclaimer (Aviso Legal)

Esta ferramenta foi desenvolvida para **fins defesa cibernética**. 
O uso contra alvos sem autorização prévia por escrito é ilegal e antiético.

---
*Projeto desenvolvido por Jean Bastos - Especialista em Segurança da Informação.*
