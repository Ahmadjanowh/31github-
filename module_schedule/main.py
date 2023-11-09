# Модуль shedule 
# pip install schedule
# pip install requests
import schedule
import requests

def greeting():
    todos_dict = {
        '08:00' : 'Drink coffe',
        '11:00' : 'Work meeting',
        '23:00' : 'Hack the Planet!'
    }

    print("Day's tasks ")
    for k,v in todos_dict.items():
        print(f"{k} : {v}")

    # Получаем курс биткоина с API 
    response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
    data = response.json()
    btc_price = f"BTC: {round(data.get('btc_usd').get('last'),2)}$\n"
    print(btc_price)
    


def main():
    # greeting()

    # schedule.every(4).seconds.do(greeting) # Каждый 4 секунд 
    # schedule.every(4).minutes.do(greeting) # Каждый 5 минут 
    # schedule.every().hours.do(greeting) # Каждый час 

    schedule.every().day.at('19:41').do(greeting) # Каждый день по опроделоннному вермени 
    schedule.every().thursday.do(greeting) # Определонный день 
    schedule.every().friday.at('23:01').do(greeting) # Опрежелонный день опроделонная время 

    while True:
        schedule.run_pending()
if __name__ == '__main__':
    main()
