from PIL import Image
import os
from pypdf import PdfMerger

# Caminho para a pasta contendo os arquivos PNG
input_folder = 'PDFs/'
output_pdf = 'merged.pdf'

# Lista para armazenar os caminhos dos arquivos PDF temporários
temp_pdfs = []

# Converter cada arquivo PNG em PDF
for image_file in os.listdir(input_folder):
    if image_file.endswith('.png'):
        image_path = os.path.join(input_folder, image_file)
        pdf_path = image_path.replace('.png', '.pdf')
        temp_pdfs.append(pdf_path)

        image = Image.open(image_path)
        # Convertendo imagem para RGB, necessário para imagens PNG com transparência
        image = image.convert('RGB')
        image.save(pdf_path)

# Mesclar os PDFs criados
merger = PdfMerger()

for pdf in temp_pdfs:
    merger.append(pdf)

merger.write(output_pdf)
merger.close()

# Opcional: Remover os arquivos PDF temporários
for pdf in temp_pdfs:
    os.remove(pdf)