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
        layout="wide"
    )
    
    # Cabeçalho
    st.title("🌐 NetworkTools - Analisador de Redes IP")
    
    # Criação das abas
    tab1, tab2, tab3 = st.tabs(["🔧 Analisador", "📚 Tutorial Acadêmico", "🧪 Exemplos Práticos"])
    
    with tab1:
        analisador_principal()
    
    with tab2:
        tutorial_academico()
    
    with tab3:
        exemplos_praticos()


def analisador_principal():
    """Aba principal com o analisador de redes."""
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
        
        st.markdown("### 👥 Equipe")
        st.markdown("""
        - [Nome 1] - 1º Semestre
        - [Nome 2] - [Semestre]
        - [Nome 3] - [Semestre]
        - [Nome 4] - [Semestre]
        """)


def tutorial_academico():
    """Aba com explicação acadêmica detalhada."""
    
    st.header("📚 Tutorial Acadêmico - Fundamentos de Redes")
    
    # Seção 1: Conceitos Fundamentais
    st.subheader("1️⃣ Conceitos Fundamentais")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🌐 Endereço IP
        
        Um **endereço IP** (Internet Protocol) é um identificador numérico único 
        atribuído a cada dispositivo em uma rede. No IPv4, é composto por **32 bits** 
        organizados em **4 octetos** (grupos de 8 bits cada).
        
        **Exemplo:** `192.168.1.10`
        - **192** = primeiro octeto
        - **168** = segundo octeto  
        - **1** = terceiro octeto
        - **10** = quarto octeto
        """)
    
    with col2:
        st.markdown("""
        ### 🎭 Máscara de Rede
        
        A **máscara de rede** (subnet mask) determina qual parte do IP 
        identifica a **rede** e qual parte identifica o **host** (dispositivo).
        
        **Notação CIDR:** `/24` significa 24 bits para rede, 8 para hosts
        
        **Formato binário:**
        - `1` = bit de rede
        - `0` = bit de host
        """)
    
    # Seção 2: Representação Binária
    st.subheader("2️⃣ Representação Binária")
    
    st.markdown("""
    ### 🔢 Como o Computador "Vê" os IPs
    
    Os computadores trabalham apenas com **números binários** (0 e 1). 
    Vamos ver como nosso IP de exemplo é representado:
    """)
    
    # Exemplo interativo
    exemplo_ip = "192.168.1.10"
    octetos = exemplo_ip.split('.')
    
    col1, col2, col3, col4 = st.columns(4)
    
    for i, (col, octeto) in enumerate(zip([col1, col2, col3, col4], octetos)):
        with col:
            binario = format(int(octeto), '08b')
            st.metric(f"Octeto {i+1}", octeto)
            st.code(f"{binario}", language="text")
    
    st.code(f"IP Completo (binário): {'.'.join([format(int(oct), '08b') for oct in octetos])}")
    st.code(f"IP Completo (32 bits): {''.join([format(int(oct), '08b') for oct in octetos])}")
    
    # Seção 3: Funcionamento das Máscaras
    st.subheader("3️⃣ Como Funcionam as Máscaras")
    
    st.markdown("""
    ### 🎯 Processo de Análise de Rede
    
    Para determinar se dois IPs estão na **mesma rede**, seguimos estes passos:
    """)
    
    # Demonstração passo a passo
    with st.expander("🔍 Demonstração Passo a Passo"):
        
        ip1 = "192.168.1.10"
        ip2 = "192.168.1.100" 
        cidr = 24
        
        st.markdown(f"**Exemplo:** Verificando se `{ip1}` e `{ip2}` estão na mesma rede `/{cidr}`")
        
        # Passo 1
        st.markdown("#### Passo 1: Converter IPs para binário")
        ip1_bin = ''.join([format(int(oct), '08b') for oct in ip1.split('.')])
        ip2_bin = ''.join([format(int(oct), '08b') for oct in ip2.split('.')])
        
        col1, col2 = st.columns(2)
        with col1:
            st.code(f"IP1: {ip1}\n{ip1_bin}")
        with col2:
            st.code(f"IP2: {ip2}\n{ip2_bin}")
        
        # Passo 2
        st.markdown("#### Passo 2: Criar máscara binária")
        mascara_bin = '1' * cidr + '0' * (32 - cidr)
        st.code(f"Máscara /{cidr}:\n{mascara_bin}")
        
        # Passo 3
        st.markdown("#### Passo 3: Aplicar operação AND")
        st.markdown("A operação **AND** mantém apenas os bits de rede:")
        
        rede1_bin = ''.join(['1' if ip1_bin[i] == '1' and mascara_bin[i] == '1' else '0' 
                            for i in range(32)])
        rede2_bin = ''.join(['1' if ip2_bin[i] == '1' and mascara_bin[i] == '1' else '0' 
                            for i in range(32)])
        
        col1, col2 = st.columns(2)
        with col1:
            st.code(f"IP1 AND Máscara:\n{rede1_bin}")
        with col2:
            st.code(f"IP2 AND Máscara:\n{rede2_bin}")
        
        # Passo 4
        st.markdown("#### Passo 4: Comparar endereços de rede")
        if rede1_bin == rede2_bin:
            st.success("✅ **Resultado:** Endereços de rede IGUAIS → Mesma rede!")
        else:
            st.error("❌ **Resultado:** Endereços de rede DIFERENTES → Redes diferentes!")
    
    # Seção 4: Implementação no Código
    st.subheader("4️⃣ Implementação no Código")
    
    st.markdown("""
    ### 💻 Como o Programa Funciona
    
    Nosso programa implementa exatamente o processo acadêmico descrito acima:
    """)
    
    # Mostrar código com explicações
    with st.expander("📝 Código da Função Principal"):
        st.code('''
def ips_mesma_rede(ip_origem, ip_destino, cidr):
    """
    Verifica se dois IPs estão na mesma rede.
    
    Processo:
    1. Valida os IPs de entrada
    2. Converte IPs para inteiros (32 bits)
    3. Cria máscara binária
    4. Aplica operação AND
    5. Compara os endereços de rede
    """
    
    # 1. Validação
    if not validar_ip(ip_origem):
        raise ValueError(f"IP de origem inválido: {ip_origem}")
    
    # 2. Conversão para inteiro
    ip_origem_int = ip_para_inteiro(ip_origem)
    ip_destino_int = ip_para_inteiro(ip_destino)
    
    # 3. Criação da máscara
    mascara_int = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF
    
    # 4. Operação AND
    rede_origem = ip_origem_int & mascara_int
    rede_destino = ip_destino_int & mascara_int
    
    # 5. Comparação
    return rede_origem == rede_destino
        ''', language='python')
    
    # Seção 5: Aplicações Práticas
    st.subheader("5️⃣ Aplicações Práticas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🏢 No Mundo Real
        
        **Roteamento de Rede:**
        - Roteadores usam máscaras para decidir rotas
        - Determina se pacote é local ou remoto
        
        **Segurança:**
        - Firewalls aplicam regras por rede
        - Controle de acesso baseado em subnet
        
        **Administração:**
        - Organização lógica de dispositivos
        - Facilita troubleshooting
        """)
    
    with col2:
        st.markdown("""
        ### 🎓 Conceitos Importantes
        
        **Classes de Rede:**
        - `/8` = 16.777.214 hosts (Classe A)
        - `/16` = 65.534 hosts (Classe B)  
        - `/24` = 254 hosts (Classe C)
        
        **VLSM (Variable Length Subnet Mask):**
        - Permite subnets de tamanhos diferentes
        - Otimiza uso de endereços IP
        """)


def exemplos_praticos():
    """Aba com exemplos práticos interativos."""
    
    st.header("🧪 Exemplos Práticos Interativos")
    
    st.markdown("""
    Experimente diferentes combinações de IPs e máscaras para entender 
    como a análise de rede funciona na prática.
    """)
    
    # Calculadora interativa
    st.subheader("🧮 Calculadora de Rede Interativa")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        ip_teste = st.text_input("IP para Testar", value="192.168.1.50")
    
    with col2:
        cidr_teste = st.slider("Máscara CIDR", 0, 32, 24)
    
    with col3:
        st.metric("IP Origem (Fixo)", IP_ORIGEM)
    
    if validar_ip(ip_teste):
        
        # Cálculos
        mascara_decimal = cidr_para_mascara_decimal(cidr_teste)
        mesma_rede = ips_mesma_rede(IP_ORIGEM, ip_teste, cidr_teste)
        
        # Visualização detalhada
        st.markdown("### 📊 Análise Detalhada")
        
        # Tabela de resultados
        dados = {
            "Parâmetro": ["IP Origem", "IP Teste", "Máscara CIDR", "Máscara Decimal", "Mesma Rede?"],
            "Valor": [IP_ORIGEM, ip_teste, f"/{cidr_teste}", mascara_decimal, 
                     "✅ Sim" if mesma_rede else "❌ Não"]
        }
        
        st.table(dados)
        
        # Visualização binária
        with st.expander("🔍 Visualização Binária"):
            
            # IPs em binário
            ip_origem_bin = '.'.join([format(int(oct), '08b') for oct in IP_ORIGEM.split('.')])
            ip_teste_bin = '.'.join([format(int(oct), '08b') for oct in ip_teste.split('.')])
            mascara_bin = '.'.join([format(int(oct), '08b') for oct in mascara_decimal.split('.')])
            
            st.code(f"""
IP Origem:  {IP_ORIGEM}
Binário:    {ip_origem_bin}

IP Teste:   {ip_teste}
Binário:    {ip_teste_bin}

Máscara:    {mascara_decimal}
Binário:    {mascara_bin}
            """)
    
    else:
        st.error("❌ IP inválido! Use o formato xxx.xxx.xxx.xxx")
    
    # Casos de estudo
    st.subheader("📚 Casos de Estudo")
    
    casos_estudo = [
        {
            "titulo": "🏠 Rede Doméstica Típica",
            "descricao": "Configuração comum em residências",
            "ip_origem": "192.168.1.1",
            "exemplos": [
                ("192.168.1.10", 24, True),
                ("192.168.1.255", 24, True),
                ("192.168.2.1", 24, False)
            ]
        },
        {
            "titulo": "🏢 Rede Empresarial",
            "descricao": "Subnet maior para mais dispositivos",
            "ip_origem": "10.0.1.1",
            "exemplos": [
                ("10.0.1.100", 16, True),
                ("10.0.50.200", 16, True),
                ("10.1.1.1", 16, False)
            ]
        },
        {
            "titulo": "🔬 Laboratório Acadêmico",
            "descricao": "Rede pequena e controlada",
            "ip_origem": "172.16.10.1",
            "exemplos": [
                ("172.16.10.50", 28, True),
                ("172.16.10.15", 28, True),
                ("172.16.10.20", 28, False)
            ]
        }
    ]
    
    for caso in casos_estudo:
        with st.expander(f"{caso['titulo']} - {caso['descricao']}"):
            
            st.markdown(f"**IP Base:** `{caso['ip_origem']}`")
            
            for ip_destino, cidr, esperado in caso['exemplos']:
                resultado = ips_mesma_rede(caso['ip_origem'], ip_destino, cidr)
                status = "✅" if resultado == esperado else "❌"
                rede_status = "Mesma rede" if resultado else "Rede diferente"
                
                st.markdown(f"- `{ip_destino}` com `/{cidr}` → {status} {rede_status}")


if __name__ == "__main__":
    main()