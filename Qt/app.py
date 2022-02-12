import sys

from PyQt5 import QtWidgets

from Qt import chatgui


class AppChat(QtWidgets.QMainWindow, chatgui.Ui_MainWindow):
    def __init__(self):
        super(AppChat, self).__init__()
        self.setupUi(self)
        self.build_handlers()

    def build_handlers(self):
        self.pushButton.clicked.connect(self.on_click_btn)

    def on_click_btn(self, event):
        message = self.lineEdit.text()
        self.plainTextEdit.appendPlainText(message)
        self.lineEdit.setText('')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AppChat()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()