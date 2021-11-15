<img width=260 src=logo.svg>

ui2pyclass.py can be used to convert .ui to a Python Class.


### Usage

ui2pyclass.py be able to a class that inherits from baseClass and formClass, after specifying the object name of the main object in ui and .ui file path

```python
import os
from PySide2.QtWidgets import *
from ui2pyclass import *

absPath = getDirname(__file__)
uiPath = os.path.join(absPath, "view.ui")

ui = ui2pyclass(ui=uiPath, objectName="ui2pyclass")
class uiWidget(ui.baseClass, ui.formClass):
    def __init__(self, parent=None, *args, **kwargs):
        super(uiWidget, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)

def main():    
    app = QApplication.instance()
    ex = uiWidget()
    ex.show()
    sys.exit()
    app.exec_()

main()
```
- Also see [/examples](examples)

