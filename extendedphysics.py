# Set title for filedialog and add instructions
# Finish def restore(), Maybe use restore(Variable)

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
    acpath = filedialog.askdirectory()
    if acpath:
      with open("acpath.txt", "w") as f:
        f.write(acpath)
  # Open filedialog in AC directory and ask for track path
  directory = filedialog.askdirectory(initialdir=acpath)

os.chdir(directory)

restorecount = 0
backupcount = 0
nobackup = 0
errorcount = 0

def rename():
  if os.path.isfile("surfaces - Kopie.ini")
  os.rename("surfaces - Kopie.ini", "surfaces-backup.ini")

def restore():
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
        if not os.path.isfile("surfaces-backup.ini"):
          try:
            shutil.copy(directory

if os.path.isdir("data"):
    os.chdir(directory + "\data")
# If only one layout for track (Dir "\data" in top folder)
    if os.path.isfile("surfaces.ini"):
        with open("surfaces.ini", "r") as f:
            if "extended" in f.read():
              rename()
                if os.path.isfile("surfaces - Kopie.ini"):
                    with open("surfaces - Kopie.ini", "r") as f2:
                        contents = f2.read()
                    with open("surfaces.ini", "w") as f3:
                        f3.write(contents)
                    print("Success\n\n" + "'surfaces.ini' has been restored!")

                else:
                    print("Failure\n\n" + "No backup was found.")
            else:
                if not os.path.isfile("surfaces - Kopie.ini"):
                    try:
                        shutil.copy(directory + "/data/surfaces.ini", directory + "/data/surfaces - Kopie.ini")
                        print("Success\n\n" + "A backup of 'surfaces.ini' has been created")
                    except:
                        print("Failure\n\n" + "An error occured while backing up 'surfaces.ini'")
    else:
        print("Failure\n\n" + "No file named 'surfaces.ini' was not found.")

else:
  # Else restore for all layouts

    for root, dirs, files in os.walk(directory):
        if "surfaces.ini" in files:
            os.chdir(root)
            with open("surfaces.ini", "r") as f:
                if "extended" in f.read():
                    if os.path.isfile("surfaces - Kopie.ini"):
                        with open("surfaces - Kopie.ini", "r") as f2:
                            contents = f2.read()
                        with open("surfaces.ini", "w") as f3:
                            f3.write(contents)
                        restorecount += 1
                    else:
                        nobackup += 1
                else:
                    if not os.path.isfile("surfaces - Kopie.ini"):
                        try:
                            shutil.copy(root + "/surfaces.ini", root + "/surfaces - Kopie.ini")
                            backupcount += 1
                        except:
                            errorcount += 1
        os.chdir(directory)
    print("Finished\n\n" + str(restorecount) + " files were restored.\n" + str(backupcount) + " files were backed up.\n" + str(nobackup) + " files had no backup.\n" + str(errorcount) + " errors occured.")
time.sleep(2)
exit(0)
