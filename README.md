# CursesEditor

CursesEditor is a simple and lightweight text editor built using Python's `curses` library. It provides a terminal-based user interface for editing text files, making it a versatile tool for developers, writers, and anyone who prefers a distraction-free editing experience.

## Features

- **Simple and intuitive interface**: CursesEditor offers a clean and minimalistic interface, allowing you to focus on your text editing without any distractions.
- **File management**: Open, save, and create new text files directly from the editor.
- **Configurable keybindings**: Customize keyboard shortcuts to suit your preferences.

## Demo

https://github.com/BRArjun/TUITextEditor/assets/123864588/6b2bed90-8397-4051-849c-5afd2dfdd887

## Installation

CursesEditor is packaged as a standalone executable using PyInstaller, so you don't need to install Python or any dependencies separately. Simply download the latest release from the [Releases](https://github.com/BRArjun/TUITextEditor/releases) page and run the executable file.

For Linux and macOS users:

```bash
cd TUITextEditor
chmod +x /dist/TUIEdit  # Make the file executable
./TUIEdit          # Run the editor

Or you can just double click on the binary after giving it suitable permissions.
```

For Windows users make sure to download the [windows-curses](https://pypi.org/project/windows-curses/) package beforehand.
Please note that I run a Linux machine and have developed this project according to my specifications such as running it on the gnome terminal, as that is what I use.
You may need to change this in the source code according to your needs and rebuild from source.
Also this has not been checked to run on Windows machines and I do not know if the windows-curses library can support functionalities that I have implemented in this project.
Please check that on you own :).
## Development

If you want to modify the code for this project to your liking

- First clone this repository
```bash
git clone https://github.com/BRArjun/TUITextEditor.git
```
- Navigate to the project directory
```bash
cd TUITextEditor
```
- The source code is present in this directory and you can modify it to you liking.

## Building from Source

If you want to create a standalone installer for this Python file:

- Install PyInstaller
```
pip install pyinstaller
```
- Navigate to the project directory
```bash
cd TUITextEditor
```
- Build the executable
```bash
pyinstaller TUIEdit.py
```
Your binary will be located inside the dist folder.
Please make sure to first delete the old build, dist and .spec files before rebuilding from source.

## Future Scope

- AI Integration: Integrate AI to increase productivity for the end users by helping them ask their questions to the model inside the editor.
- Collaborative editing: Enable real-time collaborative editing, allowing multiple users to work on the same file simultaneously.
- Plugin system: Develop a plugin system to extend the editor's functionality with custom features and tools.
- Theming and customization: Provide options for customizing the editor's appearance, including color schemes, fonts, and UI elements. Although, we are limited by the colors that your terminal and curses supports. 
- Syntax highlighting: Support syntax highlighting for various programming languages, making it easier to read and edit code.

## Contributing
Contributions to CursesEditor are welcome! If you find any bugs, have feature requests, or want to contribute code, please open an issue or submit a pull request on the GitHub repository.
