from datetime import date, datetime, timedelta
from aiohttp import ClientSession


async def get_list_currencies():
    """Получение списка валют"""
    url = f'http://api.exchangerate.host/latest'

    async with ClientSession() as session:
        async with session.get(url=url) as response:
            result_json = await response.json()
            for keys, values in result_json["rates"].items():
                print(keys)


async def convert_currencies(from_currency: str, to_currency: str, amount: float = 1.00) -> str:
    """Конвертация валют"""

    url = f'http://api.exchangerate.host/convert?from={from_currency.upper()}&to={to_currency.upper()}&ammount={amount}'
    async with ClientSession() as session:
        async with session.get(url=url) as response:
            result_json = await response.json()
            amount = result_json["query"]["amount"] * amount
            result = result_json["result"] * amount
            print(f'{amount} {result_json["query"]["from"]} to {result_json["query"]["to"]} = {result} on date {result_json["date"]}')


async def history_quotes(from_currency: str, to_currency: str, start_date):
    """История котировок"""
    start_date = datetime(year=int(start_date[0:4]), month=int(start_date[4:6]), day=int(start_date[6:8])).strftime("%Y-%m-%d")
    end_date = datetime.today().strftime("%Y-%m-%d")
    start_date_dt = datetime.strptime(start_date, ("%Y-%m-%d"))
    end_date_dt = datetime.strptime(end_date, ("%Y-%m-%d"))
    
    url = f'https://api.exchangerate.host/{start_date}'

    list_currencies = []
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()
    list_currencies.append(from_currency.upper())
    list_currencies.append(to_currency.upper())
        
    async with ClientSession() as session:
        async with session.get(url=url) as response:
            result_json = await response.json()
            for keys in result_json["rates"].items():
                while start_date_dt <= end_date_dt:
                    start_date_str = start_date_dt.strftime("%Y-%m-%d")
                    for item in list_currencies:
                        print(f'{start_date_dt} {item} {result_json["rates"][item]}')
                    start_date_dt += timedelta(days=1)