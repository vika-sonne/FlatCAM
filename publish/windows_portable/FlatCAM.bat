@echo off

echo Run FlatCAM...

:: set environment variables to run FlatCAM
set Path=%CD%\Python310;%Path%
set PYTHONPATH=%CD%\Python310\Lib;%CD%\Python310\DLLs;
set TCL_LIBRARY=%CD%\Python310\tcl\tcl8.6

python FlatCAM_2024_4.zip
