@echo off
color A

set SELF_PATH=%~dp0

::set CORE_LIBRARY=%SELF_PATH%/../../python-corelib/core-lib/
::set PYTHONPATH=%PYTHONPATH%;::E:\__CS_code\acgfilms\repos\PIPELINE\python\Lib\site-packages-dcc
set NUKE_PATH=%SELF_PATH%/_setup;%SELF_PATH%/../xxPrSuite;
::%SELF_PATH%/xDekeKincaid\nuke.env-master

::echo %CORE_LIBRARY%
::echo %PYTHONPATH%
::echo %NUKE_PATH%

::_______ LAUNCH NUKE ________
::_______ NUKE PATH ________
set NUKE_VERSION=10.5
set NUKE_APP_VERSION=10.5v1
"%ProgramFiles%/Nuke%NUKE_APP_VERSION%/Nuke%NUKE_VERSION%.exe"
::pause
