def open_location(locationError):
    global folderName
    folderName=tk.filedialog.askdirectory()
    if len(folderName)>1:
        locationError.config(text=folderName,fg="green")
    else:
        locationError.config(text="Please choose correct path", fg="green")

