import os
import zipfile
from colorama import Fore, Style
from rich import print
import pyfiglet
import time
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
title = pyfiglet.figlet_format('SP-RENAMER', font='puffy', justify="center")
print(f'[bold magenta]{title}[/bold magenta]')
print(f'[green]Created by [/green][bold cyan]Rednotsus[/bold cyan]')
print("      ")
print("       ")
start_time = time.time()
def detectMusic(folder_path):
    songs = 0
    try:
        file_list = os.listdir(folder_path)
        print(f"[yellow][ DETECTOR ]  |  Scanning files in dir")
        time.sleep(1)
        for filename in file_list:
            if filename.endswith(".mp3"):
                print(f"[green][ & FILE DETECTED & ]  |   {filename}")
                time.sleep(0.025)
                songs += 1
    except Exception as e:
        print(f"[bold red][ ERROR ]  |  An error occurred: {e}")
    return songs 
def process_music_folder(folder_path):
    try:
        for filename in os.listdir(folder_path):
            if filename.endswith(".mp3") and "[SPOTDOWNLOADER.COM] " in filename:
                new_filename = filename.replace("[SPOTDOWNLOADER.COM] ", "").strip()
                old_path = os.path.join(folder_path, filename)
                new_path = os.path.join(folder_path, new_filename)
                os.rename(old_path, new_path)
                print(f"[bold blue][ * DIRECTORY *]  |  Renamed file: {filename}")
                time.sleep(0.025)

    except Exception as e:
        print(f"[bold red][ ERROR ]  |  An error occurred: {e}")
def rename_dir(folder_path):
    try:
        if "[SPOTDOWNLOADER.COM] " in music_folder:
            new_folder_name = music_folder.replace("[SPOTDOWNLOADER.COM] ", "").strip()
            old_path = folder_path
            new_path = os.path.join(os.path.dirname(folder_path), new_folder_name)
            os.rename(old_path, new_path)
            print("      ")
            print(f"[bold blue][ * DIRECTORY *]  |  Renamed folder: {new_folder_name}")
            print("      ")
            time.sleep(0.025)
            
    except Exception as e:
        print(f"[bold red][ ERROR ]  |  An error occurred: {e}")
def extract_zip(zip_path, extract_folder):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_folder)

def detect_zip_file(folder_path):
    potential_zip_files = [zip_file for zip_file in os.listdir(folder_path) if zip_file.endswith(".zip")]
    if not potential_zip_files:
        print(f'[bold red][Error]  |  No zip file found in the folder.')
        exit()
    return os.path.join(folder_path, potential_zip_files[0])
if __name__ == "__main__":
    zip_file_path = detect_zip_file(os.getcwd())
    extract_folder = os.path.splitext(zip_file_path)[0]
    os.makedirs(extract_folder, exist_ok=True)
    extract_zip(zip_file_path, extract_folder)
    potential_music_folders = [folder for folder in os.listdir() if os.path.isdir(folder) and "[SPOTDOWNLOADER.COM]" in folder]
    music_folders_with_prefix = [folder for folder in potential_music_folders if "[SPOTDOWNLOADER.COM]" in folder]
    if not music_folders_with_prefix:
        print(f'[bold red][Error]  |  No folder with the prefix "[SPOT-DOWNLOADER.COM]" found in the extracted folder.')
        exit()
    music_folder = extract_folder
    print(f"[blue][ INFO ]  |  Zip found: [/blue][yellow]{music_folder}")
    time.sleep(1)
    songs = detectMusic(music_folder)
    print("      ")
    print(f"[yellow][ RENAMER ]  Detected ( {songs} ) songs |  Attempting to rename.")
    print("      ")
    time.sleep(1)
    process_music_folder(music_folder)
    rename_dir(music_folder)
    print(f"[green][ RENAMER ]  |  Attempting to delete the original zip file")
    os.remove(zip_file_path)
    time.sleep(0.5)
    print("      ")
    print(f"[green][ RENAMER ]  |  Deleted the original zip file: {zip_file_path}")
    elapsed_time = round(float(time.time() - start_time), 2)
    print(f"[green][ RENAMER ]  |  Done, Completed in {elapsed_time} seconds")
    print(f"[green][ RENAMER ]  |  Press enter to quit...")
    input(f"    >    ")
    if input == " ":
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        time.sleep(0.5)
        exit()
