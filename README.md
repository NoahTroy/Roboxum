> *Please Note: This project is ***still under very early development***. Therefore, functional code is still missing, many of the links below are simply dummy links, and the included information and hash sums are very apt to change by the time we put-out our first stable release.*

![Roboxum Logo](https://raw.githubusercontent.com/NoahTroy/Roboxum/master/Roboxum%20Logo%20200x200.gif)
# Roboxum
Roboxum is a free Word Finder puzzle generator, capable of creating custom educational and entertaining puzzles, similar to those seen in the game "Boggle". This software was designed to be used in a classroom setting, allowing language teachers to create custom puzzles for their students, to aid in vocabulary review. That being said, I'm sure there are plenty of other entertaining uses as well. This software is fully open-source and free to use, however I make no guarantees about its continued functionality, or about consistently updating the executable files for each operating system.
## Installation Instructions
The easiest way to install Roboxum is to download the appropriate file linked below, corresponding to the Operating System you wish to run the software on:

 - Windows (Ideally Windows 7 64-bit or newer): [Windows Installer](https://github.com/NoahTroy/Roboxum)
	 - SHA-512 Hash: `C6B0919C7FE628AE9056992C4A917E5DC035A9615D497F6EB2BD14063EAAD3E6508EFC8682FEC82823CA3F3DE311868A72990946166429F01B38F9F33D9CA610`
 - MacOS (Mojave 10.14 or higher required): [MacOS Installer](https://github.com/NoahTroy/Roboxum)
	 - SHA-512 Hash: `C6B0919C7FE628AE9056992C4A917E5DC035A9615D497F6EB2BD14063EAAD3E6508EFC8682FEC82823CA3F3DE311868A72990946166429F01B38F9F33D9CA610`
> Due the many different Linux distros and flavours, I do not maintain an installer. Instead, because a majority of the most-popular Linux distributions come with Python 3.x already installed, I recommend that Linux users follow the advanced instructions below.

### Advanced Installation Instructions
The advanced instructions are for anyone who:

 - Wishes to run the most up-to-date version of the software (although keep in mind that up-to-date does not necessarily mean stable)
 - Wants to edit/experiment with the code
 - Is using an operating system not supported by the simple installers included above
 - Is an aspiring developer
 - Just wants to feel cool
 - Is already a developer, and this their default. Heck, they probably aren't even reading this right now and have already cloned the repository from their terminal. :P

To run this code:

 1. You must install Python 3.x. For Windows and MacOS users, the easiest way is to go straight to [Python.org](https://www.python.org/downloads/) and download the corresponding installer. People using Linux may do the same, or install Python via the terminal. For example, on Ubuntu, you may use the following command: `sudo apt update && sudo apt install python3 -y` 
 2. You'll need to install Tk ("Toolkit Interface", used for creating the GUI). Detailed instructions can be found here: [TKDocs.com](https://tkdocs.com/tutorial/install.html) On Ubuntu and similar Linux distros, the following command may be used: `sudo apt update && sudo apt install python3-tk`
 3. Clone the repository. This can be done by clicking on the green "Clone or download" on the top right of the page, and then downloading the code as a zip file. Or, you may copy the URL, and then use the git command (once again, this example is for Ubuntu): `git clone https://github.com/NoahTroy/Roboxum.git`
 4. Open your terminal or command prompt (if on windows), navigate to the directory of the main.py file, then type the following command: `python3 main.py`
 5. Congratulations, you have successfully run the code! Enjoy!
