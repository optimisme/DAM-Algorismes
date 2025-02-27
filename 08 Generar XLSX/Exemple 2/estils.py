#!/usr/bin/env python3
import xlsxwriter

filename = "estils.xlsx"
workbook = xlsxwriter.Workbook(filename)
worksheet = workbook.add_worksheet("Fruites")

# Formats
bold = workbook.add_format({'bold': True})
italic = workbook.add_format({'italic': True})
centered = workbook.add_format({'align': 'center', 'valign': 'vcenter'})
right_aligned = workbook.add_format({'align': 'right', 'valign': 'vcenter'})
red_background = workbook.add_format({'bg_color': '#FF0000', 'font_color': '#FFFFFF',  'align': 'center', 'valign': 'vcenter'})
green_text = workbook.add_format({'font_color': '#00AA00', 'align': 'right', 'valign': 'vcenter'})
bold_total = workbook.add_format({'bold': True, 'align': 'left'})

# Dades
data = [
    ["Poma", 4.75, 2],
    ["Plàtan", 3.00, 1.5],
    ["Maduixa", 5.50, 1],
    ["Raïm", 6.25, 0.8],
    ["Taronja", 2.50, 3]
]

# Afegir capçalera
worksheet.write_row(0, 0, ["Fruita", "Preu/kg (€)", "Quantitat (kg)", "Preu Final (€)"], bold)

# Afegir dades
row = 1
for fruit, price_per_kg, quantity in data:
    worksheet.write(row, 0, fruit, italic)      # Primera columna: cursiva
    worksheet.write(row, 1, price_per_kg)       # Segona columna: centrat
    worksheet.write(row, 2, quantity, centered) # Tercera columna: centrat
    formula = f"B{row + 1}*C{row + 1}"          # Quarta columna: fórmula
    worksheet.write_formula(row, 3, formula, right_aligned)
    row += 1

# Formats condicionals
worksheet.conditional_format("B2:B6", {
    'type': 'cell',
    'criteria': '<',
    'value': 5,
    'format': workbook.add_format({'bg_color': '#00AA00', 'font_color': '#FFFFFF', 'align': 'center', 'valign': 'vcenter'})
})
worksheet.conditional_format("D2:D6", {
    'type': 'cell',
    'criteria': '>=',
    'value': 5,
    'format': workbook.add_format({'bg_color': '#FFCC00', 'font_color': '#AA0000', 'align': 'right', 'valign': 'vcenter'})
})

# Afegir total
worksheet.write(row, 0, "TOTAL", bold_total)
worksheet.write(row, 3, "=SUM(D2:D6)", bold)

workbook.close()
print(f"Generated: '{filename}'")


