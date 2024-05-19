from pyrogram import Client, filters
from pyrogram.enums.ChatAction import TYPING
from plugins import query, admin

@Client.on_message(filters.private & filters.user(admin) & filters.command(&quothelp&quot))
async def help_message(client, message):
    chat_id = message.chat.id
    help_message = &quot&quot&quot⚡️ **اپشن های موجود** ⚡️ 
       \n☔️ اضافه کردن پیام به ربات با کامند     /add_msg
        \n☔️ حذف کردن پیام از ربات با کامند       /del_msg
        \n☔️ نمایش جمسملات موجود با کامند       /show_msg
         \n☔️ نمایش وضعیت ربات     /info
         \n☔️ چک کردن وضعیت ربات با کامند      /status
         \n☔️ فوروارد کردن پیام       /forward
         \b☔️ جوین شدن داخل گروه مورد نظر     /join_chat
         \n☔️ ست کردن پیام بعد از جوین شدن ربات در گروه       /join_msg
         \n.
    &quot&quot&quot
    await client.send_chat_action(chat_id=chat_id, action=TYPING)
    await message.reply(text=help_message)
