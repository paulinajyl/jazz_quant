from youtubesearchpython import VideosSearch
import yt_dlp
import ffmpeg
import pprint

# Fsearch for "Moanin by Art Blakey and the Jazz Messengers"
def search_moanin_videos():
    videos_search = VideosSearch('Moanin by Art Blakey and the Jazz Messengers Cover', limit=100)
    return videos_search.result()

def download_audio(url, output_format='mp3'):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': output_format,
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return ydl.prepare_filename(info).replace('.webm', f'.{output_format}')

# Function to cut out the solo (00:30 to 01:30 for example)
def cut_solo(audio_file, start_time, end_time, output_file):
    (
        ffmpeg
        .input(audio_file, ss=start_time, to=end_time)
        .output(output_file)
        .run()
    )

a = search_moanin_videos()
for video in a['result']:
    pprint.pprint(f"Downloading: {video['title']} - {video['link']}")
    download_audio(video['link'])
    # Cut the solo (this assumes the downloaded file is in the current directory)
    cut_solo(f"{video['title']}.mp3", "02:10", "03:30", f"{video['title']}_solo.mp3")

    pprint.pprint(video)