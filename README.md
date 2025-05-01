# Test de Velocidad de Internet

Este es un script en Python que permite medir la velocidad de tu conexión a Internet, incluyendo la velocidad de descarga, subida y el ping. Los resultados se guardan en archivos JSON y CSV para su posterior revisión, análisis estadístico e historial de pruebas.

## Características

- **Medición de Velocidad de Descarga**: Mide la velocidad de descarga en Mbps.
- **Medición de Velocidad de Subida**: Mide la velocidad de subida en Mbps.
- **Medición de Ping**: Mide el ping en milisegundos.
- **Historial**: Guarda cada resultado en `resultados.json` y `resultados.csv`.
- **Estadísticas**: Calcula promedio, máximo y mínimo de las mediciones guardadas.
- **Menú Interactivo**: Interfaz por consola para elegir entre realizar pruebas, ver historial, borrar datos o salir.
- **Estilo Visual Mejorado**: Usa `pyfiglet` y `colorama` para una interfaz colorida y legible.

## Requisitos

Para ejecutar este script, necesitas tener instalado Python 3 y las siguientes bibliotecas:

- `speedtest-cli`
- `pyfiglet`
- `colorama`

Puedes instalar las bibliotecas necesarias usando pip:

```bash
pip install speedtest-cli pyfiglet colorama
```

> ⚠️ **Advertencia**: Algunas versiones recientes de `speedtest-cli` están experimentando errores `403 Forbidden`. En futuras versiones, se recomienda migrar a bibliotecas alternativas como `fast-speedtest-api`.

## Uso

### En Windows

```bash
python run.py
```

### En Linux

```bash
python3 run.py
```

#### Notas para Linux:

- Asegúrate de tener `python3` y `pip3` instalados:
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip
  ```

- Instala las dependencias con:
  ```bash
  pip3 install speedtest-cli pyfiglet colorama
  ```

- Si ves errores al guardar resultados, asegúrate de tener creada la carpeta `data`:
  ```bash
  mkdir -p data
  ```

- Si quieres limpiar la pantalla entre ejecuciones, puedes agregar esta línea en el script:
  ```python
  os.system('cls' if os.name == 'nt' else 'clear')
  ```

## Ejemplo de Salida

```
 _____         _     ___       _                       _   
|_   _|__  ___| |_  |_ _|_ __ | |_ ___ _ __ _ __   ___| |_ 
  | |/ _ \/ __| __|  | || '_ \| __/ _ \ '__| '_ \ / _ \ __|
  | |  __/\__ \ |_   | || | | | ||  __/ |  | | | |  __/ |_ 
  |_|\___||___/\__| |___|_| |_|\__\___|_|  |_| |_|\___|\__|
                                                           

------ By LordAguaKate ------

🚀 Ejecutando prueba de velocidad...

🌐 Servidor: speedtest.example.com (Ciudad, País)
⬇️  Velocidad de descarga: 300.75 Mbps
⬆️  Velocidad de subida: 296.36 Mbps
📶 Ping: 17.172 ms

📁 Resultados guardados en 'resultados.json'
📁 Resultados guardados en 'resultados.csv'
```

## Estructura del Archivo de Resultados

### `resultados.json`
Cada línea representa un test en formato JSON:

```json
{
  "Fecha": "2025-04-30 14:30:45.123456",
  "Download_Mbps": 300.75,
  "Upload_Mbps": 296.36,
  "Ping_ms": 17.172
}
```

### `resultados.csv`
Archivo tabular con los mismos campos, útil para abrir con Excel o procesar con pandas.

## Créditos

By **LordAguaKate**

¡Gracias por usar este script!
