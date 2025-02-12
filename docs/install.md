#Installation Guide for TextMasterPy

Prerequisites  
Before installing **TextMasterPy**, ensure that you have **Python 3.6 or later** installed on your device.

**Checking if Python is Installed**
To check if Python is installed on your system, open the terminal and type:  
python --version
or:
python -V
If Python is not installed, follow the instructions below.
 
Installing Python
On Windows
If Python is not installed, you can install it via PowerShell using:
winget install Python.Python
This command will install the latest version of Python on your system.

To upgrade an existing installation, run on powershell:
winget install Python.Python --upgrade
On macOS (via Homebrew)
brew install python
On Linux (Ubuntu/Debian)
sudo apt update && sudo apt install python3 -y
For other Linux distributions, use the corresponding package manager (dnf, pacman, etc.).
 
📦 Installing TextMasterPy
Once Python is installed, you can install TextMasterPy using pip:
pip install textmasterpy
To verify that the installation was successful, run on terminal:
pip show textmasterpy
If you see details about the framework, including its version and author, the installation was successful.
 
 Using a Virtual Environment (Recommended)
To avoid conflicts with other Python packages, it's highly recommended to use a virtual environment:

Updating TextMasterPy
To update TextMasterPy to the latest version, run on terminal:
pip install --upgrade textmasterpy

Uninstalling TextMasterPy
If you want to remove TextMasterPy from your system, run on terminal:
pip uninstall textmasterpy

note:
When using pip commands to install the framework on a Google Colab notebook, make sure to precede each pip command with an exclamation mark.

Getting Started
Now that TextMasterPy is installed, you can import it into your Python environment and start using its built-in functions.
import textmasterpy
print("TextMasterPy is ready!")
 
Checking the Latest Version
The current version of TextMasterPy is 1.0.1. You can always check for updates on PyPI:
https://pypi.org/project/textmasterpy/1.0.1/