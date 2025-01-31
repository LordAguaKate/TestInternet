# Test Internet - Prueba de Velocidad de Internet

Este programa permite realizar una prueba de velocidad de conexión a internet, midiendo la velocidad de descarga, subida y el ping, y guarda los resultados en un archivo JSON.

## Características
- **Velocidad de descarga:** Mide la velocidad de descarga en Mbps.
- **Velocidad de subida:** Mide la velocidad de subida en Mbps.
- **Ping:** Mide el tiempo de respuesta del servidor en milisegundos (ms).
- **Guardar resultados:** Los resultados de la prueba se guardan en un archivo `resultados.json` junto con la fecha y hora.

## Requisitos

Para ejecutar este programa, asegúrate de tener instaladas las siguientes dependencias:

- `speedtest-cli`: Para realizar las pruebas de velocidad.
- `pyfiglet`: Para generar arte ASCII en la terminal.
- `colorama`: Para añadir colores a la salida en la terminal.
- `json`: Para guardar los resultados en formato JSON.
- `datetime`: Para obtener la fecha y hora de la prueba.

Instala las dependencias utilizando `pip` si no las tienes:

```bash
pip install speedtest-cli pyfiglet colorama
