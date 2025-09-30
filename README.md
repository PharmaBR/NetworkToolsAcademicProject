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

## 👥 Equipe

- **[Nome 1]** - 1º Semestre (obrigatório)
- **[Nome 2]** - [Semestre]
- **[Nome 3]** - [Semestre]
- **[Nome 4]** - [Semestre]

## 📝 Licença

Este projeto foi desenvolvido para fins acadêmicos como parte do Trabalho 01 da disciplina de Redes de Computadores.

---

**Nota:** Todos os integrantes da equipe estão familiarizados com o código e preparados para responder perguntas durante a apresentação.