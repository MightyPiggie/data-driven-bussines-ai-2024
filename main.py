import folium
from PySide6 import QtCore, QtWidgets
from PySide6.QtWebEngineWidgets import QWebEngineView
import random
import webbrowser
import requests


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    view = QWebEngineView()
    m = folium.Map(location=(52.0838811 , 5.1756689))
    popup = folium.GeoJsonPopup(fields=["naam", "geocode_nr", "km_geocode"])
    folium.GeoJson("trace-spoorwegen.geojson").add_to(m)
    folium.GeoJson("stations-spoorwegen.geojson", popup=popup).add_to(m)
    m.save("map.html")
    html = m.get_root().render()
    view.setHtml(html)
    view.show()
    app.exec()
    print("test")
    

        