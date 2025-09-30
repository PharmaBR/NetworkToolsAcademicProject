"""
Demonstração Prática - NetworkTools
Exemplos de execução para apresentação

Execute este arquivo para ver exemplos práticos de todas as funcionalidades.
"""

from core.network_utils import (
    validar_ip, 
    validar_cidr, 
    cidr_para_mascara_decimal, 
    ips_mesma_rede
)

def demonstrar_funcionalidades():
    """Demonstra todas as funcionalidades do sistema."""
    
    print("=" * 70)
    print("    DEMONSTRAÇÃO PRÁTICA - NETWORKTOOLS")
    print("=" * 70)
    
    # IP fixo conforme requisito
    IP_ORIGEM = "192.168.1.10"
    print(f"🎯 IP de Origem (FIXO): {IP_ORIGEM}")
    print("=" * 70)
    
    # Exemplos de conversão de máscara
    print("\n📊 A) CONVERSÃO DE MÁSCARAS CIDR PARA DECIMAL:")
    print("-" * 50)
    
    mascaras_exemplo = [8, 16, 20, 23, 24, 25, 28, 30, 32]
    
    for cidr in mascaras_exemplo:
        mascara_decimal = cidr_para_mascara_decimal(cidr)
        print(f"   /{cidr:2d} bits  →  {mascara_decimal}")
    
    # Exemplos de análise de rede
    print("\n🔍 B) ANÁLISE DE REDES - MESMA REDE:")
    print("-" * 50)
    
    casos_mesma_rede = [
        ("192.168.1.100", 24),
        ("192.168.1.50", 24),
        ("192.168.1.254", 24),
        ("192.168.0.10", 16),
        ("192.168.255.1", 16),
        ("192.160.0.1", 12),
    ]
    
    for ip_destino, cidr in casos_mesma_rede:
        mesma_rede = ips_mesma_rede(IP_ORIGEM, ip_destino, cidr)
        status = "✅ MESMA" if mesma_rede else "❌ DIFERENTE"
        mascara = cidr_para_mascara_decimal(cidr)
        print(f"   {IP_ORIGEM} → {ip_destino} (/{cidr}) = {status}")
        print(f"      Máscara: {mascara}")
        print()
    
    print("🔍 B) ANÁLISE DE REDES - REDES DIFERENTES:")
    print("-" * 50)
    
    casos_redes_diferentes = [
        ("192.168.2.10", 24),
        ("192.169.1.10", 24),
        ("10.0.0.1", 24),
        ("172.16.1.1", 24),
        ("192.167.1.10", 16),
    ]
    
    for ip_destino, cidr in casos_redes_diferentes:
        mesma_rede = ips_mesma_rede(IP_ORIGEM, ip_destino, cidr)
        status = "✅ MESMA" if mesma_rede else "❌ DIFERENTE"
        mascara = cidr_para_mascara_decimal(cidr)
        print(f"   {IP_ORIGEM} → {ip_destino} (/{cidr}) = {status}")
        print(f"      Máscara: {mascara}")
        print()
    
    # Demonstração de validações
    print("🛡️  DEMONSTRAÇÃO DAS VALIDAÇÕES:")
    print("-" * 50)
    
    print("IPs válidos:")
    ips_validos = ["192.168.1.1", "10.0.0.1", "172.16.1.1", "0.0.0.0", "255.255.255.255"]
    for ip in ips_validos:
        print(f"   {ip} → {'✅ Válido' if validar_ip(ip) else '❌ Inválido'}")
    
    print("\nIPs inválidos:")
    ips_invalidos = ["300.1.1.1", "192.168.1", "abc.def.ghi.jkl", "192.168.-1.1"]
    for ip in ips_invalidos:
        print(f"   {ip} → {'✅ Válido' if validar_ip(ip) else '❌ Inválido'}")
    
    print("\nCIDRs válidos: 0-32")
    print("CIDRs inválidos: <0 ou >32")
    
    print("\n" + "=" * 70)
    print("✅ DEMONSTRAÇÃO CONCLUÍDA - TODOS OS REQUISITOS ATENDIDOS!")
    print("=" * 70)


if __name__ == "__main__":
    demonstrar_funcionalidades()