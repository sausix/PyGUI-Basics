#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from typing import Optional
from PySide2.QtCore import QCoreApplication, Slot, Qt
from PySide2.QtWidgets import QApplication, QComboBox
from window2 import Window, Dialog


class MainWindow(Window):
    def __init__(self):
        super().__init__("../MainWindow.ui")

        self.dialog: Optional[MyDialog] = None

        mnu = self.actionOptions
        mnu.setShortcut("Ctrl+O")
        mnu.setStatusTip("Show options")
        mnu.triggered.connect(self.show_options)

        sb = self.statusBar()
        sb.showMessage("Hello Statusbar!")

        cb: QComboBox = self.comboBox
        cb.addItem("A", 100)
        cb.addItem("B", 200)
        cb.addItem("C", 300)

        self.register_widget(self.dockWidget)
        self.register_widget(self.lineEdit)
        self.register_widget(self.checkBox, changefunc=self.toggled_dockcheckbox)
        self.register_widget(self.comboBox)
        self.register_widget(self.dateTimeEdit)

    def toggled_dockcheckbox(self, new_state):
        if new_state:
            self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockWidget)
            self.dockWidget.show()
        else:
            self.removeDockWidget(self.dockWidget)

    def show_options(self):
        self.open_dialog()

    @Slot()
    def on_pushButton_clicked(self):
        self.open_dialog()

    @Slot()
    def on_pushButtonModal_clicked(self):
        self.open_dialog(True)

    def open_dialog(self, modal: bool = False):
        if self.dialog is None:
            self.dialog = MyDialog()

        self.dialog.show(modal)

    def closeEvent(self, e):
        super().closeEvent(e)
        e.accept()
        QCoreApplication.exit()


class MyDialog(Dialog):
    def __init__(self):
        super(MyDialog, self).__init__("../Dialog.ui")

    def closeEvent(self, e):
        super().closeEvent(e)
        e.accept()


if __name__ == "__main__":
    QCoreApplication.setOrganizationName("MyCompany")
    QCoreApplication.setApplicationName("MyApp")
    QCoreApplication.setOrganizationDomain("MyCompany.example.com")

    qapp = QApplication(sys.argv)

    root = MainWindow()
    root.show()
    ret = qapp.exec_()
    sys.exit(ret)
