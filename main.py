import os
import re
from yt_dlp import YoutubeDL
import subprocess

# Ruta relativa a ffmpeg en tu proyecto
ffmpeg_path = os.path.join(os.getcwd(), 'ffmpeg', 'bin', 'ffmpeg.exe')

def sanitize_filename(filename):
    """
    Sanitiza el nombre del archivo para que sea compatible con sistemas de archivos.
    Remueve caracteres no permitidos en los nombres de archivos (Windows).
    """
    # Reemplaza caracteres no permitidos con guiones bajos
    return re.sub(r'[<>:"/\\|?*]', '_', filename)

def download_audio_from_youtube(url, output_path=".", filename="audio.mp3"):
    try:
        # Crear la carpeta de salida si no existe
        output_dir = os.path.join(output_path, "output")
        os.makedirs(output_dir, exist_ok=True)

        # Configuración de yt-dlp para descargar solo el mejor audio
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Usar el título del video
            'noplaylist': True,  # No descargar playlists
        }

        # Descargar el archivo de audio
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', 'audio')  # Obtener el título del video

        # Sanitizar el nombre del archivo
        sanitized_filename = sanitize_filename(video_title) + ".mp3"
        output_file = os.path.join(output_dir, sanitized_filename)

        # Ruta temporal del archivo descargado (esto dependerá del formato de salida)
        downloaded_file = os.path.join(output_dir, f"{sanitize_filename(video_title)}.webm")

        # Convertir a MP3 usando ffmpeg
        subprocess.run([ffmpeg_path, '-i', downloaded_file, '-b:a', '320k', output_file])

        # Eliminar el archivo temporal
        os.remove(downloaded_file)

        print(f"Descarga y conversión completadas: {output_file}")

    except Exception as e:
        print("Error:", e)

def main():
    urls_input = input("Ingresa las URL(s) del video de YouTube separadas por comas: ")
    urls = [url.strip() for url in urls_input.split(",")]  # Separar las URLs por comas y quitar espacios
    
    for url in urls:
        download_audio_from_youtube(url)  # Descargar y convertir cada URL

if __name__ == "__main__":
    main()
