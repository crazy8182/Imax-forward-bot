from os import environ 

class Config:
    API_ID = environ.get("API_ID", "26741021")
    API_HASH = environ.get("API_HASH", "7c5af0b88c33d2f5cce8df5d82eb2a94")
    BOT_TOKEN = environ.get("BOT_TOKEN", "") 
    BOT_SESSION = environ.get("BOT_SESSION", "vegamoviesforwordbot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://devashibambhava0:devashibambhava0@cluster0.ux6amy9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6859451629').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
