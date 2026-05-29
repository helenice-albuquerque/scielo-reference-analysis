import os
import xml.etree.ElementTree as ET
from langdetect import detect, LangDetectException
import openpyxl

PASTA_XML = "xmls"

referencias = []

for arquivo in sorted(os.listdir("xmls")):
    if not arquivo.endswith(".xml"):
        continue

    caminho = os.path.join("xmls", arquivo)

    try:
        tree = ET.parse(caminho)
        root = tree.getroot()
    except ET.ParseError:
        continue

    # extrai referências — SciELO Brasil
    refs = []
    for elem in root.findall(".//{*}citation"):
        texto = " ".join(elem.itertext()).strip()
        if len(texto) > 20:
            refs.append((elem, texto))

    # extrai referências — SciELO Portugal
    if not refs:
        for tag in ["nlm-citation", "mixed-citation", "element-citation", "ref"]:
            for elem in root.iter(tag):
                texto = " ".join(elem.itertext()).strip()
                if len(texto) > 20:
                    refs.append((elem, texto))

    for elem, texto in refs:
        ref_lower = texto.lower()

        # detecta português
        is_pt = False
        if any(p in ref_lower for p in [" de ", " da ", " do ", " dos ", " das ", " e ", " em "]):
            is_pt = True
        else:
            try:
                if len(texto.split()) >= 5 and detect(texto) == "pt":
                    is_pt = True
            except LangDetectException:
                pass

        if not is_pt:
            continue

        # tenta extrair título
        titulo = ""
        for tag in ["article_title", "chapter-title", "source", "series_title"]:
            t = elem.find(f".//{tag}")
            if t is not None and t.text:
                titulo = t.text.strip()
                break
        
        # tenta com CDATA
        if not titulo:
            for tag in ["article_title", "source", "series_title"]:
                for t in elem.iter(tag):
                    txt = " ".join(t.itertext()).strip()
                    if txt:
                        titulo = txt
                        break

        if not titulo:

            partes = texto.split()

            # tenta encontrar ano
            pos_ano = -1

            for i, p in enumerate(partes):

                if p.isdigit() and len(p) == 4:

                    ano = int(p)

                    if 1900 <= ano <= 2035:
                        pos_ano = i
                        break

            # pega o que vem depois do ano
            if pos_ano != -1 and pos_ano + 1 < len(partes):

                titulo = " ".join(partes[pos_ano + 1:])

            else:
                titulo = texto[:150]  # usa o texto completo se não achar título

        referencias.append((titulo, arquivo))

# ordena alfabeticamente
referencias.sort(key=lambda x: x[0].lower())

# salva Excel
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Referências PT"
ws.append(["Nº", "Título da Referência", "Artigo de Origem"])
ws.column_dimensions["A"].width = 5
ws.column_dimensions["B"].width = 80
ws.column_dimensions["C"].width = 50

for i, (titulo, origem) in enumerate(referencias, 1):
    ws.append([i, titulo, origem])

wb.save("referencias_pt.xlsx")
print(f"Total: {len(referencias)} referências em português")
print("Arquivo 'referencias_pt.xlsx' criado!")