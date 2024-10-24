import os
import sys
import yt_dlp as youtube_dl
from tkinter import Tk
from tkinter.filedialog import askdirectory
from termcolor import colored

def choose_video_quality(formats):
    print(colored("\nMevcut Kalite Seçenekleri:", attrs=['underline']))
    for i, format in enumerate(formats):
        print(f"[{i}] {format['format']} - {format['ext']}")
    
    choice = input(colored("\nLütfen istediğiniz kalite numarasını girin: ", "yellow"))
    while not choice.isdigit() or int(choice) < 0 or int(choice) >= len(formats):
        choice = input("Geçerli bir numara girin: ")
    return formats[int(choice)]

def choose_download_location():
    root = Tk()
    root.attributes('-topmost', True)  # Tkinter penceresini en öne getir
    root.withdraw()  # Tkinter penceresini gizle
    location = askdirectory(title="Videoyu indirmek istediğiniz klasörü seçin")
    root.destroy()  # Tkinter penceresini kapat
    if not location:
        print("Klasör seçilmedi, geçerli klasörü kullanıyorum.")
        location = os.getcwd()
    return location

def main():
    url = input("YouTube video URL'sini girin: ")
    try:
        ydl_opts = {}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])
    except youtube_dl.utils.DownloadError as e:
        print(f"Video mevcut değil veya URL yanlış. Lütfen geçerli bir URL girin: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"URL çözülemedi, lütfen geçerli bir URL girin: {e}")
        sys.exit(1)

    chosen_format = choose_video_quality(formats)
    download_location = choose_download_location()

    print("\nVideo indiriliyor...")
    try:
        ydl_opts = {
            'format': f"{chosen_format['format_id']}+bestaudio",
            'outtmpl': os.path.join(download_location, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }]
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\nVideo başarıyla indirildi: {download_location}")
    except Exception as e:
        print(f"\nVideo indirilemedi: {e}")

if __name__ == "__main__":
    main()
