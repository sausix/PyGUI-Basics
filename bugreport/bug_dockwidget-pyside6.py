import sys
from PySide6.QtWidgets import QApplication
from PySide6 import QtUiTools

app = QApplication(sys.argv)
w = QtUiTools.QUiLoader().load("bug_dockwidget-v6.ui")
w.show()
sys.exit(app.exec_())
