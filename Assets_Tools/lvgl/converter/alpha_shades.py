from lvgl.converter.base_converter import Converter
from lvgl.lvgl_enum import ColorFormat
from lvgl.converter.utility import consume

class AlphaShadesConverter(Converter):
    converter = None
    alpha_size = None
    bin_out = []
    image = None

    def format_bin_out(self):
        result_bin_out = []       
        row_size = len(self.bin_out) / self.image.height
        consumer = iter(self.bin_out)
        while True:
            try:
                result_bin_out.append(consume(consumer, row_size))
            except StopIteration:
                break
        return result_bin_out, 0, len(result_bin_out)

class Alpha1ShadesConverter(AlphaShadesConverter):
    converter = ColorFormat.Alpha_1_Shades
    alpha = 1
    alpha_size = 2
    lv_cf = 11

    def convert_pixel_internal(self, pixel, x, y):
        current_alpha = pixel[3]
        w = self.image.width >> 3
        if (self.image.width & 0x07):
            w += 1
        p = w * y + (x >> 3)
        try:
            _ = self.bin_out[p]
        except IndexError:
            self.bin_out.insert(p, 0)
        assert(self.bin_out[p] >= 0)

        if (current_alpha > 0x80):
            self.bin_out[p] |= 1 << (7 - (x & 0x7))

class Alpha2ShadesConverter(AlphaShadesConverter):
    converter = ColorFormat.Alpha_2_Shades
    alpha = 1
    alpha_size = 4
    lv_cf = 12

    def convert_pixel_internal(self, pixel, x, y):
        current_alpha = pixel[3]
        w = self.image.width >> 2
        if (self.image.width & 0x03):
            w += 1
        p = w * y + (x >> 2)
        try:
            _ = self.bin_out[p]
        except IndexError:
            self.bin_out.insert(p, 0)
        assert(self.bin_out[p] >= 0)
        self.bin_out[p] |= (current_alpha >> 6) << (6 - ((x & 0x3) * 2))

class Alpha4ShadesConverter(AlphaShadesConverter):
    converter = ColorFormat.Alpha_4_Shades
    alpha = 1
    alpha_size = 16
    lv_cf = 13

    def convert_pixel_internal(self, pixel, x, y):
        current_alpha = pixel[3]
        w = self.image.width >> 1
        if (self.image.width & 0x01):
            w += 1
        p = w * y + (x >> 1)
        try:
            _ = self.bin_out[p]
        except IndexError:
            self.bin_out.insert(p, 0)
        assert(self.bin_out[p] >= 0)
        self.bin_out[p] |= (current_alpha >> 4) << (4 - ((x & 0x1) * 4))

class Alpha8ShadesConverter(AlphaShadesConverter):
    converter = ColorFormat.Alpha_8_Shades
    alpha = 1
    alpha_size = 256
    lv_cf = 14

    def convert_pixel_internal(self, pixel, x, y):
        pixel = self.image.convert("RGBA").getpixel((x,y))
        current_alpha = pixel[3]
        p = self.image.width * y + x
        try:
            _ = self.bin_out[p]
        except IndexError:
            self.bin_out.insert(p, 0)
        assert(self.bin_out[p] >= 0)        
        self.bin_out[p] = current_alpha

