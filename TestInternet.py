import speedtest
import json
import pyfiglet
from datetime import datetime
from colorama import Fore, Style, init

# Convierte bits por segundo a Mbps.
def convert_mbps(value):
    return round(value / 10 ** 6, 2)

#Presentacion del programa
font = pyfiglet.figlet_format('Test Internet')
print(Fore.RED+font)
print(Fore.RED + "------ By LordAguaKate------")
def velocidad_test():
    #Mensaje sobre la ejecución
    print(Fore.CYAN + "\n🚀 Ejecutando prueba de velocidad...\n")

    test = speedtest.Speedtest()
    test.get_best_server()

    # Mide la velocidad de descarga
    down_speed = convert_mbps(test.download())
    print(Fore.GREEN + f"⬇️  Velocidad de descarga: {down_speed} Mbps")

    # Mide la velocidad de subida
    up_speed = convert_mbps(test.upload())
    print(Fore.YELLOW + f"⬆️  Velocidad de subida: {up_speed} Mbps")

    # Mide el ping
    ping = test.results.ping
    print(Fore.RED + f"📶 Ping: {ping} ms")

    # Guardar los resultados
    save_results(down_speed, up_speed, ping)


def save_results(down_speed, up_speed, ping):
    #Guarda los resultados en un archivo JSON con la fecha y hora
    results = {
        "Fecha": str(datetime.now()),
        "Download_Mbps": down_speed,
        "Upload_Mbps": up_speed,
        "Ping_ms": ping
    }

    with open("resultados.json", "a") as file:
        json.dump(results, file)
        file.write("\n")

    print(Fore.BLUE + "\n📁 Resultados guardados en 'resultados.json'" + Style.RESET_ALL)


if __name__ == "__main__":
    velocidad_test()
