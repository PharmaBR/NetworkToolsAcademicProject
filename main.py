"""
NetworkTools - Analisador de Redes IP
Trabalho 01 - Redes de Computadores

Autor: [Seu Nome]
Data: setembro/2025

Este programa analisa redes IP, convertendo máscaras CIDR para formato decimal
e verificando se dois IPs estão na mesma rede.

Funcionalidades:
1) IP fixo de origem (configurável via constante)
2) Recebe máscara de rede em bits CIDR
3) Recebe IP de destino do usuário
4) Mostra máscara em formato decimal
5) Informa se IPs estão na mesma rede
"""

from core.network_utils import (
    validar_ip, 
    validar_cidr, 
    cidr_para_mascara_decimal, 
    ips_mesma_rede
)

# IP FIXO DE ORIGEM (Constante conforme requisito)
IP_ORIGEM = "192.168.1.10"


def exibir_cabecalho():
    """Exibe o cabeçalho do programa."""
    print("=" * 60)
    print("    NETWORKTOOLS - ANALISADOR DE REDES IP")
    print("=" * 60)
    print(f"IP de Origem (FIXO): {IP_ORIGEM}")
    print("=" * 60)


def obter_mascara_cidr():
    """
    Obtém a máscara CIDR do usuário com validação.
    
    Returns:
        int: Máscara CIDR válida
    """
    while True:
        try:
            entrada = input("\nDigite a máscara de rede em bits (ex: 24): ")
            cidr = int(entrada)
            
            if validar_cidr(cidr):
                return cidr
            else:
                print("❌ ERRO: A máscara deve estar entre 0 e 32 bits!")
                
        except ValueError:
            print("❌ ERRO: Digite apenas números!")


def obter_ip_destino():
    """
    Obtém o IP de destino do usuário com validação.
    
    Returns:
        str: IP de destino válido
    """
    while True:
        ip_destino = input("Digite o IP de destino (ex: 192.168.1.100): ").strip()
        
        if validar_ip(ip_destino):
            return ip_destino
        else:
            print("❌ ERRO: IP inválido! Use o formato xxx.xxx.xxx.xxx (0-255)")


def exibir_resultados(cidr, mascara_decimal, ip_destino, mesma_rede):
    """
    Exibe os resultados da análise.
    
    Args:
        cidr (int): Máscara CIDR
        mascara_decimal (str): Máscara em formato decimal
        ip_destino (str): IP de destino
        mesma_rede (bool): Se estão na mesma rede
    """
    print("\n" + "=" * 60)
    print("                  RESULTADOS")
    print("=" * 60)
    
    # A) Máscara em formato decimal
    print(f"\nA) MÁSCARA DE REDE:")
    print(f"   {cidr} bits")
    print(f"   {mascara_decimal}")
    
    # B) Verificação de mesma rede
    print(f"\nB) ANÁLISE DE REDE:")
    print(f"   IP Origem:  {IP_ORIGEM}")
    print(f"   IP Destino: {ip_destino}")
    print(f"   Máscara:    /{cidr}")
    
    if mesma_rede:
        print("   ✅ RESULTADO: Os IPs ESTÃO na mesma rede!")
    else:
        print("   ❌ RESULTADO: Os IPs NÃO estão na mesma rede!")
    
    print("=" * 60)


def main():
    """Função principal do programa."""
    try:
        # Exibe cabeçalho
        exibir_cabecalho()
        
        # Obtém dados do usuário
        print("\n📋 ENTRADA DE DADOS:")
        cidr = obter_mascara_cidr()
        ip_destino = obter_ip_destino()
        
        # Processa os dados
        print("\n⚙️  PROCESSANDO...")
        mascara_decimal = cidr_para_mascara_decimal(cidr)
        mesma_rede = ips_mesma_rede(IP_ORIGEM, ip_destino, cidr)
        
        # Exibe resultados
        exibir_resultados(cidr, mascara_decimal, ip_destino, mesma_rede)
        
        # Pergunta se quer continuar
        print("\nDeseja fazer outra análise? (s/n): ", end="")
        resposta = input().lower().strip()
        
        if resposta in ['s', 'sim', 'y', 'yes']:
            print("\n" + "─" * 60)
            main()  # Recursão para nova análise
        else:
            print("\n👋 Obrigado por usar o NetworkTools!")
            
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrompido pelo usuário. Até logo!")
    except Exception as e:
        print(f"\n❌ ERRO INESPERADO: {e}")
        print("Entre em contato com o suporte técnico.")


if __name__ == "__main__":
    main()
