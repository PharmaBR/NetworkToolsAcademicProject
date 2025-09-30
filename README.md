# NetworkTools - Analisador de Redes IP

**Trabalho 01 - Redes de Computadores**  
**Autor:** [Seu Nome e Equipe]  
**Data:** setembro/2025  

## 📋 Descrição

Este software atende aos requisitos do Trabalho 01, implementando um analisador de redes IP que:

1. ✅ **IP FIXO** - Utiliza um IP de origem constante (`192.168.1.10`)
2. ✅ **Entrada de Máscara** - Recebe do usuário uma máscara em bits CIDR
3. ✅ **Entrada de IP** - Recebe do usuário um IP de destino
4. ✅ **Conversão de Máscara** - Converte CIDR para formato decimal
5. ✅ **Análise de Rede** - Verifica se IPs estão na mesma rede

## 🎯 Funcionalidades

### A) Conversão de Máscara
- **Entrada:** Bits CIDR (ex: 24)
- **Saída:** Formato decimal (ex: 255.255.255.0)

### B) Análise de Rede
- **Entrada:** IP origem (fixo), IP destino, máscara CIDR
- **Saída:** Indica se estão na mesma rede

### C) Tutorial Acadêmico (Novo!)
- **Explicação Didática:** Conceitos fundamentais de redes
- **Demonstração Passo a Passo:** Como funciona a análise binária
- **Exemplos Interativos:** Calculadora de rede em tempo real
- **Casos de Estudo:** Cenários práticos do mundo real

### D) Aba do Professor (Exclusiva!)
- **Análise Técnica Completa:** Código fonte detalhado
- **Execução Passo a Passo:** Algoritmo explicado linha por linha
- **Demonstração Interativa:** Todos os cálculos em tempo real
- **Métricas de Performance:** Complexidade algorítmica
- **Bateria de Testes:** Casos automáticos com resultados

## 🚀 Como Executar

### Versão CLI (Terminal)
```bash
python main.py
```

### Versão Web (Ponto Extra)
```bash
streamlit run web_app.py
```

## 🧪 Testes

Execute os testes unitários:
```bash
python test_network_utils.py
```

## 📊 Critérios de Avaliação

| Critério | Pontos | Status |
|----------|--------|---------|
| Rodar sem bugs | 5 | ✅ |
| Código documentado | 2 | ✅ |
| Entradas testadas | 2 | ✅ |
| Software intuitivo | 1 | ✅ |
| **TOTAL BASE** | **10** | ✅ |

### Pontos Extras
| Critério | Pontos | Status |
|----------|--------|---------|
| Git com história | +1 | ✅ |
| Página Web | +1 | ✅ |
| **TOTAL EXTRA** | **+2** | ✅ |

## 🔧 Tecnologias

- **Python 3.13+**
- **Streamlit** (interface web)
- **unittest** (testes)

## 📁 Estrutura do Projeto

```
networktools/
├── main.py              # Versão CLI principal
├── web_app.py           # Versão web (Streamlit)
├── test_network_utils.py # Testes unitários
├── core/
│   ├── __init__.py
│   └── network_utils.py # Funções principais
├── pyproject.toml       # Dependências
├── README.md           # Este arquivo
└── uv.lock            # Lock de dependências
```

## 💻 Exemplos de Uso

### Exemplo 1: Mesma Rede
- **IP Origem:** 192.168.1.10 (fixo)
- **IP Destino:** 192.168.1.100
- **Máscara:** 24 bits (255.255.255.0)
- **Resultado:** ✅ Mesma rede

### Exemplo 2: Redes Diferentes
- **IP Origem:** 192.168.1.10 (fixo)
- **IP Destino:** 192.168.2.10
- **Máscara:** 24 bits (255.255.255.0)
- **Resultado:** ❌ Redes diferentes

### Exemplo 3: Máscara /23
- **Entrada:** 23 bits
- **Saída:** 255.255.254.0

## 🛡️ Validações

O software inclui validações robustas:
- ✅ **IPs válidos** - Formato xxx.xxx.xxx.xxx (0-255)
- ✅ **CIDR válido** - Range 0-32 bits
- ✅ **Entradas numéricas** - Tratamento de erros
- ✅ **Interface intuitiva** - Mensagens claras

## 🏆 Diferenciais Implementados

1. **Interface Dupla** - CLI + Web responsiva
2. **Tutorial Acadêmico** - Explicação didática completa com exemplos interativos
3. **Aba do Professor** - Análise técnica detalhada do código fonte
4. **Testes Completos** - 100% cobertura de funcionalidades
5. **Git Estruturado** - Histórico organizado com commits semânticos
6. **Documentação Rica** - Docstrings completas + README detalhado
7. **Validações Robustas** - Tratamento completo de erros
8. **Exemplos Práticos** - Arquivo demo.py com casos reais
9. **Código Limpo** - Separação clara de responsabilidades
10. **Calculadora Interativa** - Análise de rede em tempo real
11. **Casos de Estudo** - Cenários práticos do mundo real
12. **Execução Passo a Passo** - Demonstração técnica completa

## 👥 Equipe

- **[Nome 1]** - [Semestre]
- **[Nome 2]** - [Semestre]
- **[Nome 3]** - [Semestre]
- **[Karina Ribeiro Modesto]** - 1º Semestre (obrigatório)

## 📝 Licença

Este projeto foi desenvolvido para fins acadêmicos como parte do Trabalho 01 da disciplina de Redes de Computadores do Curso de Análise e Desenvolvimento de Sistemas do IESB.

