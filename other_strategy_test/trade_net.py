def trade_cal(start_price, start_num, trade_percent_list: list):
    start_cost = start_price * start_num * 10
    # start_high = start_low = start_price
    for i, tp in enumerate(trade_percent_list):
        low_list = []
        high_list = []
        start_high = start_low = start_price
        if tp['times'] == 0:
            continue

        for _ in range(tp['times']):
            start_low *= (1 - tp['percent']/100.0)
            start_high *= (1 + tp['percent']/100.0)
            start_cost += tp['opt_num'] * 10 * start_low
            low_list.append('%.2f' % start_low)
            high_list.append('%.2f' % start_high)

        print(f'net {i}: [{low_list[-1]} ~ {high_list[-1]}], (size: {tp["percent"]}, trade_times: {tp["times"]})')
    print(f'Half-Cost: {start_cost}')


if __name__ == '__main__':
    start_price = 123.92
    start_num = 58
    trade_percent_list = [
        {"percent": 1, "times": 4, "opt_num": 2},
        {"percent": 1, "times": 0, "opt_num": 2},
        {"percent": 4, "times": 1, "opt_num": 2},
        {"percent": 7, "times": 2, "opt_num": 2},
    ]
    trade_cal(start_price, start_num, trade_percent_list)
