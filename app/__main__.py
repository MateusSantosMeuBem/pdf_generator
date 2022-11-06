# --------- BUILT-IN PACKAGES ---------
import json

file_path: str = r''

# --------- EXTERNAL PACKAGES ---------
from fpdf import FPDF
import qrcode

with open(
    file=file_path,
    mode='r',
    encoding='utf-8'
) as file_: 
    content: list = json.load(file_)

pdf = FPDF()
pdf.add_page()


for data in content['data']:
    pdf.set_font("Arial", size = 16, style='B')
    title: str = data['title']
    pdf.cell(185, 10, txt = title,
            ln = 1, align = 'C')

    pdf.set_font("Arial", size = 12, style='')
    description: str = data['description']
    pdf.multi_cell(185, 10, txt = description, align = 'J')
    urls: list[dict[str, str]] = data['urls']

    for url in urls:
        pdf.set_font("Arial", size = 12, style='B')
        pdf.cell(
            w=200,
            h=10,
            txt='\n',
            ln=1, align='C'
        )
        pdf.cell(
            w=200,
            h=10,
            txt=f'{url["title"]}',
            ln=1, align='C'
        )
        image_filename: str = 'image.png'
        img = qrcode.make(
            data=url["url"],
            box_size=2
        )
        img.save(image_filename)

        pdf.image(
            name=image_filename,
            x=90
        )
        for i in range(2):
            pdf.cell(
                w=200,
                h=10,
                txt='\n',
                ln=1, align='C'
            )

pdf.set_font("Arial", size = 6, style='')
final_maessage: str = 'Esse pdf foi gerado utilizando Python e práticas de programação horríveis.Não reproduzir em casa. =D'
pdf.cell(
    w=200,
    h=10,
    txt=final_maessage,
    ln=1, align='C'
)
pdf.output("GFG.pdf")  