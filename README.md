# PyGUI-Basics

### What?
This repository is a demo how to use different GUI framworks with Python.

### Why?
It provides some cool missing functions like storing window positions and also remembering contents of specific controls. A must have for most applications. Settings are stored by QSettings, which is stored dependend on your operatin system in the Windows registry or in `~/.config/[companyname]/`

### External ui files preferred
Qt based frameworks like PyQt and PySide are used with seperated ui files. These can be modified with `Qt Designer`. It's better to seperate code from ui. User interfaces are also not converted to py files. It's easier to edit ui files at any time.

### Content
The modules `main*.py` are demo files.

The `window*.py` modules are helper and wrapper for the specific framework.

The structure is quite old and I just decided to switch from PyQt5 to PySide6. Because of Qt Designer and it's ui files, I decided to not subclass each QWidget. So this code base is not too OOP compliant. Widgets just get directly some new attributes. 

Nevertheless I also updated the older PyQt5 library for some you.


### QDockWidget
Cool thing. But currently buggy in PyQt5 and in PySide6 with Qt5-ui files.

PyQt5 crashes if the widget has all features enabled.

`AttributeError: type object 'QDockWidget' has no attribute 'DockWidgetFeatureMask'`

Bug has been reported to PyQt5 mailing list.

When using Qt5-ui files with PySide6, the widget may appear as `DockWidgetVerticalTitleBar` even if not selected in designer.

### TODO
A lot of!

Totally not my preferred code style and persistency has to be extended to more controls.

Status of this repository is still `experimental`. I'm happy to get fans, testers and help.

Documentation and comments will follow.

Also `Tkinter` will get a nice wrapper here.

`Kivy` is too generalized for mobile devives. Maybe.
