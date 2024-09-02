import  phonenumbers
import folium
from phonenumbers import geocoder,carrier,timezone
from geopy.geocoders import Photon
class PhoneConfig:
    def __init__(self,numeroT):
        self.numeroT = numeroT

    def phone_search(self):
        numero = phonenumbers.parse(self.numeroT)
        zona_horaria = timezone.time_zones_for_number(numero)
        pais = geocoder.description_for_number(numero,"es")

        operador = carrier.name_for_number(numero,"es")

        info_data ={
        "Numero":phonenumbers.format_number(numero,phonenumbers.PhoneNumberFormat.INTERNATIONAL),
        "Pais":pais,
        "Operador":operador,
        "Zona horaria":zona_horaria
        }
        return info_data
    def mapa(self, localization, filename="telefono_mapa.html"):
        geolocator = Photon(user_agent="geoapiExercise")
        location = geolocator.geocode(localization)

        mapa = folium.Map(location=[location.latitude,location.longitude],zoom_start=10)
        folium.Marker([location.latitude,location.longitude],popup=localization).add_to(mapa)
        mapa.save(filename)
        print(f"mapa guardado:{filename}")

if __name__ == "__main__":
    d= PhoneConfig("+23103539653")
    info=d.phone_search()
    print(info)
    d.mapa(info["Pais"])