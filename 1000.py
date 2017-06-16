import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QDesktopWidget, QMainWindow, QLabel)
from PyQt5.QtGui import (QFont, QIcon)
from PyQt5.QtCore import QCoreApplication

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('Тут <i><b>нет</b></i> кнопки.')

        self.btn = QPushButton('Button', self)
        self.btn.clicked.connect(self.buttonClicked)
        self.btn.setToolTip('Да, вот она, <b>кнопочка</b> :-)')
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(50, 50)

        qbtn = QPushButton('Quit', self)
        #qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.clicked.connect(self.close)
        qbtn.setToolTip('А это выход!')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 50)
        
        self.lbl1 = QLabel('Нажми же кнопочку!', self)
        self.lbl1.move(40, 20)
        
        self.setGeometry(250, 200, 400, 300)
        self.setWindowTitle('Програмка же!')
        self.setWindowIcon(QIcon('player.png'))
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def buttonClicked(self):
        self.lbl2 = QLabel('Сообщение 2', self)
        self.lbl2.move(15, 20)
        
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
