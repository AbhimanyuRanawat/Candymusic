# ๐ฌ AlishaSupport ๐ฅ Itz_VeNom_xD โจ

import asyncio

from config import SUDO_USERS

from config import PMPERMIT

from pyrogram import Client

from pyrogram import filters

from pyrogram.types import Message

from callsmusic import client as USER

PMSET =True

pchats = []

@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)

async def pmPermit(client: USER, message: Message):

    if PMPERMIT == "ENABLE":

        if PMSET:

            chat_id = message.chat.id

            if chat_id in pchats:

                return

            await USER.send_message(

                message.chat.id,

                "**๐๐ข ๐๐ฒ๐ฎ๐ฌ๐ฌ :) <๐\n๐๐ง๐ฒ ๐๐๐ฅ๐ฉ ๐๐ฆ ๐๐ฒ ๐๐ฐ๐๐๐ญ ๐\n๐๐๐ฌ๐ญ๐๐ซ ๐ธ :- [โ-๐๐ข๐ฌ๐ฌ'๐๐๐ง๐๐ฒ๐ฌ ](https://t.me/Candy_626) โค๏ธ\n**",

            )

            return

    

@Client.on_message(filters.command(["/pmpermit"]))

async def bye(client: Client, message: Message):

    if message.from_user.id in SUDO_USERS:

        global PMSET

        text = message.text.split(" ", 1)

        queryy = text[1]

        if queryy == "on":

            PMSET = True

            await message.reply_text("**๐ฅ PM-Permit๐ค Activated โจ ...**")

            return

        if queryy == "off":

            PMSET = None

            await message.reply_text("**๐ฅ PM-Permit๐ค De-Activated โจ ...**")

            return

@USER.on_message(filters.text & filters.private & filters.me)        

async def autopmPermiat(client: USER, message: Message):

    chat_id = message.chat.id

    if not chat_id in pchats:

        pchats.append(chat_id)

        await message.reply_text("**๐ฅ Auto ๐ค Approved โจ ...**")

        return

    message.continue_propagation()    

    

@USER.on_message(filters.command("a", [".", ""]) & filters.me & filters.private)

async def pmPermiat(client: USER, message: Message):

    chat_id = message.chat.id

    if not chat_id in pchats:

        pchats.append(chat_id)

        await message.reply_text("**๐ฅ Approved โจ ...**")

        return

    message.continue_propagation()    

    

@USER.on_message(filters.command("da", [".", ""]) & filters.me & filters.private)

async def rmpmPermiat(client: USER, message: Message):

    chat_id = message.chat.id

    if chat_id in pchats:

        pchats.remove(chat_id)

        await message.reply_text("**๐ฅ Dis-Approved โจ ...**")

        return

    message.continue_propagation()
