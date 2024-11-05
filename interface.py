from PySide6 import QtCore, QtWidgets
import csv

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

# print(contractgebiedcodes)
    

if __name__ == '__main__':
    
    app = QtWidgets.QApplication([])
    window = QtWidgets.QWidget()
    formLayout = QtWidgets.QFormLayout()
    stm_geo_mld = QtWidgets.QComboBox()
    stm_geo_mld.addItems(geocodes)
    stm_prioriteit = QtWidgets.QComboBox()
    stm_prioriteit.addItems(["1", "2", "4", "5", "8"])
    stm_oorz_code = QtWidgets.QComboBox()
    stm_oorz_code.addItems(oorzaakcodes)
    stm_contractgeb_gst = QtWidgets.QComboBox()
    stm_contractgeb_gst.addItems(contractgebiedcodes)
    formLayout.addRow("stm_geo_mld", stm_geo_mld)
    formLayout.addRow("stm_prioriteit", stm_prioriteit)
    formLayout.addRow("stm_oorz_code", stm_oorz_code)
    formLayout.addRow("stm_contractgeb_gst", stm_contractgeb_gst)
    window.setLayout(formLayout)
    window.show()

    app.exec()