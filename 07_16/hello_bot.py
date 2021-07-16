import requests

TOKEN='1748217015:AAF_NyjTXt1z9wwE6RavxrHcaBSBtVW5JFo'
APP_URL=f'https://api.telegram.org/bot{TOKEN}'

update_url=f'{APP_URL}/getUpdates'
response=requests.get(update_url).json()
chat_id=response["result"][0]["message"]["from"]["id"]
text='스타트캠프 끝!'
message_url=f'{APP_URL}/sendMessage?chat_id={chat_id}&text={text}'
requests.get(message_url)

