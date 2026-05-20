# File Organizer Script:
A local Python automation script designed to instantly clean up messy folders by sorting loose files into dedicated categories. Project #4 in my coding journey.

## Overview:
-As my fourth project—and my very first one using Python—this script was born out of a desire to automate annoying digital chores. While my previous projects (like the Study Hub) focused on web development, basic layouts, and front-end JavaScript, this application dives into backend scripting and interacting with my computer's file system. My primary goal was to make a quick, script-based solution that clears up folder clutter with just a single input.

## How to Use It

Since this script runs locally on your computer, follow these simple steps to organize your folders:

### Step 1: Copy the Folder Path
1. Open your computer's file explorer and find the messy folder you want to clean up (for example, your **Downloads** folder).
2. **On Windows:** Click the address bar at the top of the window and copy the path (it will look like `C:\Users\Name\Downloads`).
3. **On Mac:** Right-click the folder, hold down the `Option` key, and select **"Copy 'Folder Name' as Pathname"**.

### Step 2: Run the Script
1. Open your terminal or VS Code PowerShell.
2. Run the script by typing:
   ```bash
   python main.py
   ```

### Step 3: Paste and Organize
1. The terminal will prompt you with a message: `Enter the folder path: `
2. Paste your copied folder path into the terminal and press **Enter**.
3. Watch the terminal logs display the files being sorted instantly!


## Features:
-File Extension Sorting: Automatically scans files and groups them into designated folders (Images, Documents, Videos, Audio) based on their extensions.

-Automatic Folder Creation: Checks if the target folders exist; if they don't, the script generates them on the fly before moving files.

-Safety Check: Skips existing folders completely so it only organizes loose files and doesn't mess up your pre-existing folder structures.

-Terminal Logs: Prints a live update message in the terminal for every single file moved, so you know exactly what changed.

## What I Learned:
-Python File Modules: Learning how to use `os` and `shutil` to safely scan files and move them around on my computer.

-Case Formatting: Using `.lower()` on file extensions so uppercase file types (like `.JPG` or `.PNG`) don't break the code logic.

-Dictionary Syntax & Commas: Fixing syntax errors and learning how strict Python dictionaries are with commas when organizing lists of extensions.

-Terminal Inputs: Using the `input()` function to let users paste their folder path right into the VS Code PowerShell terminal.

-GitHub for Scripts: Realizing that Python scripts can't be hosted on GitHub Pages like websites, but are instead shared as source code repositories.

## Status: 
-Completed

## Author: 
-Aishah Mgaram
