# Corpus Biomédico em Português — SciELO
Coleta e organização de revisões sistemáticas biomédicas em português para construção de um dataset voltado a modelos de linguagem (Word2Vec).
## Descrição
Este projeto coleta 32 artigos de revisão sistemática do domínio biomédico a partir do SciELO Brasil e SciELO Portugal, baixa seus metadados em formato XML e analisa as referências bibliográficas em português para formar a base do dataset.

## Scripts

### `baixar_xmls.py`
Lê os DOIs do Excel e tenta baixar o XML de cada artigo via API do SciELO Articlemeta. Primeira versão, sem retry em caso de falha.

### `baixar2_xmls.py`
Versão melhorada. Adiciona 3 tentativas por artigo e pula arquivos já baixados, evitando downloads duplicados.

### `analisar_referencias.py`
Analisa os XMLs e conta quantas referências de cada artigo são em português, inglês ou outros idiomas. Suporta o formato do SciELO Brasil e do SciELO Portugal. Gera `analise_referencias.xlsx`.

### `extrair_referencias_pt.py`
Extrai todas as referências em português dos 32 XMLs, recupera o título de cada uma e organiza em ordem alfabética. Gera `referencias_pt.xlsx` — início do dataset.

## Dependências

```
pip install requests openpyxl langdetect
```

## Fonte dos dados

- [SciELO Brasil](https://search.scielo.org/)
- [SciELO Portugal](https://scielo.pt/)
- API utilizada: [SciELO Articlemeta](https://articlemeta.scielo.org/)
