import speedtest
import json
import csv
import pyfiglet
from datetime import datetime
from colorama import Fore, Style, init
import os

init(autoreset=True)

def convert_mbps(value):
    return round(value / 10 ** 6, 2)

def mostrar_encabezado():
    font = pyfiglet.figlet_format('Test Internet')
    print(Fore.RED + font)
    print(Fore.RED + "------ By LordAguaKate ------")

def velocidad_test():
    print(Fore.CYAN + "\n🚀 Ejecutando prueba de velocidad...\n")

    test = speedtest.Speedtest()
    server = test.get_best_server()

    print(Fore.MAGENTA + f"🌐 Servidor: {server['host']} ({server['name']}, {server['country']})")

    down_speed = convert_mbps(test.download())
    print(Fore.GREEN + f"⬇️  Velocidad de descarga: {down_speed} Mbps")

    up_speed = convert_mbps(test.upload())
    print(Fore.YELLOW + f"⬆️  Velocidad de subida: {up_speed} Mbps")

    ping = test.results.ping
    print(Fore.RED + f"📶 Ping: {ping} ms")

    save_results(down_speed, up_speed, ping)
    save_results_csv(down_speed, up_speed, ping)

def save_results(down_speed, up_speed, ping):
    results = {
        "Fecha": str(datetime.now()),
        "Download_Mbps": down_speed,
        "Upload_Mbps": up_speed,
        "Ping_ms": ping
    }

    with open("../data/resultados.json", "a") as file:
        json.dump(results, file)
        file.write("\n")

    print(Fore.BLUE + "📁 Resultados guardados en 'resultados.json'")

def save_results_csv(down_speed, up_speed, ping):
    file_exists = os.path.isfile("../data/resultados.csv")

    with open("../data/resultados.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Fecha", "Download_Mbps", "Upload_Mbps", "Ping_ms"])
        writer.writerow([datetime.now(), down_speed, up_speed, ping])

    print(Fore.CYAN + "📁 Resultados guardados en 'resultados.csv'")

def mostrar_historial():
    if not os.path.exists("../data/resultados.json"):
        print(Fore.YELLOW + "⚠️ No hay historial disponible.")
        return

    velocidades = []
    with open("../data/resultados.json", "r") as file:
        for line in file:
            try:
                data = json.loads(line)
                velocidades.append(data)
            except json.JSONDecodeError:
                continue

    if not velocidades:
        print(Fore.YELLOW + "⚠️ Historial vacío o corrupto.")
        return

    downloads = [r["Download_Mbps"] for r in velocidades]
    uploads = [r["Upload_Mbps"] for r in velocidades]
    pings = [r["Ping_ms"] for r in velocidades]

    print(Fore.GREEN + f"\n📊 Estadísticas del historial:")
    print(Fore.GREEN + f"→ Pruebas realizadas: {len(velocidades)}")
    print(Fore.GREEN + f"→ Promedio descarga: {sum(downloads)/len(downloads):.2f} Mbps")
    print(Fore.GREEN + f"→ Promedio subida: {sum(uploads)/len(uploads):.2f} Mbps")
    print(Fore.GREEN + f"→ Promedio ping: {sum(pings)/len(pings):.2f} ms")
    print(Fore.GREEN + f"→ Máxima descarga: {max(downloads)} Mbps")
    print(Fore.GREEN + f"→ Mínima descarga: {min(downloads)} Mbps")

def borrar_resultados():
    if os.path.exists("../data/resultados.json"):
        os.remove("../data/resultados.json")
    if os.path.exists("../data/resultados.csv"):
        os.remove("../data/resultados.csv")
    print(Fore.RED + "🗑️ Archivos de resultados eliminados.")

def menu():
    while True:
        print(Fore.YELLOW + "\n--- MENÚ ---")
        print("1. Realizar prueba de velocidad")
        print("2. Mostrar historial y estadísticas")
        print("3. Borrar historial")
        print("4. Salir")

        opcion = input(Fore.CYAN + "Selecciona una opción: ")

        if opcion == "1":
            velocidad_test()
        elif opcion == "2":
            mostrar_historial()
        elif opcion == "3":
            borrar_resultados()
        elif opcion == "4":
            print(Fore.GREEN + "👋 ¡Hasta luego!")
            break
        else:
            print(Fore.RED + "❌ Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    mostrar_encabezado()
    menu()
