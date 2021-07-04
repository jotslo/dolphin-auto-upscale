# dolphin-auto-upscale
### Introduction
This tool automatically upscales textures in Wii games using waifu2x on-the-fly. It uses Dolphin's "Dump Textures" feature to access any games' textures when they are encountered in game, and sends them through to the waifu2x upscaling tool to scale each image by 2, before placing them in the Load/Textures folder for Dolphin to run each time

When used alongside upscaled 3D models in Dolphin, this tool can make any Wii game look significantly nicer than what you would find in its original 480p form.

### How to use
When you want to start upscaling a game's textures, head to the Graphics -> Advanced in the Dolphin GUI, and tick "Dump Textures" and "Load Custom Textures". If your PC has a lot of RAM available, you can also tick "Prefetch Custom Textures" to reduce stuttering.

Next, double-check the `data.py` file in the `modules` directory to make sure that everything is configured as you want it to be.

From there, simply run the `main.py` file, hit ENTER, and then start playing a game on Dolphin. Each time a texture is dumped, the software will automatically run it through waifu2x and place it in the Load/Textures directory, which will be automatically loaded by Dolphin the next time you start the game.

Once you've finished playing the game, simply return to the Graphics -> Advanced, and disable "Dump Textures" until you next want to run the software.

#### Notes
- Python 3 must be installed, in addition to the `watchdog` library (available via PIP)
- Your game will run significantly slower when any textures are first encountered, this is normal.
- If you do not encounter a certain texture in your play session, that texture will **not** be upscaled. 
- The software may still be upscaling textures when you have finished your play session, make sure it has finished before closing the program.

### Example Screenshots
![wiimote_example](assets/wiimote_example.png)
![gameplay_example](assets/gameplay_example.png)
