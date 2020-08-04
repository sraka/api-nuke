import nukescripts
import nuke

class tpanel(nukescripts.PythonPanel):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, 'TPanel', 'com.ohufx.SearchReplace')
        self.dropdown = nuke.Enumeration_Knob('Layer1', 'Project:', ['a', 'b', 'c', 'd'])
        self.update = nuke.PyScript_Knob('update', 'Update')

        self.addKnob(self.dropdown)
        self.addKnob(self.update)

    def knobChanged(self, knob):
        # check which knob was changed
        if knob == self.update:
            print
            self.dropdown.value()


tpanel().showModalDialog()