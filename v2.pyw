import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
import winsound

notlar = {
    Qt.Key_1: 261.63, Qt.Key_2: 293.66, Qt.Key_3: 329.63, Qt.Key_4: 349.23,
    Qt.Key_5: 392.00, Qt.Key_6: 440.00, Qt.Key_7: 493.88, Qt.Key_8: 523.25,
    Qt.Key_9: 553.55
}

class PyPiano(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyPiano by SekoMirson")
        self.label = QLabel("123456789 tuşlarına basarak piyano çalabilirsiniz.", self)
        self.label.setGeometry(25, 25, 300, 50)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() in notlar:
            frequency = notlar[event.key()]
            winsound.Beep(int(frequency), 300)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PyPiano()
    window.setGeometry(100, 100, 300, 150)
    window.show()
    sys.exit(app.exec_())
