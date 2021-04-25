import decimal


def palette_to_rgb(palette_color_summary, rgb_color_summmary):
    """
        palette_color_summary : number of pixel per index
        rgb_color_summmary : number of pixel per rgb
        output : rgb per index
    """
    index_pixel_count = [None] * len(palette_color_summary)
    palette_rgb = [None] * len(palette_color_summary)
    for i in range(0,len(palette_color_summary)):
        index_pixel_count[i] = [pl_color[0] for pl_color in palette_color_summary if pl_color[1] == i][0]

    for i in range(0,len(palette_color_summary)):
        palette_rgb[i] = [rgb_color[1] for rgb_color in rgb_color_summmary if rgb_color[0] == index_pixel_count[i]][0]

    return palette_rgb

def convert_to_alpha(value):
    ret = (value & 0xff000000) >> 23
    if ret & 0x02:
        ret |= 0x01
    return 255 - ret



def consume(iterator, n):
    ret = []
    for _ in range(0, int(n)):
        try:
            ret.append(next(iterator))
        except StopIteration as e:
            if ret:
                return ret
            raise StopIteration from e
    return ret