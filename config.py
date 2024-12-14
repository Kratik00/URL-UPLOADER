# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "25318125")

API_HASH = os.environ.get("API_HASH", "b29fb6a928e8b8a3308f8c2d3ba9cfb0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8012673189:AAFyG4TRkK_N33ngPA-12DEhEW_Xfi6sBBI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "LP_YAGAMI") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Cluster0")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://lucifer:QGPQCl6ZFf6wHiZ7@cluster0.zmcca.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/a84c854006379d60d0a83-05f46a8d761e2827c9.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7376514183').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
