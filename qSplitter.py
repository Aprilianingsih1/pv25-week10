import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *

class Splitter(QWidget):
    
    def __init__(self):
        super(Splitter, self).__init__()
        
    def initUI(self):
        hbox = QHBoxLayout(self)
        
        top_left = QFrame()
        top_left.setFrameShape(QFrame.StyledPanel)
        
        button = QFrame()
        button.setFrameShape(QFrame.StyledPanel)
        
        splt1 = QSplitter(Qt.Horizontal)
        text = QTextEdit()
        
        splt1.addWidget(top_left)
        splt1.addWidget(text)
        splt1.setSizes([350, 450])

        splt2 = QSplitter(Qt.Vertical)
        splt2.addWidget(splt1)
        splt2.addWidget(button)

        hbox.addWidget(splt2)

        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

        self.setGeometry(450, 450, 400, 300)
        self.setWindowTitle('QSplitter Demo')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Splitter()
    ex.initUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()