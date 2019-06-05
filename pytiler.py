#!/usr/bin/python

from PIL import Image


xtiles=4
ytiles=

img = Image.open('test.png', 'r')
img_w, img_h = img.size
tile_w=img_w//3
background = Image.new('RGBA', (xtiles*tile_w+(img_w-tile_w), img_h), (0, 0, 0, 0))
bg_w, bg_h = background.size
#offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
#background.paste(img, offset)
#background.save('out.png')

comp=background
for i in range(xtiles):
    xoffset=i*tile_w
    new=Image.new('RGBA', (xtiles*tile_w+(img_w-tile_w), img_h), (0, 0, 0, 0))
    new.paste(img.rotate(i*90), (xoffset,0))
    comp=Image.alpha_composite(comp,new)
comp.save('out.png')
