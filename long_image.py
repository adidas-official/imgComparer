import os

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

pwd = Path(r'C:\Users\bluem\Documents\Prace\Ondra\combo_resize')
img_size = (1392, 928)
font = ImageFont.truetype(r'C:\Windows\fonts\CALIBRIB.TTF', 50)

if not Path(pwd / 'long').exists():
    Path(pwd / 'long').mkdir()

for d, s, f in os.walk(pwd):
    if d.endswith('combo_resize') or d.endswith('long'):
        continue
    images = [Image.open(Path(pwd) / d / x) for x in f]

    total_width = img_size[0] * 3
    total_height = img_size[1] * 2

    new_im = Image.new('RGB', (total_width, total_height))

    x_offset = 0
    y_offset = 0

    for fname, im in zip(f, images):
        # print(fname)
        new_im.paste(im, (x_offset, y_offset))
        text_obj = ImageDraw.Draw(new_im)
        text_obj.text((x_offset + 30, y_offset + 30), fname, fill=(255, 0, 0), font=font)
        x_offset += im.size[0]
        if x_offset == 3 * im.size[0]:
            y_offset = im.size[1]
            x_offset = 0

    print(pwd / 'long' / f'{Path(d).name}-merged.jpg')
    new_im.save(pwd / 'long' / f'{Path(d).name}-merged.jpg')
