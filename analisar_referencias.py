import os
import xml.etree.ElementTree as ET
from langdetect import detect, LangDetectException
import openpyxl

PASTA_XML = "xmls"

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Análise de Referências"
ws.append(["Arquivo", "Total Refs", "Refs PT", "Refs EN", "Refs Outras", "% PT", "Tem PT?"])

for arquivo in sorted(os.listdir(PASTA_XML)):
    if not arquivo.endswith(".xml"):
        continue

    caminho = os.path.join(PASTA_XML, arquivo)

    try:
        tree = ET.parse(caminho)
        root = tree.getroot()
    except ET.ParseError:
        ws.append([arquivo, "ERRO PARSE", "", "", "", "", ""])
        continue

    # extrai texto de todas as tags de referência
    refs = []
    # para SciELO Brasil (com namespace)
    for elem in root.findall(".//{*}citation"):
        texto = " ".join(elem.itertext()).strip()
        if len(texto) > 20:
            refs.append(texto)

    # para SciELO Portugal (sem namespace)
    if not refs:
        for tag in ["nlm-citation", "mixed-citation", "element-citation", "ref"]:
            for elem in root.iter(tag):
                texto = " ".join(elem.itertext()).strip()
                if len(texto) > 20:
                    refs.append(texto)

    if not refs:
        ws.append([arquivo, 0, 0, 0, 0, "0%", "NÃO"])
        print(f"⚠ {arquivo} — nenhuma referência encontrada")
        continue

    pt, en, outras = 0, 0, 0
    for ref in refs:
        try:
            idioma = detect(ref)
            if idioma == "pt":
                pt += 1
            elif idioma == "en":
                en += 1
            else:
                outras += 1
        except LangDetectException:
            outras += 1

    total = len(refs)
    pct = f"{round(pt / total * 100, 1)}%"
    tem_pt = "SIM" if pt > 0 else "NÃO"

    ws.append([arquivo, total, pt, en, outras, pct, tem_pt])
    print(f"✓ {arquivo} — {total} refs | PT: {pt} | EN: {en} | Outras: {outras}")

wb.save("analise_referencias.xlsx")
print("\nConcluído! Verifica o arquivo 'analise_referencias.xlsx'")