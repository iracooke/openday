import json
import qrcode
import textwrap
from PIL import Image
from PIL import ImageDraw

from pathlib import Path
from jinja2 import Environment, FileSystemLoader

import gspread

import argparse

def generate_page(data,name,template):

    output_path = name + ".html"
    qr_path = "qr/" + name + ".png"
    url = "https://iracooke.github.io/openday/" + output_path


    # Generate and write HTML
    html_content = template.render(data)
    with open(output_path, "w") as f:
        f.write(html_content)

    print(f"HTML file generated: {output_path}")


    img = qrcode.make(url)
    print(type(img))  # qrcode.image.pil.PilImage
    img.save(qr_path)

def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line[1:], []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))


# Load the template
environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("dna.jinja")


# Load database
SAMPLE_SPREADSHEET_ID = "14pMt-_vrcE-Ki1b1txAZ_bRt3XTNqOr8TezFtef99yk"

gc = gspread.api_key("AIzaSyDTyI-uXJVFjG9_E0P8zreEZovTcgn7Y1Q")
sh = gc.open_by_key(SAMPLE_SPREADSHEET_ID)

worksheet = sh.sheet1
data = worksheet.get_all_records()

def noname(d):
    d.pop("name")
    return(d)

ddict = { d['name']:noname(d) for d in data }




for name,page_data in ddict.items():
#    import pdb;pdb.set_trace();

    ff = page_data['fasta']
    fd = [f for f in read_fasta(open(ff,'r'))]
    header,seq = fd[0]

    page_data['sequence'] = seq

    generate_page(page_data,name,template)



