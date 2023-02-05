echo off
echo started
@REM This file takes in an arguments: name.
set name=%1
python welcome.py %name%
start C:\Users\The user\AppData\Local\slack\slack.exe
echo %Welcome to class! This is for taking notes% > Notes.docx
start Notes.docx
echo completed
@REM I did echo off to suppress echoing for the terminal. printed 'started' at the beginning and 'completed' by the end.
@REM set name to be the argument on index 1. called the python file with the system argument.
@REM Started slack. Created a word document with text inside. Started the word document.