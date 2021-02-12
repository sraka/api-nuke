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


print(seperator)
print("MENU BAR - MENU's List")

menubar = nuke.menu("Nuke")
for each in menubar.items():
    print each.name()

print(seperator)
print("NODE BAR - NODE Menu List")

nodebar = nuke.menu("Nodes")
for each in nodebar.items():
    print each.name()








