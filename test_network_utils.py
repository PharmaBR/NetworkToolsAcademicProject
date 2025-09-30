"""
Testes unitários para o módulo network_utils
Autor: [Seu Nome]
Data: setembro/2025

Este arquivo contém testes para validar todas as funcionalidades
do sistema de análise de redes.
"""

import unittest
from core.network_utils import (
    validar_ip, 
    validar_cidr, 
    cidr_para_mascara_decimal, 
    ips_mesma_rede,
    ip_para_inteiro,
    calcular_rede
)


class TestNetworkUtils(unittest.TestCase):
    """Classe de testes para as funções de rede."""
    
    def test_validar_ip_validos(self):
        """Testa validação de IPs válidos."""
        ips_validos = [
            "192.168.1.1",
            "10.0.0.1", 
            "172.16.0.1",
            "0.0.0.0",
            "255.255.255.255"
        ]
        
        for ip in ips_validos:
            with self.subTest(ip=ip):
                self.assertTrue(validar_ip(ip), f"IP {ip} deveria ser válido")
    
    def test_validar_ip_invalidos(self):
        """Testa validação de IPs inválidos."""
        ips_invalidos = [
            "300.1.1.1",
            "192.168.1",
            "192.168.1.1.1",
            "abc.def.ghi.jkl",
            "",
            "192.168.-1.1"
        ]
        
        for ip in ips_invalidos:
            with self.subTest(ip=ip):
                self.assertFalse(validar_ip(ip), f"IP {ip} deveria ser inválido")
    
    def test_validar_cidr_validos(self):
        """Testa validação de valores CIDR válidos."""
        for cidr in range(0, 33):
            with self.subTest(cidr=cidr):
                self.assertTrue(validar_cidr(cidr), f"CIDR {cidr} deveria ser válido")
    
    def test_validar_cidr_invalidos(self):
        """Testa validação de valores CIDR inválidos."""
        cidrs_invalidos = [-1, 33, 50, 100]
        
        for cidr in cidrs_invalidos:
            with self.subTest(cidr=cidr):
                self.assertFalse(validar_cidr(cidr), f"CIDR {cidr} deveria ser inválido")
    
    def test_cidr_para_mascara_decimal(self):
        """Testa conversão de CIDR para máscara decimal."""
        casos_teste = [
            (24, "255.255.255.0"),
            (23, "255.255.254.0"),
            (16, "255.255.0.0"),
            (8, "255.0.0.0"),
            (32, "255.255.255.255"),
            (0, "0.0.0.0"),
            (30, "255.255.255.252")
        ]
        
        for cidr, mascara_esperada in casos_teste:
            with self.subTest(cidr=cidr):
                resultado = cidr_para_mascara_decimal(cidr)
                self.assertEqual(resultado, mascara_esperada, 
                               f"CIDR /{cidr} deveria resultar em {mascara_esperada}")
    
    def test_cidr_para_mascara_decimal_invalido(self):
        """Testa conversão com CIDR inválido."""
        with self.assertRaises(ValueError):
            cidr_para_mascara_decimal(-1)
        
        with self.assertRaises(ValueError):
            cidr_para_mascara_decimal(33)
    
    def test_ip_para_inteiro(self):
        """Testa conversão de IP para inteiro."""
        casos_teste = [
            ("0.0.0.0", 0),
            ("0.0.0.1", 1),
            ("0.0.1.0", 256),
            ("192.168.1.1", 3232235777),
            ("255.255.255.255", 4294967295)
        ]
        
        for ip, inteiro_esperado in casos_teste:
            with self.subTest(ip=ip):
                resultado = ip_para_inteiro(ip)
                self.assertEqual(resultado, inteiro_esperado,
                               f"IP {ip} deveria resultar em {inteiro_esperado}")
    
    def test_ips_mesma_rede_positivos(self):
        """Testa casos onde IPs estão na mesma rede."""
        casos_teste = [
            ("192.168.1.1", "192.168.1.100", 24),
            ("10.0.0.1", "10.0.0.254", 24),
            ("172.16.1.1", "172.16.1.200", 24),
            ("192.168.0.1", "192.168.1.1", 16),
            ("10.1.1.1", "10.1.2.1", 16)
        ]
        
        for ip_origem, ip_destino, cidr in casos_teste:
            with self.subTest(origem=ip_origem, destino=ip_destino, cidr=cidr):
                resultado = ips_mesma_rede(ip_origem, ip_destino, cidr)
                self.assertTrue(resultado, 
                              f"{ip_origem} e {ip_destino} deveriam estar na mesma rede /{cidr}")
    
    def test_ips_mesma_rede_negativos(self):
        """Testa casos onde IPs NÃO estão na mesma rede."""
        casos_teste = [
            ("192.168.1.1", "192.168.2.1", 24),
            ("10.0.0.1", "10.1.0.1", 24),
            ("172.16.1.1", "172.17.1.1", 24),
            ("192.168.1.1", "10.0.0.1", 8)
        ]
        
        for ip_origem, ip_destino, cidr in casos_teste:
            with self.subTest(origem=ip_origem, destino=ip_destino, cidr=cidr):
                resultado = ips_mesma_rede(ip_origem, ip_destino, cidr)
                self.assertFalse(resultado, 
                               f"{ip_origem} e {ip_destino} NÃO deveriam estar na mesma rede /{cidr}")
    
    def test_ips_mesma_rede_entradas_invalidas(self):
        """Testa validação de entradas inválidas."""
        # IP de origem inválido
        with self.assertRaises(ValueError):
            ips_mesma_rede("300.1.1.1", "192.168.1.1", 24)
        
        # IP de destino inválido
        with self.assertRaises(ValueError):
            ips_mesma_rede("192.168.1.1", "300.1.1.1", 24)
        
        # CIDR inválido
        with self.assertRaises(ValueError):
            ips_mesma_rede("192.168.1.1", "192.168.1.2", 33)


if __name__ == '__main__':
    # Executa os testes
    unittest.main(verbosity=2)