from abc import ABC
from lvgl.converter.base_converter import Converter
from lvgl.converter.lvgl_enum import ColorFormat
from lvgl.converter.utility import consume

class IndexedColorsConverter(Converter):
    def format_bin_out(self):
        result_bin_out = []
        row_size = (len(self.bin_out) - 4 * self.palette_size) / self.image.height 
        consumer = iter(self.bin_out)
        for _ in range(0, self.palette_size):
            result_bin_out.append(consume(consumer, 4))
        while True:
            try:
                result_bin_out.append(consume(consumer, row_size))
            except StopIteration:
                break
        return result_bin_out, self.palette_size, len(result_bin_out) - self.palette_size
        

class Indexed1ColorsConverter(IndexedColorsConverter):
    converter = ColorFormat.Indexed_1_Colors
    palette_size = 2
    lv_cf = 7

    def convert_pixel_internal(self, pixel, x, y):
        w = self.image.width >> 3
        if (self.image.width & 0x07):
            w += 1
        p = w * y + (x >> 3) + 8

        if len(self.bin_out) <= p:
            self.bin_out.append(0)
        assert(len(self.bin_out) >= p)
        self.bin_out[p] |= (pixel & 0x1) << (7 - (x & 0x7))

class Indexed2ColorsConverter(IndexedColorsConverter):
    converter = ColorFormat.Indexed_2_Colors
    palette_size = 4
    lv_cf = 8

    def convert_pixel_internal(self, pixel, x, y):
        w = self.image.width >> 2
        if (self.image.width & 0x03):
            w += 1
        p = w * y + (x >> 2) + 16

        if len(self.bin_out) <= p:
            self.bin_out.append(0)
        assert(len(self.bin_out) >= p)
        self.bin_out[p] |= (pixel & 0x3) << (6 - ((x & 0x3) * 2))

class Indexed4ColorsConverter(IndexedColorsConverter):
    converter = ColorFormat.Indexed_4_Colors
    palette_size = 16
    lv_cf = 9

    def convert_pixel_internal(self, pixel, x, y):
        w = self.image.width >> 1
        if (self.image.width & 0x01):
            w += 1
        p = w * y + (x >> 1) + 64
        if len(self.bin_out) <= p:
            self.bin_out.append(0)
        assert(len(self.bin_out) >= p)
        self.bin_out[p] |= (pixel & 0xF) << (4 - ((x & 0x1) * 4))

class Indexed8ColorsConverter(IndexedColorsConverter):
    converter = ColorFormat.Indexed_8_Colors
    palette_size = 256
    lv_cf = 10
    
    def convert_pixel_internal(self, pixel, x, y):
        self.bin_out.append(pixel & 0xFF)
