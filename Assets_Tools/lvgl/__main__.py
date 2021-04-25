import argparse
from lvgl.lvgl_enum import OuputFormat, ColorFormat
from lvgl.algo import SmartConverter
from pathlib import Path
class CreateOutputFormat(argparse.Action):
    choices = [ f.value.value for f in list(OuputFormat) ]
    
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super(CreateOutputFormat, self).__init__(option_strings, dest, **kwargs)
    
    def __call__(self, parser, namespace, values, option_string=None):
        val = [f.value for f in list(OuputFormat) if f.value.value == values][0]
        setattr(namespace, self.dest, val)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog=__file__)
    parser.add_argument('--dithering', action='store_true')
    parser.add_argument('--output_c', action='store_true')
    parser.add_argument('--output_format', action=CreateOutputFormat, choices=CreateOutputFormat.choices)
    parser.add_argument('--color_format', type=ColorFormat, choices=ColorFormat, default=ColorFormat.True_Color)
    parser.add_argument('file', type=Path)
    smart = SmartConverter(parser.parse_args())
    smart.perform()
