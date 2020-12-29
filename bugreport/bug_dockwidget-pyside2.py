import sys
from PySide2.QtWidgets import QApplication
from PySide2 import QtUiTools

app = QApplication(sys.argv)
w = QtUiTools.QUiLoader().load("bug_dockwidget.ui")
w.show()
sys.exit(app.exec_())
