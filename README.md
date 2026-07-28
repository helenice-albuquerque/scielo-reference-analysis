# Corpus Biomédico em Português — SciELO

Coleta e organização de revisões sistemáticas biomédicas em português para construção de um corpus destinado a experimentos de Recuperação de Informação e modelos de linguagem.

## Descrição

Este projeto coleta 32 artigos de revisão sistemática do domínio biomédico a partir do SciELO Brasil e SciELO Portugal, baixa seus metadados em formato XML, identifica referências bibliográficas em português, recupera os documentos completos, converte PDFs para TXT e realiza experimentos de similaridade utilizando TF-IDF e BM25.

## Scripts

### `baixar2_xmls.py`
Baixa os metadados dos artigos em formato XML. Adiciona 3 tentativas por artigo e ignora arquivos já existentes, evitando downloads duplicados.

### `analisar_referencias.py`
Analisa os XMLs e contabiliza as referências em português, inglês e outros idiomas. Gera `analise_referencias.xlsx`.

### `extrair_referencias_pt.py`
Extrai as referências em português, recupera seus títulos e gera `referencias_pt.xlsx`.

### `pdf_to_txt.py`
Converte os documentos PDF para arquivos TXT.

### `bm25.py`
Calcula a similaridade entre os documentos utilizando TF-IDF e BM25, gerando rankings para análise.

## Dependências

```bash
pip install requests openpyxl langdetect rank-bm25 nltk scikit-learn pandas numpy
```

## Fonte dos dados

- SciELO Brasil
- SciELO Portugal
- SciELO ArticleMeta API
