---
title: "YouTube MP3 Downloader"
description: "A Python script to download audio from YouTube videos in MP3 format at 320kbps using yt-dlp and ffmpeg."
imageSrc: "https://i.postimg.cc/HLT5MH2H/artem-sapegin-b18-TRXc8-UPQ-unsplash.jpg"
detailedDescription: "This Python script downloads audio from YouTube videos, converts it to MP3 at 320kbps, and saves it in an output folder with sanitized filenames. It uses yt-dlp for downloading and ffmpeg for conversion."
technologies:
  - "Python"
  - "yt-dlp"
  - "ffmpeg"
  - "Scripting"
  - "Automation"
links:
  - href: "https://github.com/deveduar/you-mp3-python"
    label: "GitHub Repository"
    svg: "GitHubIcon"
gallery:
  - "https://i.postimg.cc/HLT5MH2H/artem-sapegin-b18-TRXc8-UPQ-unsplash.jpg"
features:
  - "Efficiently download and convert multiple YouTube videos to MP3 at 320kbps."
  - "Sanitize filenames to avoid invalid characters on Windows."
  - "Organize MP3 files in the 'output' folder."
  - "Supports batch download of multiple YouTube URLs."
---

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

Make sure Python is installed, and then install the required Python packages. You can use the `requirements.txt` file provided:

```bash
pip install -r requirements.txt
```

This will install all necessary dependencies, including `yt-dlp`.

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
├── requirements.txt          # File containing the Python dependencies
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

## Disclaimer

This script is intended for educational purposes only. The author does not condone or encourage the downloading of copyrighted material without permission. It is the responsibility of the user to ensure they comply with local laws and the terms of service of YouTube or any other platform they are using the script with.

The author will not be held liable for any misuse of this tool or for any legal consequences that arise from its use.

## License

MIT License. See the LICENSE file for more details.
