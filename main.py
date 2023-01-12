import asyncio
import argparse

from functions import get_list_currencies, convert_currencies, history_quotes

loop = asyncio.get_event_loop()

# a = get_list_currencies()
# b = convert_currencies('usd', 'eur', 1)
# c = history_quotes('usd', 'eur', '20220101', '20220110')

if __name__ == '__main__':

    # parser_for_get_list_currencies = argparse.ArgumentParser(description='Get list of currencies')
    # parser_for_get_list_currencies.add_argument("-symbols", type=str)
    # args_get_list = parser_for_get_list_currencies.parse_args()
    #
    # parser_for_convert_currencies = argparse.ArgumentParser(description='Convert currencies')
    # parser_for_convert_currencies.add_argument("-from", type=str, dest='from_currency')
    # parser_for_convert_currencies.add_argument("-to", type=str, dest='to_currency')
    # parser_for_convert_currencies.add_argument("-amount", type=int, dest='amount')
    # args_convert = parser_for_convert_currencies.parse_args()
    #
    # parser_for_history = argparse.ArgumentParser(description='History rates')
    # parser_for_history.add_argument("-from", type=str, dest='from_currency')
    # parser_for_history.add_argument("-to", type=str, dest='to_currency')
    # parser_for_history.add_argument("-start", type=int, dest='start_date')
    # parser_for_history.add_argument("-end", type=int, dest='end_date')
    # args_history = parser_for_history.parse_args()
    #
    # loop.run_until_complete(get_list_currencies(args_get_list.symbols))
    # loop.run_until_complete(convert_currencies(
    #                                             args_convert.from_currency,
    #                                             args_convert.to_currency,
    #                                             args_convert.amount
    #                                            ))
    # loop.run_until_complete(history_quotes(
    #                                         args_history.from_currency,
    #                                         args_history.to_currency,
    #                                         args_history.start_date,
    #                                         args_history.end_date
    #                                        ))
    try:
        loop.run_until_complete(convert_currencies('usd', 'eur', 1))
        loop.run_until_complete(get_list_currencies('usd'))
        loop.run_until_complete(history_quotes('usd', 'eur', '20230101', '20230110'))
    except RuntimeError:
        print('OK')
    finally:
        loop.close()
