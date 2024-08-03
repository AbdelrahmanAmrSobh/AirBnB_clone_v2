#!/usr/bin/python3
"""
    Use fabric to pack folder web_static
"""
from datetime import datetime
from fabric.api import *
from os.path import isdir


def do_pack():
    """
        Use fabric to pack files
    """
    fileName = "versions/web_static_"\
               + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    if isdir("versions") is False:
        local("mkdir versions")
    local(f"tar -cvzf {fileName} web_static")
    return fileName
