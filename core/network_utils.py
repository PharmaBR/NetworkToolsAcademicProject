"""
Módulo para análise de redes IP
Autor: [Seu Nome]
Data: setembro/2025

Este módulo contém funções para:
- Converter máscara CIDR para formato decimal
- Verificar se dois IPs estão na mesma rede
- Validar endereços IP
"""

import re


def validar_ip(ip: str) -> bool:
    """
    Valida se um endereço IP está em formato válido (IPv4).
    
    Args:
        ip (str): Endereço IP a ser validado
        
    Returns:
        bool: True se o IP for válido, False caso contrário
        
    Exemplo:
        >>> validar_ip("192.168.1.1")
        True
        >>> validar_ip("300.1.1.1")
        False
    """
    # Padrão regex para IPv4
    padrao = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    match = re.match(padrao, ip)
    
    if not match:
        return False
    
    # Verifica se cada octeto está entre 0 e 255
    for octeto in match.groups():
        if int(octeto) > 255:
            return False
            
    return True


def validar_cidr(cidr: int) -> bool:
    """
    Valida se o valor CIDR está no range válido (0-32).
    
    Args:
        cidr (int): Valor CIDR a ser validado
        
    Returns:
        bool: True se o CIDR for válido, False caso contrário
        
    Exemplo:
        >>> validar_cidr(24)
        True
        >>> validar_cidr(33)
        False
    """
    return 0 <= cidr <= 32


def cidr_para_mascara_decimal(cidr: int) -> str:
    """
    Converte uma máscara CIDR para formato decimal.
    
    Args:
        cidr (int): Número de bits da máscara (0-32)
        
    Returns:
        str: Máscara em formato decimal (ex: "255.255.255.0")
        
    Raises:
        ValueError: Se o CIDR não estiver no range válido
        
    Exemplo:
        >>> cidr_para_mascara_decimal(24)
        '255.255.255.0'
        >>> cidr_para_mascara_decimal(23)
        '255.255.254.0'
    """
    if not validar_cidr(cidr):
        raise ValueError("CIDR deve estar entre 0 e 32")
    
    # Cria a máscara binária
    mascara_binaria = '1' * cidr + '0' * (32 - cidr)
    
    # Converte para decimal em octetos
    octetos = []
    for i in range(0, 32, 8):
        octeto_binario = mascara_binaria[i:i+8]
        octeto_decimal = int(octeto_binario, 2)
        octetos.append(str(octeto_decimal))
    
    return '.'.join(octetos)


def ip_para_inteiro(ip: str) -> int:
    """
    Converte um IP em formato string para inteiro.
    
    Args:
        ip (str): Endereço IP em formato string
        
    Returns:
        int: Representação inteira do IP
        
    Exemplo:
        >>> ip_para_inteiro("192.168.1.1")
        3232235777
    """
    octetos = ip.split('.')
    return (int(octetos[0]) << 24) + (int(octetos[1]) << 16) + (int(octetos[2]) << 8) + int(octetos[3])


def calcular_rede(ip: str, cidr: int) -> int:
    """
    Calcula o endereço de rede dado um IP e CIDR.
    
    Args:
        ip (str): Endereço IP
        cidr (int): Máscara CIDR
        
    Returns:
        int: Endereço de rede em formato inteiro
    """
    ip_int = ip_para_inteiro(ip)
    mascara_int = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF
    return ip_int & mascara_int


def ips_mesma_rede(ip_origem: str, ip_destino: str, cidr: int) -> bool:
    """
    Verifica se dois IPs estão na mesma rede.
    
    Args:
        ip_origem (str): IP de origem
        ip_destino (str): IP de destino
        cidr (int): Máscara CIDR
        
    Returns:
        bool: True se estiverem na mesma rede, False caso contrário
        
    Exemplo:
        >>> ips_mesma_rede("192.168.1.1", "192.168.1.100", 24)
        True
        >>> ips_mesma_rede("192.168.1.1", "192.168.2.1", 24)
        False
    """
    if not validar_ip(ip_origem):
        raise ValueError(f"IP de origem inválido: {ip_origem}")
    
    if not validar_ip(ip_destino):
        raise ValueError(f"IP de destino inválido: {ip_destino}")
    
    if not validar_cidr(cidr):
        raise ValueError(f"CIDR inválido: {cidr}")
    
    rede_origem = calcular_rede(ip_origem, cidr)
    rede_destino = calcular_rede(ip_destino, cidr)
    
    return rede_origem == rede_destino