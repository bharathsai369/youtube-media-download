# YouTube Media Downloader

A robust Python application that leverages yt-dlp to download YouTube content in various formats and qualities. This tool supports video downloads, audio extraction, and playlist management with customizable quality settings.

## Features

- Download individual YouTube videos in multiple resolutions
- Extract audio from videos in MP3 format
- Download complete YouTube playlists
- Configurable quality settings (480p, 720p, 1080p)
- Simple command-line interface

## Requirements

- Windows 10 or Windows 11
- Python 3.9 or higher
- Active internet connection
- FFmpeg (for audio conversion)

## Installation

1. Install FFmpeg using Windows Package Manager:
   ```powershell
   winget install --id Gyan.FFmpeg -e --source winget
   ```

2. Install the required Python package:
   ```powershell
   pip install yt-dlp
   ```

## Usage

1. Run the script:
   ```powershell
   python main.py
   ```

2. Select your desired operation:
   - Option 1: Download Video
   - Option 2: Extract Audio (MP3)
   - Option 3: Download Playlist

3. Enter the YouTube URL when prompted

4. Select your preferred quality:
   - For videos: 480p, 720p, or 1080p
   - For audio: MP3 format
   - For playlists: Select quality for all videos

## Notes

- Ensure stable internet connection for large downloads
- Downloaded files will be saved in the current directory
- Audio extraction may take additional processing time