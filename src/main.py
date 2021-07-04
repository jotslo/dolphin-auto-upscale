from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from os import system, path, makedirs
from modules import data
from time import sleep

load_path = path.expanduser(f"{data.dolphin_path}\\Load\\Textures")
dump_path = path.expanduser(f"{data.dolphin_path}\\Dump\\Textures")
script_path = "\\".join(__file__.split("\\")[:-1])

input(data.startup_message)
system("cls")
print(data.started_message)

class MonitorFolder(FileSystemEventHandler):
    def get_load_path(self, file_path):
        game_title = file_path.split("\\")[-2]
        file_name = file_path.split("\\")[-1]
        new_directory = f"{load_path}\\{game_title}"
        new_file_path = f"{new_directory}\\{file_name}"

        try:
            makedirs(new_directory)
        except FileExistsError:
            pass

        return new_file_path

    def on_created(self, event):
        file_path = event.src_path
        whitelisted = file_path.split(".")[-1] in data.extension_whitelist
        blacklisted = any(name in file_path.split("\\")[-1]
            for name in data.name_contains_blacklist)
        
        if whitelisted and not blacklisted:
            new_file_path = self.get_load_path(file_path)
            system(data.upscale_command.format(
                script_path, file_path, new_file_path, data.upscale_factor))


observer = Observer()
observer.schedule(MonitorFolder(), dump_path, recursive=True)
observer.start()

try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()