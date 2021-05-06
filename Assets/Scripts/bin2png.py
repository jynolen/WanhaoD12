import argparse
import struct
import sys
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
    480*320*BYTES_PER_PIXEL: (480,320),
    320*240*BYTES_PER_PIXEL: (320,240),
    200*200*BYTES_PER_PIXEL: (200,200),
    150*80*BYTES_PER_PIXEL: (150,80),
    117*140*BYTES_PER_PIXEL:(117,140),
    117*92*BYTES_PER_PIXEL: (117,92),
    100*100*BYTES_PER_PIXEL: (100,100),
    70*40*BYTES_PER_PIXEL: (70,40),
    45*45*BYTES_PER_PIXEL: (45,45),
    50*50*BYTES_PER_PIXEL: (50,50),
    32*21*BYTES_PER_PIXEL: (32,21),
    18*14*BYTES_PER_PIXEL: (18,14),
    28*21*BYTES_PER_PIXEL: (28,21),
    90*30*BYTES_PER_PIXEL: (90,30),
    51*30*BYTES_PER_PIXEL: (51,30),
    70*28*BYTES_PER_PIXEL: (70,28),
    10*17*BYTES_PER_PIXEL: (10,17),
}

def find_closest_size(bytes_length):
    delta = sys.maxsize
    closest = -1
    for k,v in length2size.items():
        if abs(bytes_length - k) < delta:
            delta = abs(bytes_length - k)
            closest = k
    return length2size[closest]

### Convert All PNG
for file in input_dir.iterdir():
    if not file.name.endswith(".bin"):
        continue
    image_bytes = file.open("rb").read()
    header = struct.unpack("<L", image_bytes[0:4])[0]
    print(len(image_bytes)/2)
    if header & 0xff != 4:
        has_header = False
        picwidth, picheight = find_closest_size(len(image_bytes))
        # Exception
        if "bmp_circle" in file.name:
            picwidth, picheight = (52,12)
    else:
        header_only_hw = (header & 0xfffffff0)
        picheight = header_only_hw >> 21
        picwidth = (header_only_hw >> 10) & 0x3ff
        has_header = True

    image = Image.new('RGB', (picwidth, picheight))
    pixel_coord = itertools.product(range(picheight),range(picwidth))

    with file.open("rb") as fr:
        if has_header:
            _ = fr.read(4)
        current = fr.read(2)
        while current:
            if len(current) != 2:
                break
            short_ = struct.unpack("H", current)[0]
            r_ = (short_ & 0xf800) >> 8
            g_ = (short_ & 0x7e0) >> 3
            b_ = (short_ & 0x1f) << 3
            try:
                y, x = next(pixel_coord)
            except StopIteration:
                break
            image.putpixel((x,y), (r_, g_, b_))
            current = fr.read(2)
    if file.name == 'filamentchange.bin':
        print(image.size())
    image.save(ouput_dir.joinpath(file.name.replace(".bin", ".png")), 'png')
