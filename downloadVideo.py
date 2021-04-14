def download_video(ydtChoices,ytdEntry,ytdError,choices):
    choice=ydtChoices.get()
    url=ytdEntry.get()
    try:
        yt=YouTube(url)
    except py_except.RegexMatchError:
        ytdError.config(text="This is not Youtube Url",fg="red")

    if len(url)>1:
        ytdError.config(text="")
        if choice==choices[0]:
            select=yt.streams.filter(prograssive=True,).first()
        elif choice==choices[1]:
            select=yt.streams.filter(prograssive=True,file_extension="mp4").last()
        elif choice==choices[2]:
            select=yt.streams.filter(only_audio=True).first()
        else:
            ytdError.config(text="Enter Url again")
    else:
        ytdError.config(text="don't leave it empty ")
    select.download(folderName)
    ytdError.config(text="Download is finish",fg="green")