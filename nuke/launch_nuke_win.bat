@echo off
color A

set SELF_PATH=%~dp0

::_______ PIPELINE PATH ____/usr/bin/env foundry_LICENSE=4101@ws05.hyd.taufilms.com:4101@ws188.kul.taufilms.com /usr/local/Nuke11.3v2/Nuke11.3
____
set CORE_LIBRARY=E:/__CS_code/acgfilms/repos/PROJECTS/edit-space/python-lib-ctm


::_______ PROJECT PATH ________
set PROJECT_CODE=BM
set PROJECT_NAME=batman



::_______ NUKE PATH ________
set NUKE_VERSION=10.0
set NUKE_APP_VERSION=10.0v4
set NUKE_PATH=%SELF_PATH%/load;


::_______ LAUNCH NUKE ________
"%ProgramFiles%/Nuke%NUKE_APP_VERSION%/Nuke%NUKE_VERSION%.exe" --nukex
::pause







::set CORE_LIBRARY=%SELF_PATH%/../../python-lib-ctm;
::set PROJECT_SERVER_PATH=%HOME_DIR%/projects/%PROJECT_NAME%
::set PROJECT_PATH=%PROJECT_SERVER_PATH%/%PROJECT_NAME%
