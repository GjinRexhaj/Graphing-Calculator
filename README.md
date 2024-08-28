# Graphing-Calculator

## General Information/Usage
A graphing calculator written in Python capable of plotting user-specifiable arbitrary mathematical functions. Currently implemented with PySide6 and matplotlib.

This program was built using pyinstaller. Therefore, you do not need to have python installed to run this program.

## Development Requirements
Prerequisites:
- Python (latest version is ideal) 
- This project's required libraries

All of the neccessary libraries can be found in root/requirements.txt.

To install these libraries, ensure you've properly added python to path, or have a virtual environment activated (if applicable) and type the following command into your OS's respective CLI (Windows: Command prompt, Linux: Terminal, etc.):
```
pip install -r requirements.txt
```

**Please note:** If you're planning on altering the GUI in any way, It is strongly recommended you use QtDesigner as that's what this project was built around. If you're using VSCode (like I am), I recommend installing the "Qt for python" extension, as it will install QtDesigner and ensure seamless integration with VSCode.



## Source Structure
This section of the readme will document each and every file found in the root/src/ directory.

### app_framework.py
It's possible to implement signals/slots natively using QtDesigner, but this is incredibly limited. Thus, app_framework.py exists to allow for custom implementation of buttons created with QtDesigner.

### design_ui.py
This is the result of using pyuic to auto-generate python UI code in accordance with the contents of design.ui

### design.ui
This file is what you modify whenever you make a change in QtDesigner. After you finish tweaking the UI, this file must be compiled into python code using pyuic (which results in the afformentioned design_ui.py file)

### main.py
As the name implies, this is the launching point of the program.

### mplwidget.py
This is a special widget which contains a matplotlib canvas, and is what this program uses to display and let the user interact with the graphical plot.

### parser.py
Called when clicking the "Graph" button. This code is responsible for converting user input into a plotable lambda.
