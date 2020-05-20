# NotesCLI
Command line tool which helps to organize the Notes
## Prerequisites:
   * Python 3.x
   * pyinstaller( if not installed run  `pip install PyInstaller`)
   
## Installation:
   * Clone the repository
   * In cmd navigate to the directory you have cloned this repo
   * Run the following command `pyinstaller.exe --onefile Notes.py`
   * New folder named dist will be created which contains the executable file
   * In environment variables set path variable to location of Notes.exe in dist folder
    
 ## Guide:
   * `Notes --config dir_name` , specify the name of directory where you want to keep all the notes
   * `Notes -ls 1` will list all the files and dirs in a current working directory
   * `Notes -nf file_name.extension` will create a file
   * `Notes -rf file_name.extension` will open appropriate app to make content visible and editable.
   * `Notes -cd dir_name` will change the directory
   * `Notes -rd 1` Resets the directory.
   * `Notes -nd dir_name` creates the directory
