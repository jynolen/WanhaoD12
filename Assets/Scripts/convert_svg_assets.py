import argparse
import re
import sys
import struct
from cairosvg import svg2png
from pathlib import Path
from PIL import Image

parser = argparse.ArgumentParser(description='Convert all svg in folder to png')
parser.add_argument("input_dir", type=Path)
parser.add_argument("ouput_dir", type=Path)
parser.add_argument("--header", action="store_true", default=False)

args = parser.parse_args()
ouput_dir: Path = args.ouput_dir
input_dir: Path = args.input_dir
include_header = args.header

ouput_dir.mkdir(exist_ok=True, parents=True)
ouput_dir.joinpath(".png").mkdir(exist_ok=True, parents=True)

# First Convert all SVG into png
for file in input_dir.iterdir():
    if not file.name.endswith(".svg"):
        continue
    if ouput_dir.joinpath(".png", file.name.replace("svg", "png")).exists():
        continue    
    with ouput_dir.joinpath(".png", file.name.replace("svg", "png")).open("wb") as fw:
        fw.write(svg2png(file_obj=file.open()))


# Second convert all png into bin
for file in ouput_dir.joinpath(".png").iterdir():
    if not file.name.endswith(".png"):
        continue
    img = Image.open(file)
    pixs = img.load()
    width, height = img.size
    if ouput_dir.joinpath(file.name.replace(".png", ".bin")).exists():
        continue    
    with open(ouput_dir.joinpath(file.name.replace(".png", ".bin")), "wb") as fw:

        if include_header:
            fw.write(struct.pack("<L", 0x4 + (img.height << 21) + (img.width << 10 )))
        for y in range(0, height):
            for x in range(0, width):
                current_pixel = pixs[x, y]
                r, g, b = current_pixel[0] >> 3, current_pixel[1] >> 2, current_pixel[2] >> 3
                rgb = (r << 11) | (g << 5) | b
                fw.write(struct.pack('H', rgb))

### Make sure every image define in code are present in output dir
failed = False
mksui = Path("AutoBuild-MarlinFirware/Marlin/src/lcd/extui/lib/mks_ui")
file_regex = re.compile(r"/(bmp\S+.bin)")
files = set()
for file in mksui.iterdir():
    file_data = file.open("r", encoding="utf-8").read()
    for match in file_regex.finditer(file_data):
        image_file_name = match.group(1)
        files.add(image_file_name)

for image_file_name in files:
    if not ouput_dir.joinpath(image_file_name).exists():
        print(f"{image_file_name} does not exists in output dir", file=sys.stderr)
        failed = True