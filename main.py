def main():
    root=tk.Tk()
    root.title("Youtube Downloader")
    root.geometry("800x400")
    root.columnconfigure(0,weight=1)

    #ytdLabel
    ytdLabel=tk.Label(root,text="Enter your URL")
    ytdLabel.grid()

    #Entry box
    ytdEntryVar=tk.StringVar
    ytdEntry=tk.Entry(root,width=50,textvariable=ytdEntryVar)
    ytdEntry.grid()

    #Url error msg
    ytdError=tk.Label(root,text="",fg="red")
    ytdError.grid()

    #save file
    saveLabel=tk.Label(root,text="Save the file")
    saveLabel.grid()

    # Location error msg
    locationError=tk.Label(root,text="",fg="red")
    locationError.grid()

    # button save file
    saveEntry = tk.Button(root,bg="red",text="Choose Path", command=open_location(locationError))
    saveEntry.grid()

    #type video or audio
    ytdQuality= tk.Label(root,text="Select type")
    ytdQuality.grid()

    #Combobox
    choices=["720p","144p","Only Audio"]
    ydtChoices=ttk.Combobox(root,values=choices)
    ydtChoices.grid()

    #download button
    downloadbtn=tk.Button(root,text="Download",command= download_video(ydtChoices,ytdEntry,ytdError,choices))
    downloadbtn.grid()

    # pycoders
    pycodersTeam = tk.Label(root, text="pycoders")
    pycodersTeam.grid()

    root.mainloop()


