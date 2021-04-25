import io
from abc import ABC
from lvgl.converter.base_converter import Converter
from lvgl.lvgl_enum import ColorFormat
from lvgl.converter.utility import consume

class BaseRawConverter(Converter):
    def convert_pixel_internal(self, pixel):
        pass

    def convert(self, alpha=0):
        output = io.BytesIO()
        self.image.save(output, format=self.image.format)
        self.bin_out = output.getvalue()

    def export_to_bin(self):
        return bytearray()

    def format_bin_out(self):
        result_bin_out = []       
        row_size = 16
        consumer = iter(self.bin_out)
        while True:
            try:
                result_bin_out.append(consume(consumer, row_size))
            except StopIteration:
                break
        return result_bin_out, 0, len(result_bin_out)


class RawConverter(BaseRawConverter):
    converter = ColorFormat.Raw

class RawAlphaConverter(BaseRawConverter):
    converter = ColorFormat.Raw_Alpha

class RawChromaConverter(BaseRawConverter):
    converter = ColorFormat.Raw_Chroma
