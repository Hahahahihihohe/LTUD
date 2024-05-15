import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class window(QWidget):
   def __init__(s, parent = None):
      super(window, s).__init__(parent)
      s.resize(1500,1200)
      s.setWindowTitle("BAN VE XEM PHIM")
      s.label = QLabel(s)
      s.label.setText("Hello World")
      font = QFont()
      font.setFamily("Arial")
      font.setPointSize(16)
      s.label.setFont(font)
      s.label.move(500,5002)
def main():
   app = QApplication(sys.argv)
   ex = window()
   ex.show()
   sys.exit(app.exec_())
if __name__ == '__main__':
   main()