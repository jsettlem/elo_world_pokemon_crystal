# Running Battles Locally

Battles are seeded by unique identifiers--if you have an ID from the video, you can pass that ID into a script in this repo to run that battle yourself locally. While this code is better organized than the code for the gen 1 tournaments, I have not gone through the trouble of making it easy to run like I did for gen 1. Godspeed.

If you need more help, try the [more detailed instructions for the Gen 1 project](https://github.com/jsettlem/elo_world_pokemon_red/blob/master/tutorial.md). They're mostly still relevant.

I have not tested these instructions like I did for the gen 1 project, so please let raise an issue if you find an error. 

## Dependencies

The dependencies are pretty much the same as for the gen 1 tournament, except you'll need Python 3.10 instead of 3.8. Also, BGB is packaged with this repo now, so you won't need to download it separately. You'll need:

* This repo. [Download the zip](https://github.com/jsettlem/elo_world_pokemon_crystal/archive/refs/heads/master.zip) or clone it
* Windows 10 or 11 (or Wine--if you're using wine, set `USE_WINE` to `True` in [./utils/bgb.py](./utils/bgb.py). I've not tested using Wine with video output, you might need to make more changes for that)
* Python 3.10
* The requirements from `requirements.txt`. Run `pip install -r requirements.txt`, and let me know if I missed anything. 
* ffmpeg, which must be on your path
* [The CamStudio lossless codec](https://www.free-codecs.com/download_soft.php?d=a05ef709ad3c01e27214a4e83297821f&s=551&r=&f=camstudio_lossless_codec.htm)
* `pokecrystal11.gbc`, the same file the disassembly project outputs (md5 `301899B8087289A6436B0A241FBBB474`. This must match exactly (probably) and the script will not check). This should go in the `static_files` folder.  


## Configure output and scratch directories

By default, the project will use `./output` and `./scratch` for output and scratch directories. You might want to change these in [constants/file_paths.py](./constants/file_paths.py).

## Run battles

[battle_x_as_crystal.py](./battle_x_as_crystal.py) contains methods for running battles. If you want to run a battle from an ID, modify the line at the end of that file to use the appropriate ID, then run that script.
