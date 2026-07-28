# Corpus Biomédico em Português — SciELO

Coleta e organização de revisões sistemáticas biomédicas em português para construção de um corpus voltado a modelos de linguagem.

## Descrição

Este projeto coleta 32 artigos de revisão sistemática do domínio biomédico a partir do SciELO Brasil e SciELO Portugal, baixa seus metadados em formato XML, analisa as referências bibliográficas em português, recupera os documentos completos, converte os arquivos PDF para TXT e gera rankings de similaridade utilizando BM25.

## Scripts

### `baixar2_xmls.py`
Baixa os metadados dos artigos em formato XML. Adiciona 3 tentativas por artigo e ignora arquivos já existentes, evitando downloads duplicados.

### `analisar_referencias.py`
Analisa os XMLs e conta quantas referências de cada artigo são em português, inglês ou outros idiomas. Suporta o formato do SciELO Brasil e do SciELO Portugal. Gera `analise_referencias.xlsx`.

### `extrair_referencias_pt.py`
Extrai as referências em português dos XMLs, recupera seus títulos e organiza os resultados em ordem alfabética. Gera `referencias_pt.xlsx`.

### `pdf_to_txt.py`
Converte os documentos em PDF para arquivos TXT utilizados na construção do corpus.

### `bm25.py`
Gera rankings de similaridade entre os documentos utilizando o algoritmo BM25. Gera `ranking_bm25.xlsx`.

## Dependências

```bash
pip install requests openpyxl langdetect rank-bm25
```

## Fonte dos dados

- [SciELO Brasil](https://search.scielo.org/)
- [SciELO Portugal](https://scielo.pt/)
- API utilizada: [SciELO ArticleMeta](https://articlemeta.scielo.org/)
