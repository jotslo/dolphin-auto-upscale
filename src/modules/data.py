upscale_factor = 2

dolphin_path = "~\\Documents\\Dolphin Emulator"
extension_whitelist = ["png"]
name_contains_blacklist = [
    "672x736", "512x512", "352x256",
    "336x368", "256x256", "256x96",
    "176x128", "512x192"
]

upscale_command = '{0}\\waifu2x\\waifu2x.exe -i "{1}" -o "{2}" -n 2 -s {3}'

startup_message = """jotslo/dolphin-auto-upscale

This software automatically upscales any game textures found in a game on Dolphin and retextures the game on-the-fly.

*Please note that your game will run significantly slower when any textures are first encountered*

Upscaled textures are stored permanently in the emulator's files, so the game will run at normal
speed once all textures in a given scene have already been encountered, upscaled and saved.

When you're ready, press the Enter/Return key to begin.

> """

started_message = "Listening for textures..."