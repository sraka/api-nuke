import nuke

p = nuke.Panel('my custom panel')


p.addClipnameSearch('clip path', '/tmp')
p.addFilenameSearch('file path', '/tmp')
p.addTextFontPulldown('font browser', '/myFonts/')
p.addRGBColorChip('some pretty color', '')
p.addExpressionInput('enter an expression', '4*25')
p.addBooleanCheckBox('yes or no?', True)
p.addEnumerationPulldown('my choices', 'A B C')
p.addScriptCommand('tcl or python code', '')
p.addSingleLineInput('just one line', 'not much space')
p.addMultilineTextInput('multiple lines of user input text', 'lineA\nlineB')
p.addNotepad('write something', 'some very long text could go in here. For now this is just some random default value')
p.addPasswordInput('password', 'donttellanyone')
p.addButton('push here')
p.addButton('or here')
p.addButton('or even here')

print "AA"
ret = p.show()
