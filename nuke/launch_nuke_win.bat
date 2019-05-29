@echo off
color A

set NUKE_VERSION=10.0
set NUKE_APP_VERSION=10.0v4
set SELF_PATH=%~dp0

::_______ PROJECT PATH ________
set PROJECT_CODE=BM
set PROJECT_NAME=batman
::set PROJECT_SERVER_PATH=%HOME_DIR%/projects/%PROJECT_NAME%
::set PROJECT_PATH=%PROJECT_SERVER_PATH%/%PROJECT_NAME%

::_______ PIPELINE PATH ________
::set CORE_LIBRARY=%SELF_PATH%/../../python-lib-ctm;
set CORE_LIBRARY=E:/__CS_code/acgfilms/repos/PROJECTS/edit-space/python-lib-ctm


::_______ NUKE PATH ________
set NUKE_PATH=%SELF_PATH%/load;


::_______ LAUNCH NUKE ________
"%ProgramFiles%/Nuke%NUKE_APP_VERSION%/Nuke%NUKE_VERSION%.exe" --nukex 
::pause

