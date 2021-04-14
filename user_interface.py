import tkinter as tk
from tkinter import ttk
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps

import controller.locationfile as cl
import controller.video_downlodar as cvd

def display_gui():
  '''write description about what the function works for'''

  root = tk.Tk()
  root.title("Youtube dowloader")
  root.geometry("800x400")
  root.columnconfigure(0, weight = 1)

  # ytdLabel 
  ytdLabel = tk.Label(root, text = "Enter the URL of the Video", font = ("jost", 15))
  ytdLabel.grid()

  # Entry Box
  ytdEntryVar = tk.StringVar()
  ytdEntry = tk.Entry(root, width = 50, textvariable = ytdEntryVar)
  ytdEntry.grid()

  # Url Error Msg
  ytdError = tk.Label(root, text = "", fg = 'red')
  ytdError.grid()

  # Save file
  saveLabel = tk.Label(root, text = "Save the Video File", font = ("jost", 15, "bold"))
  saveLabel.grid()

  # Location Error Msg
  locationError = tk.Label(root,text = "",fg = 'red')
  locationError.grid()

  # button save file
  saveEntry = tk.Button(root, bg = "red", text = "Choose Path", command = lambda:cl.open_location(locationError))
  saveEntry.grid()

  # Type video or audio
  ydtQuality = tk.Label(root, text = "Select type")
  ydtQuality.grid()

  # choice
  choices = ["720p", "144p", "Only Audio"]

  # combobox
  ydtchoices = ttk.Combobox(root, values = choices)
  ydtchoices.grid()

  # download button
  downloadbtn = tk.Button(root, text = "Download", command = lambda:cvd.download_video(ydtchoices, ytdEntry, ytdError, choices))
  downloadbtn.grid()

  # pycoders
  developerTeam = tk.Label(root, text = "Pycoders")
  developerTeam.grid()

  #pymongo read
  client = pymongo.MongoClient("mongodb://kbc:12345@kbc1-shard-00-00.3pmda.mongodb.net:27017,kbc1-shard-00-01.3pmda.mongodb.net:27017,kbc1-shard-00-02.3pmda.mongodb.net:27017/sample_airbnb?ssl=true&replicaSet=atlas-vdbv3h-shard-0&authSource=admin&retryWrites=true&w=majority")
  client.sample_airbnb.list_collection_names()
  client['sample_airbnb'].list_collection_names()
  client.sample_airbnb.listingsAndReviews.count_documents({})
  a = client.sample_airbnb.listingsAndReviews.find({"minimum_nights": "2"}, {"_id": 1, "minimum_nights": "2"}).limit(3)
  a1=dumps(a)
  mongolabelread=tk.Label(root, text="Mongo Read")
  mongolabelread.grid()
  mongolabelread1=tk.Label(root, text=a1)
  mongolabelread1.grid()

  #pymongo delete
  client.sample_airbnb.listingsAndReviews.delete_one({"minimum_nights": "15"})
  c1=client.sample_airbnb.listingsAndReviews.delete_one({"minimum_nights": "15"}).deleted_count

  mongolabeldelete=tk.Label(root, text="Mongo Delete: minimum nights is 14")
  mongolabeldelete.grid()
  mongolabeldelete1=tk.Label(root, text=c1)
  mongolabeldelete1.grid()


  root.mainloop()