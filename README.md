# YouTube MP3 Downloader

Este script permite descargar el audio de videos de YouTube en formato MP3 a 320kbps utilizando la herramienta `yt-dlp` y `ffmpeg`. Los archivos descargados se convierten y guardan en una carpeta `output` dentro del directorio del proyecto, con el nombre del archivo correspondiente al título del video, y sin caracteres no válidos para sistemas de archivos.

## Requisitos

- Python 3.x
- `yt-dlp`: Para la descarga de videos de YouTube.
- `ffmpeg`: Para convertir los archivos de audio a MP3.

## Instalación

### 1. Clona este repositorio

```bash
git clone https://github.com/tuusuario/py-mp3-you.git
cd py-mp3-you
```

### 2. Instala las dependencias

Asegúrate de tener Python instalado y luego instala `yt-dlp`:

```bash
pip install yt-dlp
```

### 3. Descarga e instala `ffmpeg`

Puedes descargar `ffmpeg` desde su [sitio oficial](https://ffmpeg.org/download.html).

Si estás usando Windows, asegúrate de agregar la ruta de `ffmpeg` a tu variable de entorno `PATH` o coloca el binario `ffmpeg.exe` en una carpeta dentro de tu proyecto y modifica la ruta en el script.

### 4. Estructura del Proyecto

El proyecto debe tener la siguiente estructura de carpetas:

```
py-mp3-you/
├── ffmpeg/                   # Carpeta que contiene el binario de ffmpeg
│   └── bin/
│       └── ffmpeg.exe         # Ejecutable de ffmpeg
├── output/                   # Carpeta donde se guardarán los MP3 descargados
├── script.py                 # Script Python para la descarga y conversión
└── README.md                 # Este archivo
```

## Uso

1. Ejecuta el script con el siguiente comando:

```bash
python script.py
```

2. El script te pedirá que ingreses las URL(s) del video(s) de YouTube separadas por comas. Por ejemplo:

```
https://www.youtube.com/watch?v=abc123, https://www.youtube.com/watch?v=xyz456
```

3. El script descargará el audio en el mejor formato disponible, lo convertirá a MP3 a 320kbps, y lo guardará en la carpeta `output` con el nombre del video, eliminando caracteres no válidos.

## Funcionalidad

- Descarga y convierte múltiples videos de YouTube en MP3 de manera eficiente.
- Sanitiza los nombres de archivo para evitar problemas con caracteres no válidos en Windows.
- Los archivos MP3 convertidos se guardan en una carpeta `output` para organización.

## Contribuciones

Si tienes alguna sugerencia o mejora, no dudes en hacer un pull request o abrir un issue.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
