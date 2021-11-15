<img width=260 src=logo.svg>

ui2pyclass.py can be used to convert .ui to a Python Class.


### Required installation
ui2pyclass uses [elementtree-xpath](https://docs.python.org/ja/2.7/library/xml.etree.elementtree.html#elementtree-xpath), needs to be `pip install lxml` installed




### Usage
ui2pyclass.py be able to a class that inherits from baseClass and formClass, after specifying the object name of the main object in ui and .ui file path


```python
import os
from PySide2.QtWidgets import *
from ui2pyclass import *

absPath = os.path.dirname(__file__)
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
<img width=400 src=QtDesiner.png>

- Also see [/examples](examples)


