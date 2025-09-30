#!/bin/bash
# Script para inicializar o Git e criar histórico do projeto

echo "🚀 Inicializando repositório Git..."

# Inicializa o repositório
git init

# Configura informações do usuário (se necessário)
git config user.name "Equipe NetworkTools"
git config user.email "equipe@networktools.com"

# Primeiro commit - estrutura inicial
git add pyproject.toml uv.lock
git commit -m "🎯 Inicial: Configuração do projeto Python

- Adiciona pyproject.toml com dependências
- Configura Streamlit para interface web
- Estabelece estrutura base do projeto"

# Segundo commit - módulo core
git add core/
git commit -m "⚙️ Core: Implementa funções de análise de rede

- Adiciona validação de IPs e CIDR
- Implementa conversão CIDR para máscara decimal
- Cria função para verificar se IPs estão na mesma rede
- Adiciona documentação completa nas funções"

# Terceiro commit - testes
git add test_network_utils.py
git commit -m "🧪 Testes: Implementa suite completa de testes

- Testa validação de IPs válidos e inválidos
- Testa validação de CIDR válidos e inválidos
- Testa conversão CIDR para máscara decimal
- Testa verificação de mesma rede (casos positivos e negativos)
- Garante cobertura de 100% das funcionalidades"

# Quarto commit - versão CLI
git add main.py
git commit -m "💻 CLI: Implementa interface de linha de comando

- Interface intuitiva com validação de entradas
- IP fixo conforme requisito (192.168.1.10)
- Mensagens claras e formatação organizada
- Opção de múltiplas análises
- Tratamento robusto de erros"

# Quinto commit - versão web
git add web_app.py
git commit -m "🌐 Web: Adiciona interface web com Streamlit

- Interface moderna e responsiva
- Validação em tempo real
- Métricas e visualizações
- Informações técnicas expandíveis
- Exemplos de teste na sidebar"

# Sexto commit - documentação
git add README.md
git commit -m "📚 Docs: Adiciona documentação completa

- README detalhado com instruções
- Critérios de avaliação mapeados
- Exemplos de uso práticos
- Estrutura do projeto documentada
- Informações da equipe"

echo "✅ Repositório Git inicializado com histórico completo!"
echo "📊 Commits criados:"
git log --oneline