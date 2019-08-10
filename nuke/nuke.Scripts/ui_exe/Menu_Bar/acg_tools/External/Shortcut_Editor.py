import ui_src.Menu_Bar.acg_tools.External.Shortcut_Editor.Shortcut_Editor as Shortcut_Editor

try:
    Shortcut_Editor.nuke_setup()
    Shortcut_Editor.gui()
except Exception:
    import traceback
    traceback.print_exc()