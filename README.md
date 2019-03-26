# Roboxum
Roboxum is a free Word Finder puzzle generator, capable of creating custom educational and entertaining puzzles, similar to those seen in the game "Boggle". This software was designed to be used in an educational setting, allowing language teachers to create custom puzzles for their students, aiding in vocabulary review. That being said, there are plenty of other entertaining uses as well. This software is fully open-source and free to use, however I make no guarantees about its continued functionality, or consistent updates.
## Installation Instructions
The easiest way to install Roboxum is to download the appropriate file linked below, corresponding to the Operating System you wish to run the software on:

 - Windows (Ideally Windows 7 or newer):
 	 - [Windows Executable (64-bit)](https://github.com/NoahTroy/Roboxum/releases/download/v1.0.0/Roboxum_v1.0.0_Windows.64-bit.zip)
	 	 - SHA-256 Hash: `238C84CE0627600BA9F0E31B92733C8E7FE8AB96B98F37CB47F6DBE855498F89`
	 - [Windows Executable (32-bit)](https://github.com/NoahTroy/Roboxum/releases/download/v1.0.0/Roboxum_v1.0.0_Windows.32-bit.zip)
	 	 - SHA-256 Hash: `CEC2AA717FAD9E19616901FD4D54A5CF0F7DB3B21D19C1DBE8B06C2600A92C35`
 - MacOS (Mojave 10.14 or higher required):
 	 - [MacOS Application (64-bit)](https://github.com/NoahTroy/Roboxum/releases/download/v1.0.0/Roboxum_v1.0.0_MacOS.64-bit.app.zip)
	 	 - SHA-256 Hash: `A39CD9D028460FFA6319C2A203F74480C795C0911952EBDCA29C52128784A110`
		 - Please note: Some users have reported issues with this release, and it appeaers as though pyinstaller may have had issues compiling parts of the toolkit interface library. If you experience any issues running the software, please use the advanced installation instructions below instead.
> Due the many different Linux distros and flavours, I do not maintain an installer. Instead, because a majority of the most-popular Linux distributions come with Python 3.x already installed, I recommend that Linux users follow the advanced instructions below.
## How to Use
After downloading the ZIP file, decompress it, and then double click on Roboxum.exe. If you wish to add your own custom character sets, open notepad and save a file titled customCharacterSet.txt in the same directory as the Roboxum.exe file. Then, enter the characters you wish to use in the puzzle, into the text file. Make sure you do not include any spaces, new lines, tabs, etc. See the included customCharacterSet.txt file [here](https://github.com/NoahTroy/Roboxum/blob/master/customCharacterSet.txt) for an example as to how to format your file.
### Advanced Installation Instructions
The advanced instructions are for anyone who:

 - Wishes to run the most up-to-date version of the software (although keep in mind that up-to-date does not necessarily mean stable)
 - Wants to edit/experiment with the code
 - Is using an operating system not supported by the simple installers included above
 - Is an aspiring developer
 - Just wants to feel cool
 - Is already a developer, and this is their default. Heck, they probably aren't even reading this right now and have already cloned the repository from their terminal. :P

To run this code:

 1. You must install Python 3.x. For Windows and MacOS users, the easiest way is to go straight to [Python.org](https://www.python.org/downloads/) and download the corresponding installer. People using Linux may do the same, or install Python via the terminal. For example, on Ubuntu, you may use the following command: `sudo apt update && sudo apt install python3 -y` 
 2. You'll need to install Tk ("Toolkit Interface", used for creating the GUI). Detailed instructions can be found here: [TKDocs.com](https://tkdocs.com/tutorial/install.html) On Ubuntu and similar Linux distros, the following command may be used: `sudo apt update && sudo apt install python3-tk`
 3. You must install PyFPDF. You may install it via pip by running `sudo pip3 install fpdf` on Ubuntu and similar Linux distros, or by visiting [their website](https://pyfpdf.readthedocs.io/en/latest/#installation) and following the instructions located there.
 4. Clone the repository. This can be done by clicking on the green "Clone or download" button on the top right of the page, and then downloading the code as a zip file. Or, you may copy the provided URL after clicking on that button, and then use the git command (once again, this example is for Ubuntu): `git clone https://github.com/NoahTroy/Roboxum.git` to clone the repository.
 5. Open your terminal or command prompt (if on Windows), navigate to the directory of the main.py file, then type the following command: `python3 main.py`
 6. Congratulations, you have successfully run the code! Enjoy!
