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
    SESSION = os.environ.get("SESSION", "BQBI8lOKGqpKcIlLbVNMxuJvVKNGr3Lmg-BeOI_ccw6aIYFr5hNYB3GiMiEqsC5hogkHrTJjIJX04kx2V4qQyp2frKYKVwe8SmtLqzTOmINQn7Y6nQAE9X2uyod7sKWPM5y6ghut1WmZv3gZzDrgf3uaNvj_fYpfcSCLouJHlfr92mK7Qbpxq--J3-2smrhQFAqc8wghQKXZw6bUpRE_3EiqaqhjyfSMNzIc1g8fVt3Nkf5Y2ZS4SfY0b8SzuiZNaDGSZcra3syASG-LC7vCI36B0YLYI7FbXRurMACBBh5f1O_YQaMNQsp4D-wDpbplmR1gpgU0vKq7FSf_zyS_5LjlRebxfQA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001927033569"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "@nish_27_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
