# Darklands
Darklands (1992 game from Microprose) file reading utils and preserved file format docs

Based heavily upon work of Merle (wallace.net/darklands) and Joel "Quadko" McIntyre.

Probably not suitable for Windows because of lazy filepaths handling.

[Some outputs and file format docs online](http://wendigo.online-siesta.com/darklands/)


## Dirs
* DL/ - put your Darklands instalation here
* game_patches/ - essential patches to upgrade Darklands to the latest version (.7)

* file_formats/ - gathered docs on DL file formats (corrections included)

* tmp/ - you may direct output there


## Scripts
### Auxilary
* aux_show_fonts.py
* aux_check_pics.py

### Extracting
* extract_cat.py

### Generators
* generate_map_png.py
* generate_map_web.py
* generate_simple_map.py

### Readers
* reader_cty.py
* reader_loc.py
* reader_map.py
* reader_msg.py
* reader_pic.py

### Common libs
* utils.py


## Misc
* dosbox.conf - to ease playing of Darklands

