import folium
from PySide6 import QtCore, QtWidgets
from PySide6.QtWebEngineWidgets import QWebEngineView
import random
import webbrowser


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    view = QWebEngineView()
    m = folium.Map(location=(52.0838811 , 5.1756689))
    html = m.get_root().render()
    view.setHtml(html)
    view.show()
    app.exec()
    print("test")
    

        