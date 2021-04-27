import struct
import io

from jinja2 import Template
from PIL import Image
from abc import ABC, abstractmethod
from lvgl.converter.utility import palette_to_rgb
from lvgl.converter.lvgl_enum import ColorFormat, OuputFormat
from pathlib import Path
from math import log2
from abc import ABC
from cairosvg import svg2png

class Converter(ABC):
    converter: ColorFormat
    palette_size = 0
    alpha = 0
    alpha_size = 0
    c_array = []
    lv_cf = None
    dithering = False
    
    @classmethod
    def instanciate(cls, format: ColorFormat):
        for c in cls.__subclasses__():
            for sub in c.__subclasses__():
                if sub.converter == format:
                    return sub
        raise NotImplementedError()

    @classmethod
    def get_class_from_header(cls, header):
        for c in cls.__subclasses__():
            for sub in c.__subclasses__():
                if sub.lv_cf == header:
                    return sub
        raise NotImplementedError()


    @abstractmethod
    def convert_pixel_internal(self, pixel, x, y):
        raise NotImplementedError()
        
    def format_bin_out(self):
        return self.bin_out, 0, len(self.bin_out)

    def jinja_params(self):
        bin_out, header_size, row_count = self.format_bin_out()
        return {  
            "width":self.image.width,
            "height":self.image.height,
            "include_name":self.filename.upper(),
            "output_name_file":self.filename.lower(),
            "len_bin_out":len(self.bin_out),
            "palette_size":self.palette_size,
            "alpha_size":self.alpha_size,
            "log2_indexed":int(log2(self.palette_size)) if self.palette_size else None,
            "log2_alpha":int(log2(self.alpha_size)) if self.alpha_size else None,
            "bin_out": iter(bin_out),
            "bin_out_header": header_size,
            "bin_out_row_count": row_count,
            self.converter.value: True
        }

    def __init__(self, args):
        self.file = args["file"]
        self.dithering = args["dithering"]
        self.output_mode = args["output_format"]
        self.filename = self.file.name.split(".")[0]

        try:
            self.image: Image = Image.open(self.file)
        except:
            try:
                self.image = Image.open(io.BytesIO(svg2png(file_obj=self.file.open())))
            except:
                raise ValueError("Unsupported Image format")
        if self.alpha:
            self.image = self.image.convert("RGBA")

        self.earr = {"r": [], "g": [], "b": []}
        self.nerr = {"r": 0, "g": 0, "b": 0}
        self.act = {"r":None, "g":None, "b": None }

        if self.dithering:
            self.earr["r"] = [0] * (self.image.width + 2)
            self.earr["g"] = [0] * (self.image.width + 2)
            self.earr["b"] = [0] * (self.image.width + 2)

        self.bin_out = []

    def palette_convert(self):
        assert(self.palette_size != 0)
        self.image = self.image.convert("RGB").quantize(self.palette_size, Image.MEDIANCUT)

        # Make sure the resulting image as at most palette size colors
        assert(len(self.image.convert('RGB').getcolors()) <= self.palette_size)

        # Retreive RGB from Palette based on pixel count
        for (red, green, blue) in palette_to_rgb(self.image.getcolors(), self.image.convert('RGB').getcolors()):
            self.bin_out += [blue, green, red, 0xff]

        # If original image as less color than the palette complete-it to white
        for _ in range(0, self.palette_size - len(self.image.getcolors())):
            self.bin_out += [0xff, 0xff, 0xff, 0xff]

        # Make sure we push the right amount of data in resulting binarry
        assert(len(self.bin_out) == 4*self.palette_size)

    def dithering_reset(self):
        if self.dithering:
            self.nerr = {"r": 0, "g": 0, "b": 0}

    def dithering_next(self, pixel, x):
        pass

    def convert_pixel(self, x, y):
        self.dithering_next(self.image.getpixel((x, y)), x)
        self.convert_pixel_internal(self.image.getpixel((x, y)), x, y)

    def convert(self):
        if self.palette_size:
            self.palette_convert()
        for y in range(0, self.image.height):
            self.dithering_reset()
            for x in range(0, self.image.width):
                self.convert_pixel(x, y)

    def export_to_bin(self):
        header = self.lv_cf + (self.image.width << 10) + (self.image.height << 21)
        header_bin = struct.pack("<L", header)
        return bytearray(header_bin) + bytearray(self.bin_out)

    def export(self, c_array=True):
        if c_array:
            return self.export_to_c_array()
        else:
            return self.export_to_bin()

    def export_to_c_array(self):
        with Path(__file__).parent.joinpath("c_array.jinja").open() as fp:
            template_content = fp.read()
        template = Template(template_content)
        return template.render(self.jinja_params())

