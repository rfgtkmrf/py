import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QDesktopWidget)
from PyQt5.QtGui import (QFont, QIcon)
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('Тут <i><b>нет</b></i> кнопки.')

        btn = QPushButton('Button', self)
        btn.clicked.connect(self.Button)
        btn.setToolTip('Да, вот она, <b>кнопочка</b> :-)')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        qbtn = QPushButton('Quit', self)
        #qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.clicked.connect(self.close)
        qbtn.setToolTip('А это выход!')
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 50)
        
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
        
    def Button(self):
        reply = QMessageBox.question(self, 'Вопрос, однако', 'Точно?', QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            pass
        else:
            pass
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
