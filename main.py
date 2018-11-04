from PyQt5 import QtWidgets, QtCore
from design import design
import numpy as np
import pyqtgraph as pg


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pg.setConfigOptions(antialias=True)
        self.graphicsView.plot()

    def update_graphics(self):
        self.graphicsView.clear()
        a1 = self.verticalSlider_1.value()
        a2 = self.verticalSlider_2.value()
        a3 = self.verticalSlider_3.value()
        a4 = self.verticalSlider_4.value()
        a5 = self.verticalSlider_5.value()
        a6 = self.verticalSlider_6.value()
        fi1 = self.verticalSlider_7.value()
        fi2 = self.verticalSlider_8.value()
        fi3 = self.verticalSlider_9.value()
        fi4 = self.verticalSlider_10.value()
        fi5 = self.verticalSlider_11.value()
        fi6 = self.verticalSlider_12.value()
        shift = 0.01
        x = np.arange(-10, 10, shift)
        y = a1*np.cos(x + fi1) + a2*np.cos(2*x + fi2) + a3*np.cos(4*x + fi3) + a4*np.cos(6*x + fi4) + a5*np.cos(8*x + fi5) + a6*np.cos(10*x + fi6)
        self.graphicsView.plot(x, y, pen=pg.mkPen(color="r"))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()