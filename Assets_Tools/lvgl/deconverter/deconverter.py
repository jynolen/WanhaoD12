"""
    Convert Back RGB565 back to png to identify what to change
"""
import struct
from PIL import Image
import numpy
from lvgl.converter.lvgl_enum import OuputFormat, ColorFormat
from lvgl.converter import Converter

class Deconverter:
    def __init__(self, fr, output_mode):
        self.img = fr
        self.img_fw = fr.open("rb")
        header = self.img_fw.read(4)
        header = struct.unpack('<L', header)[0]
        self.output_mode = [ c for c in OuputFormat if c.value == output_mode][0]
        self.height = header >> 21
        self.width = (header & 0xFFFFF) >> 10
        self.img_mode  = Converter.get_class_from_header( header & 0xF )


    def convert(self):
        """Convert RAW file *fil* to a 2D array."""
        #header = 4 + (89 << 10) + ( 97 << 21)
        #header = struct.pack("<L", header)
        images = []
        for _ in range(self.height):
            row = []
            for _ in range(self.width): 
                s = self.img_fw.read(self.output_mode.value.bytes_per_pixel)
                r,g,b = self.output_mode.value.convert_bin(s)
                alpha = 0xff
                if self.img_mode.alpha:
                    alpha = int.from_bytes(self.img_fw.read(1), byteorder='little')
                row.append([r, g, b, alpha])
            images.append(row)
        return numpy.array(images, dtype=numpy.uint8)

    def perform(self, output):
        #try:
            bytes_ = self.convert()
            image = Image.fromarray(bytes_, 'RGBA')
            image.save(output)
        #except Exception as e:
        #    print(f"Unable to convert file {self.img} - {e}")
