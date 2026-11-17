# Cadastro de turma em Python

[![Abrir no Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/IamPriime/cadastro-turma-python/blob/main/cadastro_turma.ipynb)

Cadastro em memória de alunos e professores usando listas, dicionários e funções.

Projeto de estudo de **Gabriel / [IamPriime](https://github.com/IamPriime)**, desenvolvido a partir de um notebook do Google Colab e organizado para portfólio. O foco é mostrar a lógica implementada e permitir que outra pessoa execute o projeto.

## O que o projeto faz

- Lista alunos e professores.
- Adiciona nomes por categoria.
- Remove registros por posição com validação.
- Oferece menu interativo para usar as funções.

## Tecnologias e conceitos

Python 3.10+ · funções · controle de fluxo · validação de entradas.

## Como executar

```bash
git clone https://github.com/IamPriime/cadastro-turma-python.git
cd cadastro-turma-python
python -m venv .venv
```

Ative o ambiente: no Windows PowerShell, `.venv\Scripts\Activate.ps1`; no macOS/Linux, `source .venv/bin/activate`.

```bash
python -m pip install -r requirements.txt
python cadastro_turma.py
```

No Colab, use o botão no início deste README. Execute a célula e responda às entradas interativas.

## Exemplo e interpretação

Exemplo: escolha `2`, digite um nome de exemplo e use `1` para listar. Para remover, escolha `4` e informe a posição exibida. A turma começa vazia e os dados existem apenas durante a execução.

## Estrutura

| Arquivo | Função |
| --- | --- |
| `cadastro_turma.ipynb` | Notebook para Colab/Jupyter, sem saídas antigas |
| `cadastro_turma.py` | Versão executável localmente |
| `requirements.txt` | Indicação de que não há dependências externas |


## Origem e melhorias

Origem no Colab: `Untitled`. O arquivo no Drive foi preservado. As funções de cadastro foram reunidas em um menu, com validação de posições e nomes vazios. As saídas de execução e os metadados pessoais do notebook foram removidos da versão publicada.

## Limitações

Projeto educacional executado no terminal. Não inclui banco de dados, interface web ou persistência.

## Próximos passos

- Adicionar persistência e ampliar a cobertura de cenários de entrada.
- Separar a interface de terminal da lógica para facilitar futuras interfaces.

## Autoria e uso

Organização de estudos de [IamPriime](https://github.com/IamPriime). Nenhuma licença de software foi escolhida para este repositório.
