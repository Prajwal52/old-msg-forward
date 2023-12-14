import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "28394784"))
    API_HASH = os.environ.get("API_HASH", "9544a3ad7d8660acbae0dcf553c808e5")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5847064573:AAGC0OerM5XtAjKjQ1JLy0jAKrkDcM3osI4")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "1966376217")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://forward:forward@cluster1.pgynkyr.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste1")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'forward_files')
    SESSION = os.environ.get("SESSION", "BQFIc8EAUSQDdKcjBhiZSxpYKqNNBL2oLyjLG9L9rBhHowjycxTfoLDo6f0-F_IUUnYM8vUw9Qw2sbEIU-UIBfJdJ3kRpItSctSEM1bPxrJdCno9Lnz0bh_0uqJrlkeBed9yJx3GBESXpM0uvDU7nZulUv-Nj75DG8mX3pZ18c7-QlveQ5jzcrC10HXxHalfpM3d95RjFBwYtn8eiKtwlq3WnDCeeavn_7S5pp0Db4tdwzSwLm5H1N1exKpLoExE4AfsDqN6W9Ya15g5LE98r-DWAOzZl2M-uUUBKyMPjjEvXd7gzuPVhvXqJqwrVPquKtBU9wnPTGO5Hu199NBC8H_5qPHxfwAAAABF5vF9AA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002127116469"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "@nish_27_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
