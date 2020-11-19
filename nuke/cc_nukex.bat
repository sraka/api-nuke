@echo off
color A

set SELF_PATH=%~dp0
set NUKE_VERSION=%1
set NUKE_APP_VERSION=%2
set NUKE_PATH=%SELF_PATH%/_setup;

"%ProgramFiles%/Nuke%NUKE_APP_VERSION%/Nuke%NUKE_VERSION%.exe" --nukex
::pause
