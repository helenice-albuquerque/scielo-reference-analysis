import os
import xml.etree.ElementTree as ET
from langdetect import detect, LangDetectException
import openpyxl

PASTA_XML = "xmls"

referencias = []

for arquivo in sorted(os.listdir(PASTA_XML)):

    if not arquivo.endswith(".xml"):
        continue

    caminho = os.path.join(PASTA_XML, arquivo)

    try:
        tree = ET.parse(caminho)
        root = tree.getroot()

    except ET.ParseError:
        continue

    refs = []

    # tenta padrão SciELO Brasil
    for elem in root.findall(".//{*}citation"):

        texto = " ".join(elem.itertext()).strip()

        if len(texto) > 20:
            refs.append((elem, texto))

    # tenta outros padrões
    if not refs:

        for tag in [
            "nlm-citation",
            "mixed-citation",
            "element-citation",
            "ref"
        ]:

            for elem in root.iter(tag):

                texto = " ".join(elem.itertext()).strip()

                if len(texto) > 20:
                    refs.append((elem, texto))

    for elem, texto in refs:

        ref_lower = texto.lower()

        # detecta português
        is_pt = False

        palavras_pt = [
            " de ",
            " da ",
            " do ",
            " dos ",
            " das ",
            " e ",
            " em "
        ]

        if any(p in ref_lower for p in palavras_pt):
            is_pt = True

        else:
            try:
                if len(texto.split()) >= 5:

                    if detect(texto) == "pt":
                        is_pt = True

            except LangDetectException:
                pass

        if not is_pt:
            continue

        titulo = ""

        # tenta pegar título do artigo
        for tag in [
            "article-title",
            "chapter-title"
        ]:

            t = elem.find(f".//{{*}}{tag}")

            if t is not None:

                txt = " ".join(t.itertext()).strip()

                if txt:
                    titulo = txt
                    break

        # se nao achar, tenta outras tags
        if not titulo:

            for tag in [
                "source",
                "series-title"
            ]:

                t = elem.find(f".//{{*}}{tag}")

                if t is not None:

                    txt = " ".join(t.itertext()).strip()

                    if txt:
                        titulo = txt
                        break

        # fallback
        if not titulo:
            titulo = texto[:150]

        referencias.append((titulo, arquivo))

# ordena alfabeticamente
referencias.sort(key=lambda x: x[0].lower())

# cria excel
wb = openpyxl.Workbook()

ws = wb.active
ws.title = "Referências PT"

ws.append([
    "Nº",
    "Título da Referência",
    "Artigo de Origem"
])

ws.column_dimensions["A"].width = 5
ws.column_dimensions["B"].width = 100
ws.column_dimensions["C"].width = 50

for i, (titulo, origem) in enumerate(referencias, 1):

    ws.append([
        i,
        titulo,
        origem
    ])

wb.save("referencias_pt.xlsx")

print(f"Total: {len(referencias)} referências em português")
print("Arquivo 'referencias_pt.xlsx' criado!")