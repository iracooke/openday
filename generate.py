import json
import qrcode
import textwrap
from PIL import Image
from PIL import ImageDraw

from pathlib import Path
from jinja2 import Environment, FileSystemLoader

import gspread

import argparse

def generate_page(data,template):

    output_path = "test" + ".html"

    # Generate and write HTML
    html_content = template.render(data[0])
    with open(output_path, "w") as f:
        f.write(html_content)

    print(f"HTML file generated: {output_path}")

    img = qrcode.make('https://iracooke.github.io/openday/sepia_esculenta.html')
    print(type(img))  # qrcode.image.pil.PilImage
    img.save("qr/sepia_esculenta_front.png")

# img = Image.new('RGB', (410, 410),(255, 255, 255))
# d = ImageDraw.Draw(img)
# d.text((20, 20), data['sequence'], fill=(0, 0, 0),font_size=20)

# img.save("qr/sepia_esculenta_back.png")


# Load database
SAMPLE_SPREADSHEET_ID = "14pMt-_vrcE-Ki1b1txAZ_bRt3XTNqOr8TezFtef99yk"

gc = gspread.api_key("AIzaSyDTyI-uXJVFjG9_E0P8zreEZovTcgn7Y1Q")
sh = gc.open_by_key(SAMPLE_SPREADSHEET_ID)

worksheet = sh.sheet1
data = worksheet.get_all_records()

# Load the template
environment = Environment(loader=FileSystemLoader("templates/"))
template = environment.get_template("dna.jinja")
