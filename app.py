from pyrogram import Client, filters


api_id = 3335796
api_hash = "138b992a0e672e8346d8439c3f42ea78"
bot_token = "5088657122:AAGXARfg6sSX1p1ge876jknkrJizwH959b4"

plugins = dict(root="plugins")

app = Client(
      "uploader",
      api_id=api_id,
      api_hash=api_hash,
      bot_token=bot_token,
      plugins=plugins )


app.run()
