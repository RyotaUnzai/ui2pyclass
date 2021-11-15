import xml.etree.ElementTree as xml
from cStringIO import StringIO

# PySide
try:
    import PySide
    import pysideuic
except ImportError:
    import PySide2
    import pyside2uic as pysideuic


class ui2pyclass(object):
    def __init__(self, ui, titleName="From"):
        self.__ui = ui
        self.__titleName = titleName
        self.__formClass = None
        self.__baseClass = None
        self.__widgetClass = None

        self.loadUiType()

    def fixedUiText(self, uiText=""):
        uiText = uiText.decode("utf-8")
        uiText_list = uiText.split("\n")
        classStartFlag = False
        classStart = "	def retranslateUi(self, %s):" % self.__titleName
        relpaceText1 = ", None, -1)"
        relpaceText2 = "QtWidgets.QApplication.translate(\"%s\", " % self.__titleName
        classLine = ""
        count = 0

        while True:
            try:
                classLine = (uiText_list[count])
            except Exception:
                return uiText.encode("ascii", "ignore")
            if classStart == classLine:
                classStartFlag = True
            if classStartFlag:
                try:
                    uiText_list[count].encode("ascii")
                    fixedUiTextLine = uiText_list[count].replace(relpaceText1, "")
                    fixedUiTextLine = fixedUiTextLine.replace(relpaceText2, "")
                    uiText = uiText.replace(uiText_list[count], fixedUiTextLine)
                except UnicodeEncodeError:
                    position = 0
                    uiTextEncodeText = ""
                    for word in uiText_list[count]:
                        try:
                            uiTextEncodeText += word.encode("ascii")
                        except Exception:
                            uiTextEncodeText += "%s" % hex(ord(u"%s" % word))
                        position += 1

                    fixedUiTextLine = uiTextEncodeText.replace(relpaceText1, "")
                    fixedUiTextLine = fixedUiTextLine.replace(relpaceText2, "u")
                    uiText = uiText.replace(uiText_list[count], fixedUiTextLine)

            count += 1

    def loadUiType(self):
        parsed = xml.parse(self.__ui)
        self.__widgetClass = parsed.find("widget").get("class")
        self.__formClass = parsed.find("class").text

        with open(self.__ui, "r") as f:
            o = StringIO()
            frame = {}
            pysideuic.compileUi(f, o, indent=0)
            value = self.fixedUiText(uiText=o.getvalue())
            pyc = compile(value, "<string>", "exec")
            exec pyc in frame
            self.__formClass = frame["Ui_%s" % self.__formClass]
            self.__baseClass = getattr(PySide2.QtWidgets, self.__widgetClass)

        return self.__formClass, self.__baseClass

    @property
    def formClass(self):
        pass

    @formClass.getter
    def formClass(self):
        return self.__formClass

    @property
    def baseClass(self):
        pass

    @baseClass.getter
    def baseClass(self):
        return self.__baseClass
