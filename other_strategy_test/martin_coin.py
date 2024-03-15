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
        fund_list.append(fund_list[-1] + other_each_add * math.pow(add_ratio_multiple, i))
    return fund_list, fund_list[-1]


def cal_cost(decline_list, fund_list, init_price) -> (list, list):
    # f_list = fund_list[1:]
    amount_list = []
    price = init_price
    cost_list = []
    price_list = []
    decline_list_tmp = [0]
    decline_list_tmp.extend(decline_list)

    for i, obj in enumerate(zip(decline_list_tmp, fund_list)):
        add = obj[1] - fund_list[i - 1] if i > 0 else obj[1]
        price = init_price * (1 - obj[0])
        amount = add / price
        amount_list.append(amount)
        cost_list.append(obj[1] / math.fsum(amount_list))
        price_list.append(price)
        # print(price, amount, add, obj, math.fsum(amount_list), obj[1] / math.fsum(amount_list))

    return cost_list, price_list


def cal(bc: BaseConfig):
    decline_list, max_decline = cal_decline(bc.base_decline, bc.add_ratio_gap, bc.add_times)
    fund_list, max_fund = cal_fund(bc.first_add, bc.add_times, bc.other_each_add, bc.add_ratio_multiple)
    cost_list, price_list = cal_cost(decline_list, fund_list, bc.init_price)
    decline_list = [f'{d * 100}%' for d in decline_list]
    print(f'最大下跌比例:        {max_decline * 100}%')
    print(f'所需资金:            {max_fund}')
    print(f'每次下跌比例:        {decline_list}')
    print(f'每次下跌对应所需资金: {fund_list}')
    print(f'每次加仓成本变化:     {cost_list}')
    print(f'每次价格:            {price_list}')
    print(f'对应差价比例:         {[obj[0]*1.01/obj[1] for obj in zip(cost_list, price_list)]}')
    print(f'价格区间:            {bc.init_price} - {bc.init_price * (1 - max_decline)}')


if __name__ == '__main__':
    bc = BaseConfig(base_decline=0.01, init_price=8400.0, first_add=20, other_each_add=10, add_times=15, add_ratio_multiple=1.0,
                    add_ratio_gap=1.1)
    cal(bc)
