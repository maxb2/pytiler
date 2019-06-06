#!/usr/bin/python

from PIL import Image
from random import randint, choice
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("tiles", metavar='dims', nargs=2, type=int, help="number of tiles in each direction")
parser.add_argument("f_in", metavar='files', type=str, nargs='+', help="input images to be tiled, randomly selected")
parser.add_argument("-o", "--out", type=str, help="output image", default="out.png")
parser.add_argument("-t", "--tile-divs", type=int, help="tile subdivisions, usually to take care of alpha borders", default=1)
parser.add_argument("-r", "--rotate", help="randomly rotate the tiles", action="store_true")
args = parser.parse_args()

xtiles, ytiles = args.tiles
files_in = args.f_in

imgs = [Image.open(f, 'r') for f in files_in ]
img_w, img_h = imgs[0].size
tile_w=img_w//args.tile_divs
tile_h=img_h//args.tile_divs
comp = Image.new('RGBA', (xtiles*tile_w+(img_w-tile_w), (ytiles*tile_h+(img_h-tile_h))), (0, 0, 0, 0))

for i in range(xtiles):
    xoffset=i*tile_w
    for j in range(ytiles):
        yoffset=j*tile_h
        new=Image.new('RGBA', (xtiles*tile_w+(img_w-tile_w), (ytiles*tile_h+(img_h-tile_h))), (0, 0, 0, 0))
        img = choice(imgs)
        if args.rotate:
            img = img.rotate(randint(0,3)*90)
        new.paste(img, (xoffset,yoffset))
        comp = Image.alpha_composite(comp,new)
comp.save(args.out)
