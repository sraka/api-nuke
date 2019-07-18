@echo off
color A

set SELF_PATH=%~dp0

::_______ PIPELINE PATH ____
____
set CORE_LIBRARY=E:/__CS_code/acgfilms/repos/PROJECTS/dev-zone/python-corelib/core-lib

::_______ NUKE PATH ________
set NUKE_VERSION=10.0
set NUKE_APP_VERSION=10.0v4
set NUKE_PATH=%SELF_PATH%/load;

set PYTHONPATH=%PYTHONPATH%;E:\__CS_code\acgfilms\repos\PIPELINE\python\Lib\site-packages-dcc

::_______ LAUNCH NUKE ________
"%ProgramFiles%/Nuke%NUKE_APP_VERSION%/Nuke%NUKE_VERSION%.exe" --nukex
pause

