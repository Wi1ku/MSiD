import apiBroker
import time
import datetime
import numpy as np

pairs = [
    "BTC-USD",
    "ETH-USD",
    "LTC-USD"
]


# YYYY-MM_DD format
def convert_dates(human_readable_date):
    (yyyy, mm, dd) = (human_readable_date.split("-"))
    date = datetime.datetime(int(yyyy), int(mm), int(dd))
    return int(date.timestamp())


def sim(trading_pair, starting_date, ending_date):
    starting_date = convert_dates(starting_date)
    ending_date = convert_dates(ending_date)
    if ending_date >= time.time() or starting_date >= ending_date:
        raise ValueError("Wrong date range")
    if trading_pair not in pairs:
        raise ValueError("Wrong trading pair")
    data = apiBroker.get_data(trading_pair, starting_date, ending_date)
    print(count_rise_probability(data))


def count_rise_probability(data):
    a = 0
    total_diff = 0
    for record in data:
        diff = float(record['open']) - float(record['close'])
        record['diff'] = np.abs(diff)
        if diff > 0:
            a += diff
        total_diff += record['diff']
    print(a)
    print(total_diff)

    return a / total_diff


if __name__ == '__main__':
    sim("BTC-USD", "2020-05-18", "2020-05-24")
