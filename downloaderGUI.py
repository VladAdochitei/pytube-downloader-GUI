from tkinter import * 
import tkinter as tk
from libraryPath import * 
from pytube import YouTube
import os

# Window initialisation
root = Tk()

# Window configuration
root.title("Youtube Downloader")
root.geometry("500x300")
root.resizable(0,0)
root['bg'] = "grey17"


# GUI elements configuration variables-----------------------------------------
# Labels
labelXvar = 60                  # x axis coordinates (px)
labelYvar = 30                  # y axis coordinates (px)
labelYOffset = 30               # offset (px)

# Entry
entryXvar = 60                 # x axis coordinates (px)
entryYvar = 60                  # y axis coordinates (px)
entryYOffset = 30               # offset (px)
entryWidth = 50

# Buttons
buttonXvar = 30                 # x axis coordinates (px)
buttonYvar = 250                # y axis coordinates (px)
buttonXOffset = 90              # offset (px)
buttonWidth = 6                 # Button Width (px)
buttonBackground = "grey12"
buttonForeground = "grey45"


# Fonts
labelFont = "arial 12 bold"
entryFont = "arial 10"
buttonFont = "arial 10 bold"

# Entry color scheme
entryBackground = "grey12"
entryForeground = "ghost white"

# Label color scheme
labelBackground = "grey17"
labelForeground = "ghost white"
#------------------------------------------------------------------------------



# Application variables--------------------------------------------------------
youtube_link = StringVar()
#------------------------------------------------------------------------------




# Functions

# Testing function that outputs the value of variables
def TestInput():
    print(
    "-------------------TEST-LOG-------------------\n",
    "youtube_link = "+youtube_link.get()+"\n",
    "---------------END-OF-TEST-LOG----------------\n"
    )

# Basic Application Utilities
def Exit():
    root.destroy()

def DownloadYT(link, path):
    youtubeObject = YouTube(link)
    video = youtubeObject.streams.get_highest_resolution()

    download_path = libraryPath(path)

    try:
        video.download(download_path)
    except:
        print("Download failed, check internet connection")
        return 1

    print ("Download completed!")    

def DownloadVideo():
    DownloadYT(youtube_link.get(),"video-library")

# GUI elements 

# User input section

# Vault Path
Label(root, font = labelFont, bg = labelBackground, fg = labelForeground, text = 'Youtube Link:').place(x = labelXvar, y = labelYvar)
Entry(root, font = entryFont, textvariable = youtube_link, bg = entryBackground, width = entryWidth, fg = entryForeground).place(x=entryXvar, y = entryYvar)



# Utility buttons

# Test button
test_button = tk.Button(root, font = buttonFont, text = 'TEST', width = buttonWidth, bg = buttonBackground, fg = buttonForeground, command = TestInput).place(x = buttonXvar, y = buttonYvar)

# Download Button
download_button = tk.Button(root, font = buttonFont, text = 'Download Youtube Video', width = buttonWidth*5, bg = buttonBackground, fg = buttonForeground, command = DownloadVideo).place(x = buttonXvar + buttonXOffset, y = buttonYvar)

# Exit button (TERMINATE)
exit_button = tk.Button(root, font = buttonFont, text = 'EXIT', width = buttonWidth, bg = buttonBackground, fg = buttonForeground, command = Exit).place(x = buttonXvar + buttonXOffset*4, y = buttonYvar)
root.mainloop()