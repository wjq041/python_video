# PyQt5 images
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.iniiUI()

    def iniiUI(self):
        central_widget= QWidget()
        self.setCentralWidget(central_widget)

        label1=QLabel("#1", self)
        label2=QLabel("#2", self)
        label3=QLabel("#3", self)
        label4=QLabel("#4", self)
        label5=QLabel("#5", self)
        label6=QLabel("#6", self)


        label1.setStyleSheet("background-color: red;")
        label2.setStyleSheet("background-color: yellow;")
        label3.setStyleSheet("background-color: green;")
        label4.setStyleSheet("background-color: blue;")
        label5.setStyleSheet("background-color: purple;")
        label6.setStyleSheet("background-color: gray;")


        vbox=QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)
        vbox.addWidget(label6)


        central_widget.setLayout(vbox)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
