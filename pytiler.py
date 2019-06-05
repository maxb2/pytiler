#!/usr/bin/python

from PIL import Image
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("tiles", metavar='dims', nargs=2, type=int, help="number of tiles in each direction")
# parser.add_argument("xtiles", type=int, help="number of tiles in the x direction")
# parser.add_argument("ytiles", type=int, help="number of tiles in the y direction")
parser.add_argument("f_in", metavar='files', type=str, nargs='+', help="input images to be tiled")
parser.add_argument("-o", "--out", type=str, help="output image", default="out.png")
args = parser.parse_args()

xtiles, ytiles = args.tiles
files_in = args.f_in[0]

print(args)
print(xtiles,ytiles,files_in)

img = Image.open(files_in, 'r')
img_w, img_h = img.size
tile_w=img_w//3
tile_h=img_h//3
background = Image.new('RGBA', (xtiles*tile_w+(img_w-tile_w), (ytiles*tile_h+(img_h-tile_h))), (0, 0, 0, 0))
bg_w, bg_h = background.size
#offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
#background.paste(img, offset)
#background.save('out.png')

comp=background
for i in range(xtiles):
    xoffset=i*tile_w
    for j in range(ytiles):
        yoffset=j*tile_h
        new=Image.new('RGBA', (xtiles*tile_w+(img_w-tile_w), (ytiles*tile_h+(img_h-tile_h))), (0, 0, 0, 0))
        new.paste(img.rotate(((i+1)*(j+1)-1)*90), (xoffset,yoffset))
        comp=Image.alpha_composite(comp,new)
comp.save(args.out)
