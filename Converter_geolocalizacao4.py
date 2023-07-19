from geopy.geocoders import Nominatim #Pacote externo geopy, Biblioteca geocoders, Classe Nominatim
from Capitulo3_Funcoes.Funcoes_JSON import ler_arquivo, gravar_arquivo #Pacote Capitulo3_Funcoes, Biblioteca Funcoes_JSON, Métodos ler_arquivo e gravar_arquivo

geolocator = Nominatim(user_agent="wazeyes") # Nome do seu aplicativo

location = geolocator.geocode("Avenida Paulista, 100 Sao Paulo")

print(geolocator.geocode("Avenida Paulista, 100 Sao Paulo"))
print((location.latitude, location.longitude))