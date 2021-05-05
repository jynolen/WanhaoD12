import argparse
from cairosvg import svg2png
from pathlib import Path

parser = argparse.ArgumentParser(description='Convert all svg in folder to png')
parser.add_argument("input_dir", type=Path)
parser.add_argument("ouput_dir", type=Path)

args = parser.parse_args()
args.ouput_dir.mkdir(exist_ok=True, parents=True)
for file in args.input_dir.iterdir():
    if not file.name.endswith(".svg"):
        continue
    with args.ouput_dir.joinpath(file.name.replace("svg", "png")).open("wb") as fw:
        fw.write(svg2png(file_obj=file.open()))