# Test de Velocidad de Internet

Este es un script en Python que permite medir la velocidad de tu conexión a Internet, incluyendo la velocidad de descarga, subida y el ping. Los resultados se guardan en un archivo JSON para su posterior revisión.

## Características

- **Medición de Velocidad de Descarga**: Mide la velocidad de descarga en Mbps.
- **Medición de Velocidad de Subida**: Mide la velocidad de subida en Mbps.
- **Medición de Ping**: Mide el ping en milisegundos.
- **Guardado de Resultados**: Los resultados se guardan automáticamente en un archivo JSON (`resultados.json`) con la fecha y hora de la prueba.

## Requisitos

Para ejecutar este script, necesitas tener instalado Python 3 y las siguientes bibliotecas:

- `speedtest-cli`
- `pyfiglet`
- `colorama`

Puedes instalar las bibliotecas necesarias usando pip:

```bash
pip install speedtest-cli pyfiglet colorama
```
## Uso
- Clona este repositorio o descarga el script `speedtest.py.`

- Ejecuta el script en tu terminal:

``` bash
python speedtest.py
```
- El script mostrará un mensaje de presentación y comenzará a medir la velocidad de tu conexión a Internet.

- Una vez completada la prueba, los resultados se mostrarán en la terminal y se guardarán en el archivo resultados.json.

## Ejemplo de Salida

```
 _____         _     ___       _                       _   
|_   _|__  ___| |_  |_ _|_ __ | |_ ___ _ __ _ __   ___| |_ 
  | |/ _ \/ __| __|  | || '_ \| __/ _ \ '__| '_ \ / _ \ __|
  | |  __/\__ \ |_   | || | | | ||  __/ |  | | | |  __/ |_ 
  |_|\___||___/\__| |___|_| |_|\__\___|_|  |_| |_|\___|\__|
                                                           

------ By LordAguaKate------

🚀 Ejecutando prueba de velocidad...

⬇️  Velocidad de descarga: 300.75 Mbps
⬆️  Velocidad de subida: 296.36 Mbps
📶 Ping: 17.172 ms

📁 Resultados guardados en 'resultados.json'
```
## Estructura del Archivo de Resultados
Los resultados se guardan en un archivo JSON (`resultados.json`) con el siguiente formato:
```
{
  "Fecha": "2023-10-05 14:30:45.123456",
  "Download_Mbps": 300.75,
  "Upload_Mbps": 296.36,
  "Ping_ms": 17.172
}
```
##
¡Gracias por usar este script! .

By LordAguaKate









