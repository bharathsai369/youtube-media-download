import os
import subprocess

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print("✅ FFmpeg is already installed.")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚙️ Installing FFmpeg via winget...")
        subprocess.run(["winget", "install", "--id", "Gyan.FFmpeg", "-e", "--source", "winget"], check=True)

def install_ytdlp():
    try:
        __import__('yt_dlp')
        print("✅ yt-dlp is already installed.")
    except ImportError:
        print("⚙️ Installing yt-dlp...")
        subprocess.run(["pip", "install", "--upgrade", "yt-dlp"], check=True)

def main():
    print("\n📺 YouTube Downloader (yt-dlp)")
    print("Choose what you want to download:\n1. Video\n2. Audio\n3. Playlist\n")
    choice = input("➡️ Enter choice (1/2/3): ").strip()

    url = input("🔗 Enter YouTube URL: ").strip()
    if not url:
        print("❌ URL cannot be empty.")
        return

    # Set download quality
    quality = input("🎞️ Choose quality (480/720/1080): ").strip() or "720"

    if choice == "1":  # Video
        format_code = f"bv*[height<={quality}]+ba[ext=m4a]/b[height<={quality}]"
        out_format = "mp4"
    elif choice == "2":  # Audio only
        format_code = "bestaudio"
        out_format = "mp3"
    elif choice == "3":  # Playlist (Video)
        format_code = f"bv*[height<={quality}]+ba[ext=m4a]/b[height<={quality}]"
        out_format = "mp4"
    else:
        print("❌ Invalid choice.")
        return

    cmd = [
        "yt-dlp",
        "-f", format_code,
        "--merge-output-format", out_format,
        "--embed-thumbnail",
        "--add-metadata",
        "-o", "%(title)s.%(ext)s",
        url
    ]

    print("\n📥 Downloading, please wait...\n")
    subprocess.run(cmd)
    print("\n✅ Download complete!")

if __name__ == "__main__":
    check_ffmpeg()
    install_ytdlp()
    main()
