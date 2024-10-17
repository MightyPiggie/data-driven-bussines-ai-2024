import folium
from PySide6 import QtCore, QtWidgets
from PySide6.QtWebEngineWidgets import QWebEngineView
import random
import webbrowser
import requests
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv(r"dataset-prorail-clean-2.csv", nrows=10)
    df.dropna(subset=['stm_geo_mld'], inplace=True)
    geocodes = pd.read_csv(r"hectometerpunt-geocode.csv")
    df = df[['stm_geo_mld', 'stm_sap_meldtekst', 'stm_oorz_code' ]]

    for index, row in df.iterrows():
        geocode = geocodes[geocodes['GEOCODE_NR'] == row['stm_geo_mld']]
        if not geocode.empty:
            df.at[index, 'lat'] = geocode.iloc[0]['LATITUDE']
            df.at[index, 'lon'] = geocode.iloc[0]['LONGITUDE']
        else:
            df.drop(index, inplace=True)

    
    app = QtWidgets.QApplication([])
    view = QWebEngineView()
    m = folium.Map(location=(52.0838811 , 5.1756689))

    for i in range(0,len(df)):
        popupString = "Geocode: " + str(df.iloc[i]['stm_geo_mld']) + "<br>" + "Melding Omschrijving: " + str(df.iloc[i]['stm_sap_meldtekst']) + "<br>" + "Oorzaak code: " + str(df.iloc[i]['stm_oorz_code'])
        popup = folium.Popup(popupString, max_width=1000 )
        folium.Marker(
            location=[df.iloc[i]['lat'], df.iloc[i]['lon']],
            popup=popup,
            icon=folium.Icon(color='red',icon_color='#FFFF00')
        ).add_to(m)


    popup = folium.GeoJsonPopup(fields=["naam", "geocode_nr", "km_geocode"])
    folium.GeoJson("trace-spoorwegen.geojson").add_to(m)
    folium.GeoJson("stations-spoorwegen.geojson", popup=popup).add_to(m)
    m.save("index.html")
    html = m.get_root().render()
    view.setHtml(html)
    view.show()
    app.exec()
    print("test")
    

        