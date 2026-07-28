# Portuguese Biomedical Corpus Construction from SciELO

This repository was developed during the **INESC TEC Summer Research Internship 2026** at **LIAAD (Laboratory of Artificial Intelligence and Decision Support)**.

## Overview

This project presents a reproducible pipeline for constructing an initial Portuguese biomedical corpus from SciELO Brazil and SciELO Portugal.

The workflow automatically:

- Downloads SciELO XML metadata from seed articles.
- Identifies the language of each bibliographic reference.
- Extracts references written in Portuguese.
- Organizes the extracted references into spreadsheets.
- Retrieves the corresponding full-text documents.
- Converts PDF files into plain text.
- Prepares the corpus for Information Retrieval experiments.
- Generates BM25 similarity rankings.
- Supports manual relevance assessment.

---

# Workflow

```
Seed Articles
      │
      ▼
Download XML Metadata
      │
      ▼
Language Identification
      │
      ▼
Portuguese Reference Extraction
      │
      ▼
Reference Organization
      │
      ▼
Full-text Retrieval
      │
      ▼
PDF → TXT Conversion
      │
      ▼
Corpus Construction
      │
      ▼
BM25 Ranking
      │
      ▼
Manual Relevance Assessment
```

---

# Repository Structure

```
scripts/
│
├── baixar2_xmls.py
├── analisar_referencias.py
├── extrair_referencias.py
├── pdf_to_txt.py
└── bm25.py

examples/
│
├── analise_referencias.xlsx
├── referencias_pt.xlsx
└── ranking_bm25_ate11.xlsx
```

---

# Scripts

## baixar2_xmls.py

Downloads XML metadata from SciELO Brazil and SciELO Portugal.

---

## analisar_referencias.py

Analyzes all references found in the XML files and identifies their language.

Output:

- `analise_referencias.xlsx`

---

## extrair_referencias.py

Extracts only the references written in Portuguese.

Output:

- `referencias_pt.xlsx`

---

## pdf_to_txt.py

Converts downloaded PDF documents into plain text for corpus construction.

---

## bm25.py

Generates BM25 similarity rankings over the constructed Portuguese biomedical corpus.

Output:

- `ranking_bm25_ate11.xlsx`

---

# Technologies

- Python
- Pandas
- Requests
- BeautifulSoup
- XML Processing
- BM25
- Information Retrieval

---

# Example Outputs

The **examples** folder contains sample outputs generated during the internship:

- Reference language analysis
- Extracted Portuguese references
- BM25 similarity rankings

---

# Future Work

- Expand the corpus using all 32 seed articles.
- Publish the corpus on Hugging Face.
- Compare BM25 with transformer-based retrieval models.
- Prepare a scientific publication based on the corpus.

---

# Acknowledgements

This work was developed during the **INESC TEC Summer Research Internship 2026**.

Supervisor:

**Evelin Carvalho Freire de Amorim**

LIAAD – INESC TEC
