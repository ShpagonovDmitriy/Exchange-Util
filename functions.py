from datetime import datetime, timedelta
from aiohttp import ClientSession

async def get_list_currencies(*currencies):
    """Получение списка валют. Выводятся валюты и их курс"""
    url = f'http://api.exchangerate.host/latest'
    
    if currencies:
        list_currencies = [i.upper() for i in currencies]
    
        async with ClientSession() as session:
            async with session.get(url=url) as response:
                result_json = await response.json()
                for item in list_currencies:
                    print(item, result_json["rates"][item])
       
    else:        
        async with ClientSession() as session:
            async with session.get(url=url) as response:
                result_json = await response.json()
                for keys, values in result_json["rates"].items():
                    print(keys, values)


async def convert_currencies(from_currency: str, to_currency: str, amount: float = 1.00) -> str:
    """Конвертация валют"""
    url = f'http://api.exchangerate.host/convert?from={from_currency.upper()}&to={to_currency.upper()}&ammount={amount}'
    async with ClientSession() as session:
        async with session.get(url=url) as response:
            result_json = await response.json()
            print(f'{result_json["query"]["amount"]} {result_json["query"]["from"]} to {result_json["query"]["to"]} = {result_json["result"]} on date {result_json["date"]}')


async def history_quotes(from_currency: str, to_currency: str, start_date, end_date):
    """История котировок"""
    start_date = datetime(year=int(start_date[0:4]), month=int(start_date[4:6]), day=int(start_date[6:8])).strftime("%Y-%m-%d")
    end_date = datetime(year=int(end_date[0:4]), month=int(end_date[4:6]), day=int(end_date[6:8])).strftime("%Y-%m-%d")
    start_date_dt = datetime.strptime(start_date, ("%Y-%m-%d"))
    end_date_dt = datetime.strptime(end_date, ("%Y-%m-%d"))
    
    url = f'https://api.exchangerate.host/timeseries?start_date={start_date}&end_date={end_date}'

    list_currencies = []
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    list_currencies.append(from_currency.upper())
    list_currencies.append(to_currency.upper())
        
    async with ClientSession() as session:
        async with session.get(url=url) as response:
            result_json = await response.json()
            for keys in result_json["rates"][start_date].items():
                while start_date_dt <= end_date_dt:
                    start_date_str = start_date_dt.strftime("%Y-%m-%d")
                    for item in list_currencies:
                        print(f'{start_date_dt} {item} {result_json["rates"][start_date_str][item]}')
                    start_date_dt += timedelta(days=1)
