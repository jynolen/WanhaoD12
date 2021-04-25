import numpy
from PIL import Image

for n in range(5):
    a = numpy.random.rand(25,25,3) * 255
    im_out = Image.fromarray(a.astype('uint8')).convert('RGB')
    im_out.save('random_%s_%000d.%s' % (type, n, "bmp"))

for n in range(25):
    a = numpy.random.rand(25,25,4) * 255
    im_out = Image.fromarray(a.astype('uint8')).convert('RGBA')
    im_out.save('random_%s_%000d.%s' % (type, n, type))