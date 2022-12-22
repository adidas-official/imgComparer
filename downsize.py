from os import walk, chdir
from pathlib import Path
from PIL import Image

pwd = Path(r'C:\Users\bluem\Documents\Prace\Ondra\ALL_PHOTOS')
chdir(pwd)
combo = pwd.parent / 'combo_resize'
downscale_factor = 4

if not combo.exists():
    combo.mkdir()

size = (int(5568 / downscale_factor), int(3712 / downscale_factor))

for folders, subfolders, files in walk(pwd):
    for file in files:
        img = Path(folders) / Path(file)
        if not Path(combo / Path(folders).name).exists():
            Path(combo / Path(folders).name).mkdir()
        # print(img)  # C:\Users\bluem\Documents\Prace\Ondra\ALL_PHOTOS\DSC_1276\auto_br-con.jpg
        new_name = Path(combo) / Path(folders).name / img.name
        print(new_name)
        image = Image.open(img)
        new_image = image.resize(size)
        # image.resize(size)
        new_image.save(new_name)
