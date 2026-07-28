# SciELO Reference Analysis

This repository contains Python scripts for constructing a Portuguese biomedical corpus from SciELO systematic reviews.

## Workflow

- Download XML metadata from SciELO.
- Analyze the language of bibliographic references.
- Extract references written in Portuguese.
- Retrieve the corresponding full-text documents.
- Convert PDF files to TXT.
- Generate BM25 similarity rankings.

## Scripts

- `baixar2_xmls.py` – Downloads XML files from SciELO.
- `analisar_referencias.py` – Identifies the language of references.
- `extrair_referencias.py` – Extracts Portuguese references.
- `pdf_to_txt.py` – Converts PDF files to TXT.
- `bm25.py` – Generates BM25 rankings.

## Requirements

- Python 3
- pandas
- requests
- beautifulsoup4
- lxml
- rank-bm25

## Example Outputs

- `analise_referencias.xlsx`
- `referencias_pt.xlsx`
- `ranking_bm25_ate11.xlsx`
