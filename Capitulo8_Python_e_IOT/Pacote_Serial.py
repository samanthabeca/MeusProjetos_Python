#Dica: para utilizar o pacote "serial" no Ubuntu 22.04, instalar o pacote "python3-serial" com sudo apt install python3-serial
# Link para Download da Arduino IDE: https://www.arduino.cc/en/software
# Ou link direto do download para Linux: https://downloads.arduino.cc/arduino-ide/arduino-ide_2.1.1_Linux_64bit.zip

import serial
conexao = serial.Serial('/dev/ttyUSB0', 115200)

#Se fosse no Windows, a porta serial seria COM3:
import serial
conexao = serial.Serial('COM3', 115200, timeout=0.5)