import sys
from menu1 import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.actionExit.triggered.connect(self.close)
		self.ui.actionSave.triggered.connect(self.saveToFile)
		
	def saveToFile(self):
		options = QtWidgets.QFileDialog.Options()
		self.fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save To File", "", "HTML Files (*.html)", options=options)
		if self.fileName:
                        self.writeFile = open(self.fileName, 'w', encoding='utf-8')
                        self.writeFile.write(self.ui.plainTextEdit.toHtml())
                        self.writeFile.close()
                        self.ui.statusbar.showMessage('Saved to %s' % self.fileName)
                        
	def closeEvent(self, e):
		result = QtWidgets.QMessageBox.question(self, "Confirm Dialog", "Really quit?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
		if result == QtWidgets.QMessageBox.Yes:
			e.accept()
		else:
			e.ignore()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	myapp = MyWin()
	myapp.show()
	sys.exit(app.exec_())
