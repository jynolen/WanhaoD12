import argparse
import struct
import itertools
from pathlib import Path
from PIL import Image

BYTES_PER_PIXEL = 2

parser = argparse.ArgumentParser(description='Convert all svg in folder to png')
parser.add_argument("input_dir", type=Path)
parser.add_argument("ouput_dir", type=Path)

args = parser.parse_args()
ouput_dir: Path = args.ouput_dir
input_dir: Path = args.input_dir
ouput_dir.mkdir(exist_ok=True, parents=True)


length2size = {
    320*240*BYTES_PER_PIXEL: (320,240),
    200*200*BYTES_PER_PIXEL: (200,200),
    150*80*BYTES_PER_PIXEL: (150,80),
    117*140*BYTES_PER_PIXEL:(117,140),
    117*92*BYTES_PER_PIXEL: (117,92),
    100*100*BYTES_PER_PIXEL: (100,100)
}

### Convert All PNG
for file in input_dir.iterdir():
    if not file.name.endswith(".bin"):
        continue
    image_bytes = file.open("rb").read()

    """
        This is to rewrite
    """
    picwidth = 117
    picheight = 140
    x=0
    y=0    
    if file.name == "bmp_logo.bin":
        picwidth = 480
        picheight = 320
    elif file.name == "bmp_preview.bin":
        picwidth = 200
        picheight = 200
    elif file.name == "bmp_pause.bin" or file.name == "bmp_stop.bin":
        picwidth = 150
        picheight = 80
    elif len(image_bytes)/2 < picwidth*picheight:
        picwidth = 150
        picheight = 80
        if len(image_bytes)/2 <picwidth*picheight:
            picwidth = 117
            picheight = 92
            if len(image_bytes)/2 < picwidth*picheight:
                picwidth = 100
                picheight = 100
                if len(image_bytes)/2 < picwidth*picheight:
                    exit
    #size = length2size[len(image_bytes)]
    image = Image.new('RGB', (picwidth, picheight))
    pixel_coord = itertools.product(range(picheight),range(picwidth))
    with file.open("rb") as fr:
        current = fr.read(2)
        while current:
            if len(current) != 2:
                break
            short_ = struct.unpack("H", current)[0]
            r_ = (short_ & 0xf800) >> 8
            g_ = (short_ & 0x7e0) >> 3
            b_ = (short_ & 0x1f) << 3
            try:
                y,x = next(pixel_coord)
            except StopIteration:
                break
            image.putpixel((x,y), (r_, g_, b_))
            current = fr.read(2)
    if file.name == 'filamentchange.bin':
        print(image.size())
    image.save(ouput_dir.joinpath(file.name.replace(".bin", ".png")), 'png')