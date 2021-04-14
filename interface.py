import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
import pytube.exceptions as py_except
from controller import downloadVideo
from controller import location
from controller import main
import pymongo
from pymongo import MongoClient

connect=MongoClient('mongodb+srv://bulent:220525525@cluster0.aojnh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db=connect['bulent']
collection=db['PyCoders']

if  __name__ == '__main__':
    controller.main()
