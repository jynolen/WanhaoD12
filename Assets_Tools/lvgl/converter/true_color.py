from lvgl.converter.base_converter import Converter
from lvgl.lvgl_enum import ColorFormat, OuputFormat
from jinja2 import Template
from pathlib import Path
from abc import ABC
from lvgl.converter.utility import consume
import copy

class TrueColorCommonConverter(Converter):
    act = {"r":None, "g":None, "b": None }
    nerr = {"r":None, "g":None, "b": None }
    narr = {"r":[None], "g":[None], "b": [None] }

    def format_bin_out(self, data=None):
        result_bin_out = []       
        data = self.bin_out if not data else data
        row_size = int(len(data)/self.image.height)
        consumer = iter(data)
        while True:
            try:
                result_bin_out.append(consume(consumer, row_size))
            except StopIteration:
                break
        return result_bin_out, 0, len(result_bin_out)

    def convert_pixel_internal(self, pixel, x, y):
        alpha = 0xff if self.converter != ColorFormat.True_Color_Alpha else pixel[3]
        self.bin_out+= self.output_mode.convert_rgba(self.act["r"], self.act["g"], self.act["b"], alpha, self.alpha)

    def dithering_next(self, pixel, x):
        if self.dithering:
            self.act = {
                "r" : pixel[0] + self.nerr["r"] + self.narr["r"][x+1],
                "g" : pixel[1] + self.nerr["g"] + self.narr["g"][x+1],
                "b" : pixel[2] + self.nerr["b"] + self.narr["b"][x+1]
            }
            self.narr["r"][x+1] = self.narr["g"][x+1] = self.narr["b"][x+1] = 0
            
            self.act = self.output_mode.dithering(pixel)
            self.err = copy.deepcopy(self.act)
            
            for key, value in self.err.items(): # key <=> ["r", "g", "b"]
                self.err[key] = round((7 * value) /16)

            for key in ["r", "g", "b"]:
                self.narr[x][key] += round((3 * self.err[key]) / 16)
                self.narr[x+1][key] += round((5 * self.err[key]) / 16)
                self.narr[x+2][key] += round(self.err[key] / 16)
        else:
            self.act = self.output_mode.dithering(pixel)
    
    def export_to_c_array(self):
        true_color_out = { self.output_mode.value : copy.deepcopy(self.bin_out) }
        for of in list(OuputFormat):
            output_format = of.value
            if output_format == self.output_mode:
                continue
            converter = self.__class__(args = {"dithering": self.dithering, "file": self.file, "output_format": output_format})
            converter.convert()
            true_color_out[output_format.value] = converter.bin_out
        
        with Path(__file__).parent.joinpath("c_array.jinja").open() as fp:
            template_content = fp.read()
        template = Template(template_content)
        params = self.jinja_params()
        bin_332, _, _ = self.format_bin_out(true_color_out["bin_332"])
        bin_565, _, _ = self.format_bin_out(true_color_out["bin_565"])
        bin_565_swap, _, _ = self.format_bin_out(true_color_out["bin_565_swap"])
        bin_888, _, _ = self.format_bin_out(true_color_out["bin_888"])
        params.update({
            "true_color_bin332": bin_332,
            "true_color_bin565": bin_565,
            "true_color_bin565_swap": bin_565_swap,
            "true_color_bin888": bin_888
        })
        return template.render(params)


class TrueColorConverter(TrueColorCommonConverter):
    converter = ColorFormat.True_Color
    lv_cf = 4

class TrueColorAlphaConverter(TrueColorCommonConverter):
    converter = ColorFormat.True_Color_Alpha
    alpha = 1
    lv_cf = 5

class TrueColorChromaConverter(TrueColorCommonConverter):
    converter = ColorFormat.True_Color_Chroma_Keyed
    lv_cf = 6