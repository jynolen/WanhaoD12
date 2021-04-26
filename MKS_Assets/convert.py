"""
    Convert Back RGB565 back to png to identify what to change
"""
import struct
import png

class Kobo565:
    def __init__(self, img):
        self.img = img
        header = self.img.read(4)
        header = struct.unpack('<L', header)[0]
        self.height = header >> 21
        self.width = (header & 0xFFFFF) >> 10

    def make_array(self):
        """Convert RAW file *fil* to a 2D array."""
        #header = 4 + (89 << 10) + ( 97 << 21)
        #header = struct.pack("<L", header)
        for i in range(self.height):
          row = []
          s = self.img.read(self.width*2)
          pixels = struct.unpack(f'<{self.width}H', s)
          for p in pixels:
            r = p >> 11
            g = (p >> 5) & 0x3f
            b = p & 0x1f
            r = (r * 255) / 31.0
            g = (g * 255) / 63.0
            b = (b * 255) / 31.0
            row.extend([int(round(x)) for x in [r, g, b]])
          yield row

def main():
    import sys
    outname = None
    arg = sys.argv[1:]
    while arg:
        if arg[0] == '-o':
            outname = arg[1]
            arg = arg[2:]
        elif arg[0] == '--':
            arg = arg[1:]
            break
        elif arg[0].startswith('-'):
            raise Exception("Unknown option %r" % arg[0])
        else:
            try:
                img = open(arg[0], "rb")
            except:
                img = sys.stdin
            break
    kobo = Kobo565(img)
    array = kobo.make_array()
    image = png.from_array(array, 'RGB', info=dict(height=kobo.height))

    if outname is None:
        image.save(sys.stdout)
    else:
        image.save(outname)

if __name__ == '__main__':
    try:
        main()
    except:
        pass
