#!/usr/bin/env python
# coding=utf-8

import nuke

seperator = "="*89

print(seperator)
print("Plugin's List ")
for each in nuke.plugins():
    print(each)

print(seperator)
print("Plugin Paths")
for each in nuke.pluginPath():
    print(each)











