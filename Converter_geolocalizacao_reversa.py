from geopy.geocoders import Nominatim #pacote externo geopy, biblioteca geocoders e classe Nominatim
geolocator = Nominatim(user_agent="wazeyes")

latitude = float(input("Digite a latitude ...: "))
longitude = float(input("Digite a longitude .: "))

resultado = str(geolocator.reverse(f"{latitude}, {longitude}")).split(",")
#exemplo de latitude e longitude: -23.5702973, -46.6456683

if resultado[0] != 'None':
    print("Endereço completo .: ", resultado)
    print("Rua ...............: ", resultado[1])
    print("Número ............: ", resultado[0])
    print("Bairro ............: ", resultado[2])    