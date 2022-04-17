from os import getenv

# TELEGRAM
OWNER = int(getenv('bot_token'))
if OWNER is None:
    raise Exception("Por favor configura tu Bot Token) 

API_ID = int(getenv('tg_admin_user'))
if API_ID is None:
    raise Exception("Por favor configura el Admin de la cuenta ") 
