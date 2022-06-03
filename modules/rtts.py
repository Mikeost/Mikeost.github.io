# Russian tts for Friendly-telegram and Uniborg: .r
# By @m1k30st
# Test-build ID: 8

import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="r ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
        user_msg = """{}""".format(event.pattern_match.group(1))
        self_mess = True
        if not user_msg:
            await event.edit("Вы должны или написать что-нибудь, или ответить на что-нибудь")
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        self_mess = False
        sender = reply_message.sender
        if not reply_message.text:
            await event.edit("```Ты должен ответить на текст```")
            return
    chat = "@aleksobot"
    await event.edit("```Скачивание вирусов на устройства ;)```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=616484527))
              if not self_mess:
                  await event.client.forward_messages(chat, reply_message)	
              else: 
                  await event.client.send_message(chat, user_msg)	
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Разблокируй @aleksobot, ибо ничего не произойдёт```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("```А сейчас я не могу переслать. Разрешишь?```")
          else: 	 
             await event.delete()
             alexoNewMessage =  await event.client.send_message(event.chat_id, response.message) 
             await event.client.edit_message(event.chat_id, alexoNewMessage, '.')
             await event.client.send_message(event.chat_id, "```Доп. модули\n```"  + "                  ▬ @mikeostdev ▬\n" + "                ▬ www.mikeost.com ▬") 

	
