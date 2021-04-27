import enum
import decimal
import struct

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
    bytes_per_pixel = 1
    @classmethod
    def convert_rgba(cls, r, g, b, a, include_alpha=False):
        # Keep most signicant bits of each colors
        r_mask = 0b11100000 # 3 bits for red
        g_mask = 0b00011100 # 3 bits for green
        b_mask = 0b00000011 # 3 bits for blue
        
        r_ = (    r     & r_mask )
        g_ = ( (g >> 3) & g_mask )
        b_ = ( (b >> 6) & b_mask )
        return [ r_ | g_ | b_ ] + ([a] if include_alpha else [])

    @classmethod
    def convert_bin(cls, pixel):
        pixel  = struct.unpack(f'>B', pixel)[0]
        r_mask = 0b11100000
        g_mask = 0b00011100
        b_mask = 0b00000011

        r = ( pixel & r_mask )
        g = ( pixel & g_mask ) << 3 
        b = ( pixel & b_mask ) << 5 
        
        return r,g,b
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
    bytes_per_pixel = 2
    @classmethod
    def convert_rgba(cls, r, g, b, a, include_alpha=False):
        # Keep most signicant bits of each colors
        r_mask = 0b11111000 # 5 bits for red
        g_mask = 0b11111100 # 6 bits for green
        b_mask = 0b11111000 # 5 bits for blue

        
        r_ =   ( r  & r_mask )        << 8 
        g_ = ( ( g  & g_mask ) >> 2 ) << 5
        b_ = ( ( b  & g_mask ) >> 3 )

        long = r_ | g_ | b_
        return [ (long >> 8), long & 0xff ] + ([a] if include_alpha else [])

    @classmethod
    def dithering(cls, pixel):
        r, g, b = classify_pixel(pixel, (5,6,5))
        return {
            "r" : 0xf8 if r > 0xf8 else r,
            "g" : 0xfc if g > 0xfc else g,
            "b" : 0xf8 if b > 0xf8 else b
        }

    @classmethod
    def convert_bin(cls, pixel):
        pixel  = struct.unpack(f'>H', pixel)[0]
        r_mask = 0b1111100000000000
        g_mask = 0b0000011111100000
        b_mask = 0b0000000000111111

        r = ( pixel & r_mask ) >> 8
        g = ( pixel & g_mask ) >> 3
        b = ( pixel & b_mask ) << 3

        return r,g,b

    @classmethod
    def row_size(cls, width):
        return 2*width

class RGB565_SWAP:
    value = "bin_565_swap"
    bytes_per_pixel = 2
    @classmethod
    def convert_rgba(cls, r, g, b, a, include_alpha=False):
        # Keep most signicant bits of each colors
        r_mask = 0b11111000 # 5 bits for red
        g_mask = 0b11111100 # 6 bits for green
        b_mask = 0b11111000 # 5 bits for blue

        r_ = ( ( r  & r_mask ) >> 3 )       
        g_ = ( ( g  & g_mask ) >> 2 ) << 5
        b_ =   ( b_ & g_mask )        << 8
        
        long = r_ | g_ | b_
        return [ (long >> 8), long & 0xff ] + ([a] if include_alpha else [])

    @classmethod
    def dithering(cls, pixel):
        r, g, b = classify_pixel(pixel, (5,6,5))
        return {
            "r" : 0xf8 if r > 0xf8 else r,
            "g" : 0xfc if g > 0xfc else g,
            "b" : 0xf8 if b > 0xf8 else b
        }

    @classmethod
    def convert_bin(cls, pixel):
        pixel  = struct.unpack(f'>H', pixel)[0]

        r_mask = 0b0000000000111111
        g_mask = 0b0000011111100000
        b_mask = 0b1111100000000000

        r = ( pixel & r_mask ) << 3
        g = ( pixel & g_mask ) >> 3
        b = ( pixel & b_mask ) >> 8
        return r,g,b

    @classmethod
    def row_size(cls, width):
        return 2*width

class RGB888:
    value = "bin_888"
    bytes_per_pixel = 3
    @classmethod
    def convert_rgba(cls, r, g, b, a, include_alpha=False):
        return [ b, g, r, a ]

    @classmethod
    def convert_bin(cls, pixel):
        pixel  = struct.unpack(f'>L', b"\0" + pixel)[0]
        r_mask = 0b000000000000000011111111
        g_mask = 0b000000001111111100000000
        b_mask = 0b111111110000000000000000
                   
        r = ( pixel & r_mask )
        g = ( pixel & g_mask ) >> 8
        b = ( pixel & b_mask ) >> 8*2

        return r,g,b

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