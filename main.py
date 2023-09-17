import requests


api_key = 'b6f26f2cd225326a0a6824803baa41da'

Parameters = {
    "lat": 22.5726,
    "lon": 88.3639,
    "appid": api_key,
}


def telegram_bot_sendtext(bot_message):

    bot_token = "6086626203:AAEbx2bN91AgMxhtU6ucETdgqLvZCkElKIc"
    bot_chatID = "1412740519"
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response1 = requests.get(send_text)

    return response1.json()


response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=Parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for i in range(12):
    if weather_data["list"][i]["weather"][0]["id"] < 700:
        will_rain = True
        break

if will_rain:
    telegram_bot_sendtext("It will rain. Bring your Umbrella☂️")
