import os
import sys
import tkinter as tk
from tkinter import filedialog
import shutil
import time

root = tk.Tk()
root.withdraw()

# Set operating directory
if len(sys.argv) > 1:
  # Use CM Argument if given
    directory= sys.argv[1]
else:
  os.chdir()
  if os.path.isfile("acpath.txt"):
    # Use saved initial path if possible
    with open("acpath.txt", "r") as f:
      if len(f.read()) >= 1:
        acpath = f.read().strip()
  else:
    # Ask for AC directory
    acpath = filedialog.askdirectory(title = "Select Assetto Corsa directory (steamapps/common/assettocorsa)")
    if acpath:
      with open("acpath.txt", "w") as f:
        f.write(acpath)
  # Open filedialog in AC directory and ask for track path
  directory = filedialog.askdirectory(initialdir=acpath, title = "Select AC track folder (assettocorsa/content/tracks/Name of the Track)")

os.chdir(directory)

layoutcount = 0
restorecount = 0
backupcount = 0
nobackup = 0
errorcount = 0

def rename():
  if os.path.isfile("surfaces - Kopie.ini"):
    os.rename("surfaces - Kopie.ini", "surfaces-backup.ini")

def restore(workdir):
  if os.path.isfile("surfaces.ini"):
    with open("surfaces.ini", "r") as f:
      if "extended" in f.read():
        if os.path.isfile("surfaces-backup.ini"):
          with open("surfaces-backup.ini") as f2:
            contents = f2.read()
          with open("surfaces.ini") as f3:
            f3.write(contents)
          restorecount += 1
        else:
          nobackup += 1
      else:
        if not os.path.isfile("surfaces-backup.ini"):
          try:
            shutil.copy(workdir + "/data/surfaces.ini", workdir + "/data/surfaces-backup.ini")
            backupcount += 1
          except:
            errorcount += 1


# If only one layout
if os.path.isdir("data"):
  os.chdir(directory + "/data")
  restore(directory + "/data")
  layoutcount += 1

# If multiple layouts
else:
  for root, dirs, files in os.walk(directory):
    if "surfaces.ini" in files:
      os.chdir(root)
      restore(root)
      layoutcount += 1
    os.chdir(directory)

# Show results and exit after 2s
print("Finished\n\n" + str(layoutcount) + " layouts were found.\n" + str(restorecount) + " files were restored.\n" + str(backupcount) + " files were backed up.\n" + str(nobackup) + " files had no backup.\n" + str(errorcount) + " errors occured.")
time.sleep(2)
exit(0)