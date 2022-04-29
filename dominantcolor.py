#dominantcolor.py 
from colorthief import ColorThief
def returnDominantColor(path,quality=1):
    from colorthief import ColorThief
    color_thief = ColorThief(path)
    # get the dominant color
    return color_thief.get_color(quality=quality)
