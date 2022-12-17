from pytube import YouTube

def Download(link):
    try:
        youtubeObject = YouTube(link)
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        youtubeObject.download()
    except:
        return "An error has occurred"
    return "Download is completed successfully"

