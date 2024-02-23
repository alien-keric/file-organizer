'''
    Author: alienX and Jehoshaphat Obol
    Date: 23/02/2024
    Description: This is a simple file organizer. It organizes the files
        in a given directory in to categories like Documents, Videos,
        Pictures etc.
    Usage: python organize.py
    
    Permissions: Feels free to share modify and redistribute the code to
        your liking.
'''

import subprocess

# A Dictionary of file categories
file_categories = {
    "Documents": [".txt", ".pdf", ".doc", ".docx", ".odt", ".rtf"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"],
    "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Applications": [".exe", ".app", ".deb", ".rpm", ".msi"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Audio": [".mp3", ".wav", ".flac", ".ogg", ".aac"],
    "Torrents": [".torrent"]
}

# Get a list of files in the current directory
files = subprocess.run(capture_output=True, args=["ls"])
files = files.stdout.splitlines()

# convert the byte string into a normal string
files = [x.decode("utf-8") for x in files]

# categorize the files
for file in files:
    # get the file extension
    extenstion = f".{file.split('.')[-1]}".lower()
    
    # don't move this file
    if file == "organize.py":
        continue

    # determine file category, create a file category folder if one does not exist
    # move the file to the new directory
    if extenstion in file_categories["Documents"]:
        subprocess.run(args=["mkdir", "-p", "Documents"])
        subprocess.run(args=["mv", f"./{file}", "./Documents/"])
    if extenstion in file_categories["Videos"]:
        subprocess.run(args=["mkdir", "-p", "Videos"])
        subprocess.run(args=["mv", f"./{file}", "./Videos/"])
    if extenstion in file_categories["Pictures"]:
        subprocess.run(args=["mkdir", "-p", "Pictures"])
        subprocess.run(args=["mv", f"./{file}", "./Pictures/"])
    if extenstion in file_categories["Applications"]:
        subprocess.run(args=["mkdir", "-p", "Applications"])
        subprocess.run(args=[f"mv", f"./{file}", "./Applications/"])
    if extenstion in file_categories["Archives"]:
        subprocess.run(args=["mkdir", "-p", "Archives"])
        subprocess.run(args=["mv", f"./{file}", "./Archives/"])
    if extenstion in file_categories["Audio"]:
        subprocess.run(args=["mkdir", "-p", "Audio"])
        subprocess.run(args=["mv", f"./{file}", "./Archives/"])
    if extenstion in file_categories["Torrents"]:
        subprocess.run(args=["mkdir", "-p", "Torrents"])
        subprocess.run(args=["mv", f"./{file}", "./Torrents/"])
