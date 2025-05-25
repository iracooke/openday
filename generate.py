import json
from pathlib import Path

def generate_html(data):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{data.get('title', 'Untitled')}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 40px;
            line-height: 1.6;
        }}
        img {{
            max-width: 400px;
            height: auto;
            display: block;
            margin-bottom: 20px;
        }}
        .sequence {{
            font-family: monospace;
            white-space: pre-wrap;
            background-color: #f4f4f4;
            padding: 10px;
            border-left: 4px solid #ccc;
        }}
    </style>
</head>
<body>
    <h1>{data.get('title', '')}</h1>
    <h2><em>{data.get('commonname', '')}</em> (<i>{data.get('organism', '')}</i>)</h2>
    {"<p>" + data['about'] + "</p>" if data.get('about') else ""}
    <img src="{data.get('image', '')}" alt="{data.get('commonname', '')}">
    <h3>Sequence</h3>
    <div class="sequence">{data.get('sequence', '')}</div>
    <p><a href="{data.get('genbank', '#')}" target="_blank">View GenBank Entry</a></p>
</body>
</html>
"""
    return html

def main():
    input_path = "sepia_esculenta.json"  # Change this to your JSON filename
    output_path = "sepia_esculenta.html"

    # Load JSON data
    with open(input_path, "r") as f:
        data = json.load(f)

    # Generate and write HTML
    html_content = generate_html(data)
    with open(output_path, "w") as f:
        f.write(html_content)

    print(f"HTML file generated: {output_path}")

if __name__ == "__main__":
    main()
