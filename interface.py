from PySide6 import QtWidgets
import csv
import sys
import matplotlib
matplotlib.use('Qt5Agg')

from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from joblib import load
import sklearn as sk

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

model = load(f"models/VotingClassifier.joblib")




class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class App(QWidget):

    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setGeometry(100, 100, 1200, 800)
        self.formLayout = QtWidgets.QFormLayout()
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
        self.canvas.axes.set_position([0.1, 0.3, 0.8, 0.6])  # Adjust the position to give more space at the bottom

        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

        self.show()

    def update_plot(self):
        x_data = [300, 840, 1499, 2220, 2940, 3722.1, 5280, 7619, 10155, 13440, 16675.56, 22500, 28800]
        x_data2 = [i for i in range(1, len(x_data))]
        x_data3 = [i for i in range(len(x_data)+1)]
        print(self.result)
        self.result = self.result[0]  # Assuming the result is a 2D array and we need the first row
        self.canvas.axes.cla()
        self.canvas.axes.hist(x_data2, bins=x_data3, weights=self.result, align='left', rwidth=0.9, ec='red')
        self.canvas.axes.set_xticks(x_data2)
        self.canvas.axes.set_xticklabels([f"{x_data[i]}-{x_data[i+1]}" for i in range(len(x_data)-1)], rotation=45, ha='center')
        self.canvas.axes.set_xlabel('Range')
        self.canvas.axes.set_ylabel('Probability')
        self.canvas.axes.set_title('Predicted Probabilities')
        self.canvas.draw()
        
    def on_submit(self):
        print("submit")
        print(self.stm_geo_mld.currentText(), self.stm_prioriteit.currentText(), self.stm_oorz_code.currentText(), self.stm_contractgeb_gst.currentText(), self.stm_techn_mld.currentText())
        self.result = model.predict_proba([[self.stm_geo_mld.currentText(), self.stm_prioriteit.currentText(), self.stm_oorz_code.currentText(), self.stm_contractgeb_gst.currentText(), self.stm_techn_mld.currentText()]])
        self.update_plot()


app = QApplication(sys.argv)
w = App()
app.exec()