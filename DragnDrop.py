import sys
from PyQt5.QtWidgets import *

class DragAndDrop(QComboBox):

    def __init__(self, title, parent):
        super(DragAndDrop, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, text):
        print(text)
        print(text.mimeData())

        if text.mimeData().hasText():
            text.accept()
        else:
            text.ignore()

    def dropEvent(self, text):
        self.addItem(text.mimeData().text())

class widget(QWidget):
    def __init__(self):
        super(widget, self).__init__()
        self.initUI()

    def initUI(self):
        layout = QFormLayout()
        layout.addRow(QLabel("Type some text in textbox and drag into combo box"))

        edit = QLineEdit()
        edit.setDragEnabled(True)
        combo = DragAndDrop("Button", self)

        layout.addRow(edit, combo)
        self.setLayout(layout)
        self.setWindowTitle("Drag and Drop Demo")

def main():
    app = QApplication(sys.argv)
    ex = widget()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()