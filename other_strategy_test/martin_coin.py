import math


class BaseConfig(object):
    def __init__(self, all_fund=250, init_price=8000.0, base_decline=0.01, first_add=20, other_each_add=10,
                 add_times=10,
                 add_ratio_multiple=1.0, add_ratio_gap=1.0):
        self.all_fund = all_fund
        self.init_price = init_price
        self.base_decline = base_decline
        self.first_add = first_add
        self.other_each_add = other_each_add
        self.add_times = add_times
        self.add_ratio_multiple = add_ratio_multiple
        self.add_ratio_gap = add_ratio_gap


def cal_decline(base_decline, add_ratio_gap, times) -> (list, float):
    decline_list = []
    for i in range(times):
        multiple = base_decline * math.pow(add_ratio_gap, i)
        decline_list.append(decline_list[-1] + multiple if len(decline_list) > 0 else multiple)
    return decline_list, decline_list[-1]


def cal_fund(first_add, times, other_each_add, add_ratio_multiple) -> (list, float):
    fund_list = [first_add]
    for i in range(times):
        fund_list.append(other_each_add * add_ratio_multiple)
    return fund_list, math.fsum(fund_list)


def cal(bc: BaseConfig):
    decline_list, max_decline = cal_decline(bc.base_decline, bc.add_ratio_gap, bc.add_times)
    _, max_fund = cal_fund(bc.first_add, bc.add_times, bc.other_each_add, bc.add_ratio_multiple)
    print(f'最大下跌比例: {max_decline * 100}%')
    decline_list = [f'{d * 100}%' for d in decline_list]
    print(f'每次下跌比例: {decline_list}')
    print(f'所需资金: {max_fund}')
    print(f'价格区间: {bc.init_price} - {bc.init_price * (1 - max_decline)}')


if __name__ == '__main__':
    bc = BaseConfig(init_price=7600.0, first_add=20, other_each_add=10, add_times=8, add_ratio_multiple=1.1,
                    add_ratio_gap=1.2)
    cal(bc)
