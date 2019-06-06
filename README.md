# pytiler

A python tool to create a bigger image out of image tiles. pytiler is especially useful for building RPG maps from tilesets using conventional photo editing software such as [Photoshop](https://www.adobe.com/products/photoshop.html) or [GIMP](https://www.gimp.org/).

### Usage

The simplest way to make a 4x2 image with a single tile is:
`python pytiler.py 4 2 tile.png`

pytiler can also select from a group of tiles and even randomly rotate them for a more natural look. See the usage for more details.

```
$python pytiler.py -h
usage: pytiler.py [-h] [-o OUT] [-t TILE_DIVS] [-r]
                  dims dims files [files ...]

positional arguments:
  dims                  number of tiles in each direction
  files                 input images to be tiled, randomly selected

optional arguments:
  -h, --help            show this help message and exit
  -o OUT, --out OUT     output image
  -t TILE_DIVS, --tile-divs TILE_DIVS
                        tile subdivisions, usually to take care of alpha
                        borders
  -r, --rotate          randomly rotate the tiles
```

#### Tile subdivisions
Some tilesets come with an alpha border, see [2-Minute Tabletop Dungeon Room Builder](https://2minutetabletop.com/gallery/dungeon-room-builder/). pytiler handles these with the `-t, --tile-divs` option. For example, if you have a tile image that has an alpha border the same width as the width of the image, you would use `-t 3` since the actual image is 1/3 of the total image length.
