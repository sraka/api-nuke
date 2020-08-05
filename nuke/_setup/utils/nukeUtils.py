import os
import nuke
import platform
import subprocess


def nOpenFolder(path):
    """
    Open folder based on OS.
    :param path:
    :type path:
    :return: None
    :rtype: None
    """
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    elif platform.system() == "Linux":
        try:
            subprocess.check_call(["gnome-open", path])
        except OSError as e:
            nuke.message("Linux Platform other than gnome are currently not supported")
    else:
        nuke.message("Unsupported OS")
