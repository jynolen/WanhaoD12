from lvgl.converter import Converter
from pathlib import Path

class SmartConverter:
    def __init__(self, args):
        self.output_c = args.output_c
        self.converter = Converter.instanciate(args.color_format)(vars(args))


    def perform(self):
        self.converter.convert()
        output_name_file = Path(self.converter.file).name.split(".")[:-1][0]
        if self.output_c:
            with open(f"{output_name_file}.c", "w") as fp:
                fp.write(self.converter.export_to_c_array())
        with open(f"{output_name_file}.bin", "wb") as fp:
            fp.write(self.converter.export_to_bin())