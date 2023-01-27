import asyncio
import argparse
from functions import get_list_currencies, convert_currencies, history_quotes

parser_symbols = argparse.ArgumentParser(description='Get list of currencies')
parser_symbols.add_argument('symbols')
args_symbols = parser_symbols.parse_args()

parser_convert = argparse.ArgumentParser(description="Convert currencies")
parser_convert.add_argument('convert', help='Convert command', default='convert')
parser_convert.add_argument('FROM', help='From currency', default='from')
parser_convert.add_argument('from_currency', type=str, help='From currency')
parser_convert.add_argument('TO', help='To currency', default='to')
parser_convert.add_argument('to_currency', type=str, help='To currency')
parser_convert.add_argument('amount', type=float, help='Amount', default=1.00)
args_convert = parser_convert.parse_args()

parser_history = argparse.ArgumentParser(description="Historical rates")
parser_history.add_argument('history', help='History command', default='history')
parser_history.add_argument('FROM', help='From currency', default='from')
parser_history.add_argument('from_currency', type=str, help='From currency')
parser_history.add_argument('TO', help='To currency', default='to')
parser_history.add_argument('to_currency', type=str, help='To currency')
parser_history.add_argument('date_from', type=str, help='Date from')
# parser_history.add_argument('date_to', type=str, help='Date to')
args_history = parser_history.parse_args()


async def main():
    if args_symbols.symbols == 'symbols':
        await get_list_currencies()

    if args_convert.convert == 'convert' and args_convert.FROM == 'from' and args_convert.TO == 'to':
        await convert_currencies(args_convert.from_currency,
                                 args_convert.to_currency,
                                 args_convert.amount)

    if args_history.history == 'history' and args_history.FROM == 'from' and args_history.TO == 'to':
        await history_quotes(args_history.from_currency,
                                 args_history.to_currency,
                                 args_history.date_from)

asyncio.run(main())
