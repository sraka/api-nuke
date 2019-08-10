@echo off
color A

set SELF_PATH=%~dp0


set CORE_LIBRARY=%SELF_PATH%/../../python-corelib/core-lib/
set PYTHONPATH=%PYTHONPATH%;E:\__CS_code\acgfilms\repos\PIPELINE\python\Lib\site-packages-dcc
set NUKE_PATH=%SELF_PATH%/_setup;C:\Users\artis\Downloads\Pr_Suite

echo %CORE_LIBRARY%
echo %PYTHONPATH%
echo %NUKE_PATH%

::_______ LAUNCH NUKE ________
::_______ NUKE PATH ________
set NUKE_VERSION=10.0
set NUKE_APP_VERSION=10.0v4
"%ProgramFiles%/Nuke%NUKE_APP_VERSION%/Nuke%NUKE_VERSION%.exe" --nukex
::pause

