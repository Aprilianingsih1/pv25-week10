import sys
from PyQt5.QtWidgets import *

class Window(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()

        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("Cascade")
        file.addAction("Tiled")
        file.triggered[QAction].connect(self.windowAction)
        self.setWindowTitle("Multiple Document Interface Demo")

    def windowAction(self, p):
        print("triggered")

        if p.text() == "New":
            Window.count += 1
            sub = QMdiSubWindow()
            sub.setWindowTitle("Window" + str(Window.count))
            self.mdi.addSubWindow(sub)
            sub.show()
        if p.text() == "Cascade":
            self.mdi.cascadeSubWindows()

        if p.text() == "Tiled":
            self.mdi.tileSubWindows()

def main():
    app = QApplication(sys.argv)
    Win = Window()
    Win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()