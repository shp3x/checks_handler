from pyrogram import Client, types
from dotenv import dotenv_values

config = dotenv_values()
app = Client('my_session', api_id=config['API_ID'], api_hash=config['API_HASH'], phone_number=config['PHONE_NUMBER'])


@app.on_message()
async def get_check(client: Client, message: types.Message):

    if 't.me/send?start=' in message.text:
        code = str(message.text[message.text.find('t.me/send?start='):]).split()[0].replace('t.me/send?start=', '')
        await client.send_message(chat_id='send', text=f"/start {code}")

    elif 'http://t.me/send?start=' in message.text:
        code = str(message.text[message.text.find('http://t.me/send?start='):]).split()[0].replace('http://t.me/send?start=', '')
        await client.send_message(chat_id='send', text=f"/start {code}")


if __name__ == '__main__':
    app.run()
