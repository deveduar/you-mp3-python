# YouTube MP3 Downloader

This script allows you to download audio from YouTube videos in MP3 format at 320kbps using the `yt-dlp` tool and `ffmpeg`. The downloaded files are converted and saved in an `output` folder within the project directory, with the filename corresponding to the video title, while removing invalid characters for file systems.

## Requirements

- Python 3.x
- `yt-dlp`: For downloading YouTube videos.
- `ffmpeg`: For converting audio files to MP3.

## Installation

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/py-mp3-you.git
cd py-mp3-you
```

### 2. Install dependencies

Make sure Python is installed, and then install `yt-dlp`:

```bash
pip install yt-dlp
```

### 3. Download and install `ffmpeg`

You can download `ffmpeg` from the [official website](https://ffmpeg.org/download.html).

If you are using Windows, make sure to add the `ffmpeg` path to your `PATH` environment variable, or place the `ffmpeg.exe` binary in a folder within your project and modify the path in the script.

### 4. Project Structure

The project should have the following folder structure:

```
py-mp3-you/
├── ffmpeg/                   # Folder containing the ffmpeg binary
│   └── bin/
│       └── ffmpeg.exe         # ffmpeg executable
├── output/                   # Folder where the downloaded MP3s will be saved
├── script.py                 # Python script for downloading and converting
└── README.md                 # This file
```

## Usage

1. Run the script with the following command:

```bash
python script.py
```

2. The script will ask you to enter the YouTube video URL(s) separated by commas. For example:

```
https://www.youtube.com/watch?v=abc123, https://www.youtube.com/watch?v=xyz456
```

3. The script will download the audio in the best available format, convert it to MP3 at 320kbps, and save it in the `output` folder with the video title, removing invalid characters.

## Features

- Efficiently downloads and converts multiple YouTube videos to MP3.
- Sanitizes filenames to avoid issues with invalid characters on Windows.
- The converted MP3 files are organized and saved in an `output` folder.

## Contributions

If you have suggestions or improvements, feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
