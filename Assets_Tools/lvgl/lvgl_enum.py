import enum
import decimal

def classify_pixel(pixel, bits):
    assert len(pixel) >= 3 and len(bits) >= 3
    ret = [-1, -1, -1]
    for i in range(0, 3):
        tmp = 1 << (8 - bits[i])
        val = decimal.Decimal(pixel[i] / tmp).quantize(0, decimal.ROUND_HALF_DOWN) * tmp
        val = 0 if val < 0 else int(val)
        ret[i] = val
    return tuple(ret)

class SmartEnum(enum.Enum):
    def __str__(self):
        return self.value

class RGB332:
    value = "bin_332"

    @classmethod
    def convert_rgba(cls, r, g, b, a, include_alpha=False):
        return [ r | (g >> 3) | (b >> 6) ] + ([a] if include_alpha else [])

    @classmethod
    def dithering(cls, pixel):
        r, g, b = classify_pixel(pixel, (3,3,2))
        return  {
            "r" : 0xe0 if r > 0xe0 else r,
            "g" : 0xe0 if g > 0xe0 else g,
            "b" : 0xc0 if b > 0xc0 else b
        }

    @classmethod
    def row_size(cls, width):
        return width

class RGB565:
    value = "bin_565"

    @classmethod
    def convert_rgba(cls, r, g, b, a, include_alpha=False):
        p = (r << 8) | (g << 3) | (b >> 3)
        return [ p & 0xff,  (p >> 8) & 0xff ]  + ([a] if include_alpha else [])

    @classmethod
    def dithering(cls, pixel):
        r, g, b = classify_pixel(pixel, (5,6,5))
        return {
            "r" : 0xf8 if r > 0xf8 else r,
            "g" : 0xfc if g > 0xfc else g,
            "b" : 0xf8 if b > 0xf8 else b
        }

    @classmethod
    def row_size(cls, width):
        return 2*width

class RGB565_SWAP:
    value = "bin_565_swap"

    @classmethod
    def convert_rgba(cls, r, g, b, a, include_alpha=False):
        p = (r << 8) | (g << 3) | (b >> 3)
        return [ (p >> 8) & 0xff, p & 0xff ] + ([a] if include_alpha else [])

    @classmethod
    def dithering(cls, pixel):
        r, g, b = classify_pixel(pixel, (5,6,5))
        return {
            "r" : 0xf8 if r > 0xf8 else r,
            "g" : 0xfc if g > 0xfc else g,
            "b" : 0xf8 if b > 0xf8 else b
        }

    @classmethod
    def row_size(cls, width):
        return 2*width

class RGB888:
    value = "bin_888"

    @classmethod
    def convert_rgba(cls, r, g, b, a, include_alpha=False):
        return [ b, g, r, a ]

    @classmethod
    def dithering(cls, pixel):
        r, g, b = classify_pixel(pixel, (8,8,8))
        return {
            "r" : 0xff if r > 0xff else r,
            "g" : 0xff if g > 0xff else g,
            "b" : 0xff if b > 0xff else b
        }

    @classmethod
    def row_size(cls, width):
        return 4*width

class OuputFormat(SmartEnum):
    RGB_332         = RGB332
    RGB_565         = RGB565
    RGB_565_SWAP    = RGB565_SWAP
    RGB_888         = RGB888

class ColorFormat(SmartEnum):
    True_Color              = "true_color"
    True_Color_Alpha        = "true_color_alpha"
    True_Color_Chroma_Keyed = "true_color_chroma"
    Indexed_1_Colors        = "indexed_1"
    Indexed_2_Colors        = "indexed_2"
    Indexed_4_Colors        = "indexed_4"
    Indexed_8_Colors        = "indexed_8"
    Alpha_1_Shades          = "alpha_1"
    Alpha_2_Shades          = "alpha_2"
    Alpha_4_Shades          = "alpha_4"
    Alpha_8_Shades          = "alpha_8"
    Raw                     = "raw"
    Raw_Alpha               = "raw_alpha"
    Raw_Chroma              = "raw_chroma"