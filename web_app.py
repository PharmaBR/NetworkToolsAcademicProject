"""
NetworkTools - Versão Web
Trabalho 01 - Redes de Computadores

Autor: [Seu Nome]
Data: setembro/2025

Interface web usando Streamlit para análise de redes IP.
Para executar: streamlit run web_app.py
"""

import streamlit as st
from core.network_utils import (
    validar_ip, 
    validar_cidr, 
    cidr_para_mascara_decimal, 
    ips_mesma_rede
)

# IP FIXO DE ORIGEM (Constante conforme requisito)
IP_ORIGEM = "192.168.1.10"


def main():
    """Interface web principal."""
    
    # Configuração da página
    st.set_page_config(
        page_title="NetworkTools - Analisador de Redes",
        page_icon="🌐",
        layout="centered"
    )
    
    # Cabeçalho
    st.title("🌐 NetworkTools - Analisador de Redes IP")
    st.markdown("---")
    
    # IP de origem fixo
    st.info(f"**IP de Origem (FIXO):** `{IP_ORIGEM}`")
    
    # Formulário de entrada
    st.subheader("📋 Entrada de Dados")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Máscara CIDR
        cidr = st.number_input(
            "Máscara de rede (bits)",
            min_value=0,
            max_value=32,
            value=24,
            help="Digite a quantidade de bits da máscara (0-32)"
        )
    
    with col2:
        # IP de destino
        ip_destino = st.text_input(
            "IP de destino",
            value="192.168.1.100",
            help="Digite o IP de destino no formato xxx.xxx.xxx.xxx"
        )
    
    # Botão de análise
    if st.button("🔍 Analisar Rede", type="primary"):
        # Validações
        erros = []
        
        if not validar_cidr(cidr):
            erros.append("CIDR deve estar entre 0 e 32")
        
        if not validar_ip(ip_destino):
            erros.append("IP de destino inválido")
        
        if erros:
            # Exibe erros
            for erro in erros:
                st.error(f"❌ {erro}")
        else:
            # Processa análise
            try:
                mascara_decimal = cidr_para_mascara_decimal(cidr)
                mesma_rede = ips_mesma_rede(IP_ORIGEM, ip_destino, cidr)
                
                # Exibe resultados
                st.markdown("---")
                st.subheader("📊 Resultados")
                
                # A) Máscara decimal
                st.markdown("### A) Máscara de Rede")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("Bits", f"/{cidr}")
                
                with col2:
                    st.metric("Formato Decimal", mascara_decimal)
                
                # B) Análise de rede
                st.markdown("### B) Análise de Rede")
                
                # Tabela de comparação
                dados_comparacao = {
                    "Parâmetro": ["IP Origem", "IP Destino", "Máscara"],
                    "Valor": [IP_ORIGEM, ip_destino, f"/{cidr} ({mascara_decimal})"]
                }
                
                st.table(dados_comparacao)
                
                # Resultado final
                if mesma_rede:
                    st.success("✅ **RESULTADO:** Os IPs ESTÃO na mesma rede!")
                else:
                    st.error("❌ **RESULTADO:** Os IPs NÃO estão na mesma rede!")
                
                # Informações adicionais
                with st.expander("ℹ️ Informações Técnicas"):
                    st.write(f"**IP Origem (binário):** {format(int(''.join(IP_ORIGEM.split('.'))), 'b').zfill(32)}")
                    st.write(f"**IP Destino (binário):** {format(int(''.join(ip_destino.split('.'))), 'b').zfill(32)}")
                    st.write(f"**Máscara (binário):** {'1' * cidr + '0' * (32 - cidr)}")
                
            except Exception as e:
                st.error(f"❌ Erro no processamento: {e}")
    
    # Sidebar com informações
    with st.sidebar:
        st.markdown("### 📚 Sobre o NetworkTools")
        st.markdown("""
        Este programa foi desenvolvido para análise de redes IP, 
        atendendo aos seguintes requisitos:
        
        **Funcionalidades:**
        - ✅ IP fixo de origem
        - ✅ Conversão CIDR → Decimal
        - ✅ Verificação de mesma rede
        - ✅ Interface intuitiva
        - ✅ Validação de entradas
        - ✅ Testes unitários
        - ✅ Código documentado
        """)
        
        st.markdown("### 🧪 Exemplos de Teste")
        st.markdown("""
        **Mesma rede (24 bits):**
        - IP1: 192.168.1.10
        - IP2: 192.168.1.100
        
        **Redes diferentes (24 bits):**
        - IP1: 192.168.1.10  
        - IP2: 192.168.2.10
        """)
        
        st.markdown("### 👥 Equipe")
        st.markdown("""
        - [Nome 1] - 1º Semestre
        - [Nome 2] - [Semestre]
        - [Nome 3] - [Semestre]
        - [Nome 4] - [Semestre]
        """)


if __name__ == "__main__":
    main()