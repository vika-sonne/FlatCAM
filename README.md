# FlatCAM β (c) 2024.4

![FlatCAM β](/FlatCAM/assets/resources/flatcam_icon128.png)
Based on
* FlatCAM BETA (c) 2019 by Marius Stanciu
* 2D Computer-Aided PCB Manufacturing by (c) 2014-2016 Juan Pablo Caram

FlatCAM is a program for preparing CNC jobs for making PCBs on a CNC router.
Among other things, it can take a Gerber file generated by your favorite PCB
CAD program, and create G-Code for Isolation routing.

### Example of PCB Isolation Routing from Gerber file (.gbr) to CNC G-Code (.nc) file:
1-2 Open Gerber file (.gbr).<br>
3 Double click .gbr file in Project tab panel.<br>
4 Click "Isolation Routing" button.<br>
5 Click "Generatew geometry" button.<br>
6 Click "Generate CNCJob object" button.<br>
7-8 Save CNC G-code file (.nc).

![Isolation Routing](/media/IsolationRouting.webp)

# Installation instructions

## Windows portable installation

This installation contains Python with installed packages and Qt binaries.

Note: Python 3.10 supports Windows 8.1 and newer.

* Download and install [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022) for Visual Studio 2019 x64
* Download and install [7z archiver](https://www.7-zip.org/download.html)
* Download .7z archive file from [releases page](https://github.com/vika-sonne/FlatCAM/releases), for example: `FlatCAM_2024_4_windows_portable.7z`
* Extract .7z archive and **run FlatCAM** in extracted folder: `FlatCAM.bat`

## Versions requirements
* **`Python 3.10`**
* `PyQt5`
* See `pyproject.toml` file for version dependency (or `requirements.txt` file)
* Use a **strictly versions** of Python and packages

See more on GitHub:
* [FlatCAM by Marius Stanciu](https://github.com/MRemy2/FlatCam)
* [Juan Pablo Caram](https://github.com/Denvi/FlatCAM)

## Installation

### 1. Python installation

See [Python downloads](https://www.python.org/downloads/).

### 2. Get pip
See [Pip documentation](https://pip.pypa.io/en/latest/installation/) to get `pip`.

### 3. Python packages installation

#### 3.1. Linux
Install Python packages:
```
python -m pip install --disable-pip-version-check --no-deps --ignore-installed -r requirements.txt
```

#### 3.2. Windows

Download and install:
* [Qt 5.15.2](https://www.qt.io/offline-installers)
* [.Net 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48) online installer (ndp48-web.exe) or offline installer (ndp48-x86-x64-allos-enu.exe)
* [VS C++ Build tools](https://visualstudio.microsoft.com/visual-cpp-build-tools) (vs_BuildTools.exe)

Set environment variables:
* Add python to Path variable; example: `Path=C:\Users\IEUser\AppData\Local\Programs\Python\Python310;%Path%`
* Add Qt to Path variable; example: `Path=C:\Users\IEUser\Downloads\msvc2019_64\bin;%Path%`
* Add variable QT_QPA_PLATFORM_PLUGIN_PATH for Qt plugins path; example: `QT_QPA_PLATFORM_PLUGIN_PATH=C:\Users\IEUser\Downloads\msvc2019_64\plugins\platforms`

Install Python packages with `PyQt5` windows version and `pywin32` package.
```
python -m pip install --disable-pip-version-check --no-deps --ignore-installed -r requirements_windows.txt
```

## Debian/Ubuntu instructions

So, according to strictly dependency graph and new version of Debian `pip` (disallow to install packages to system Python environment, for example Kubuntu 23.04), project moved to automated version control:
* [pyenv](https://github.com/pyenv/pyenv?ysclid=lhe4n4h8za388534739#installation) - for install to Python version environment
* [poetry](https://python-poetry.org/docs/) - for packages install to Python virtual environment. See `pyproject.toml` file

### pyenv usage

Install `pyenv`:
```
curl https://pyenv.run | bash
```

Add `pyenv` to interactive console. Add lines to `.bashrc`:
```
# pyenv
export PYENV_ROOT="$HOME/.pyenv"
command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

Show available python versions to download and install:
```
pyenv install --list
```

Install python (for example, 3.10.11, see `pyproject.toml` file for python version requirements):
```
pyenv install 3.10.11
# show installed python versions:
pyenv versions
```

Switch to Python version:
```
pyenv local 3.10.11
# or set global version (this not affect the system Python):
pyenv global 3.10.11
```

### poetry usage

Install `poetry`:
```
curl -sSL https://install.python-poetry.org | python3 -
```

Install python environment (packages) according to `pyproject.toml` file:
```
poetry install
# list all python environments:
poetry env list
```

For spetial cases it possible export poetry lock file to `requirements.txt` file for `pip` usage:
```
cd FlatCAM
poetry update
poetry export -f requirements.txt --output requirements.txt
python -m pip install --disable-pip-version-check --no-deps --ignore-installed -r requirements.txt
```

### Developer tools installation

Kubuntu 24.04:
```sh
sudo apt install pyqt5-dev-tools
```

# Run


```
python FlatCAM.zip
```

Get command-line help:
```
python FlatCAM.zip -h
usage: FlatCAM.zip [-h] [--shellfile SHELLFILE] [--shellvar SHELLVAR] [--headless] [-V] [misc ...]

2D Computer-Aided PCB Manufacturing for CNC

positional arguments:
  misc                  commands: quit, exit, save; file path: .FlatPrj, .FlatConfig, .FlatScript, .TCL

options:
  -h, --help            show this help message and exit
  --shellfile SHELLFILE
  --shellvar SHELLVAR
  --headless
  -V, --version         show version

Usage examples:
FlatCAM.zip --shellfile=<cmd_line_shellfile>
FlatCAM.zip --shellvar=<1,'C:\path',23>
FlatCAM.zip --headless
```
