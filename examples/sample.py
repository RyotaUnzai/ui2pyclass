# -*- coding: utf-8 -*-
import os
try:
    from PySide.QtGui import *
except ImportError:
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
