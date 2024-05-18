# Move-Up
This is a context menu tool to elevate the contents of a folder by one level.

For example, if your directory structure in a folder is:
```none
C:/
├── Target/
│   ├── stuff.txt
│   └── extra-stuff/
├── notes.txt
```
After using move up on the target folder, it would become:
```none
C:/
├── stuff.txt
├── extra-stuff/
└── notes.txt
```


# Installation
You can either:
```cmd
python setup.py
```
Or you can double click the .reg file. The reg file's default location is on C:/Users/User, so you'll need to adjust it accordingly. You might also need to adjust the location for your python.exe (but the setup.py will handle this and clean up the files after registering as you no longer need them afterwards)


# Usage
Just right click on a folder and it should show up as an option once installed
![Usage example](https://i.imgur.com/G4xYxDo.png)

<hr>

![Icon](icon.ico)