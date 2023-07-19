from geopy.geocoders import Nominatim
from Capitulo3_Funcoes.Funcoes_JSON import ler_arquivo, gravar_arquivo

geolocator = Nominatim(user_agent="wazeyes") # Nome do seu aplicativo

location = geolocator.geocode("Rua Capitão Alberto Mendes Júnior 544, Joquei Club, Marilia-SP")

print(location.address)
print((location.latitude, location.longitude))