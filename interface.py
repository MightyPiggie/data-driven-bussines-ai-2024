from PySide6 import QtCore, QtWidgets
import csv
import random
import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout
from PySide6.QtCore import QTimer

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

with open('datasets/geocodes.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    geocodes = list(reader)
    geocodes = [geocode[0] for geocode in geocodes]
    geocodes = geocodes[1:]
    
with open('datasets/oorzaakcodes.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    oorzaakcodes = list(reader)
    oorzaakcodes = [oorzaakcode[0] for oorzaakcode in oorzaakcodes]
    oorzaakcodes = oorzaakcodes[1:]
    
with open('datasets/contractgebiedcodes.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    contractgebiedcodes = list(reader)
    contractgebiedcodes = [contractgebiedcode[1] for contractgebiedcode in contractgebiedcodes]
    contractgebiedcodes = contractgebiedcodes[1:]
    
with open('datasets/techniekvelden.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    techniekvelden = list(reader)
    techniekvelden = [techniekvelde[1] for techniekvelde in techniekvelden]
    techniekvelden = techniekvelden[1:]

# print(techniekvelden)
    

# if __name__ == '__main__':
    
    # app = QtWidgets.QApplication([])
    # window = QtWidgets.QWidget()
    
    # window.setLayout(formLayout)
    # window.show()

    # app.exec()
    




class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class App(QWidget):

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        
        self.formLayout = QtWidgets.QFormLayout()
        # formLayout = QtWidgets.QFormLayout()
        self.stm_geo_mld = QtWidgets.QComboBox()
        self.stm_geo_mld.addItems(geocodes)
        self.stm_prioriteit = QtWidgets.QComboBox()
        self.stm_prioriteit.addItems(["1", "2", "4", "5", "8"])
        self.stm_oorz_code = QtWidgets.QComboBox()
        self.stm_oorz_code.addItems(oorzaakcodes)
        self.stm_contractgeb_gst = QtWidgets.QComboBox()
        self.stm_contractgeb_gst.addItems(contractgebiedcodes)
        self.stm_techn_mld = QtWidgets.QComboBox()
        self.stm_techn_mld.addItems(techniekvelden)
        self.sumbit_button = QtWidgets.QPushButton("Submit")
        self.sumbit_button.clicked.connect(lambda: self.on_submit())
        self.formLayout.addRow("stm_geo_mld", self.stm_geo_mld)
        self.formLayout.addRow("stm_prioriteit", self.stm_prioriteit)
        self.formLayout.addRow("stm_oorz_code", self.stm_oorz_code)
        self.formLayout.addRow("stm_contractgeb_gst", self.stm_contractgeb_gst)
        self.formLayout.addRow("stm_techn_mld", self.stm_techn_mld)
        self.formLayout.addRow(self.sumbit_button)
        self.layout = QVBoxLayout()
        self.layout.addLayout(self.formLayout)
        
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.layout.addWidget(self.canvas)
        # self.formLayout.addRow(self.canvas)
        self.setLayout(self.layout)
        # self.setCentralWidget(self.canvas)

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 10) for i in range(n_data)]
        self.update_plot()

        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.ydata = self.ydata[1:] + [random.randint(0, 10)]
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()
        
    def on_submit(self):
        print("submit")
        print(self.stm_geo_mld.currentText(), self.stm_prioriteit.currentText(), self.stm_oorz_code.currentText(), self.stm_contractgeb_gst.currentText(), self.stm_techn_mld.currentText())


app = QApplication(sys.argv)
w = App()
app.exec()