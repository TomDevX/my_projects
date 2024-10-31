import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(800, 800)

        self.setStyleSheet('background:black;')


        mainLayout = QVBoxLayout(self)
        mainLayout.setContentsMargins(0, 0, 0, 0)

        color_1 = '162, 162, 162,'
        color_2 = '255, 255, 255,'
        color_3 = '0, 255, 255,'

        d_ = 1

        power = int(255/100*d_)

        for x in range(6):
            label = QLabel(self)


            color_L = color_1
            glass_L = 255
            size_L = 60
            blut_L = 0


            label.raise_()

            if x < 1 :
                color_L = color_1
            elif x < 2 :
                color_L = color_3
                glass_L = power
            elif x < 3 :
                color_L = color_2
                blut_L = 6
                glass_L = power
            elif x < 4:
                color_L = color_2
                blut_L = 40
                glass_L = power
            elif x < 5 :
                label.lower()
                color_L = color_3
                blut_L = 40
                size_L = 70
                glass_L = power
            elif x < 6 :
                label.lower()
                color_L = color_3
                blut_L = 150
                size_L = 70
                glass_L = power

            label.setText('test')
            label.setStyleSheet('background:rgba(0, 0, 0, 0);color:rgba({} {}); font-size:{}px;'.format(color_L, glass_L,size_L))
            label.resize(self.width(), self.height())
            label.setAlignment(Qt.AlignCenter)

            self.effect = QGraphicsBlurEffect(blurRadius=blut_L)
            label.setGraphicsEffect(self.effect)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
