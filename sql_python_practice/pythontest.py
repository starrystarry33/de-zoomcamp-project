1. 按支付方式汇总 fare（dict 累加）
trips = [
    {"payment_type": 1, "fare_amount": 12.5},
    {"payment_type": 2, "fare_amount": 8.0},
    {"payment_type": 1, "fare_amount": 20.0},
    {"payment_type": 2, "fare_amount": 15.5},
]
写一个函数，返回一个 dict：key 是 payment_type，value 是该支付方式的 fare 总额。
预期结果：{1: 32.5, 2: 23.5}



def sum_amount(dic):
    result = default_dic()
    for n, v in dic.items():
            result[n] += v
       
"""
day 8
Python：输入是一个 trip dict 的列表（每个 dict 有 payment_type 和 fare_amount），
写一个函数返回 {payment_type: {"count": 订单数, "avg_fare": 平均消费保留2位小数}}。参数名用 lst。

lst = [
    {"payment_type": 1, "fare_amount": 10.5},
    {"payment_type": 1, "fare_amount": 20.0},
    {"payment_type": 2, "fare_amount": 15.25},
    {"payment_type": 2, "fare_amount": 8.75},
    {"payment_type": 1, "fare_amount": 12.0},
]


1.建个空 dict result = {}，按 payment_type 分组
2.for trip in lst: 遍历每个 trip
   取出 trip["payment_type"] 和 trip["fare_amount"]
3.如果这个 payment_type 第一次出现，先在 result 里初始化 {"count": 0, "total": 0}（total 先存着，最后算平均用）
count 加 1，total 加上这单的 fare
循环结束后再遍历一遍 result：avg = total / count，用 round(avg, 2) 保留两位小数
返回 {payment_type: {"count": ..., "avg_fare": ...}}

"""

def fuc(lst):
    result = {} # payment_type{count:, avg:}

    for trip in lst:
        fare = trip["fare_amount"]
        payment_type = trip["payment_type"]
        if payment_type not in result:
            result[payment_type] = {"count": 0, "total": 0}
        result[payment_type]["count"] += 1
        result[payment_type]["total"] += fare

    for ptype in result:
        count = result[ptype]["count"]
        total = result[ptype]["total"]
        result[ptype] = {"count": count, "avg_fare": round(total / count, 2)}

    return result


    
"""
day10
写一个函数 summarize_by_pickup(trips)，返回一个 dict：
key 是 PULocationID
value 是 {"count": 订单数, "avg_amount": 平均 total_amount（保留2位小数）, "total_distance": trip_distance 总和（保留2位小数）}
只保留订单数 > 100 的地点，结果按订单数降序排列（提示：Python 里排序用 sorted + key）
trips = [
    {"PULocationID": 132, "total_amount": 15.5, "trip_distance": 2.3},
    {"PULocationID": 132, "total_amount": 22.0, "trip_distance": 4.1},
    {"PULocationID": 45,  "total_amount": 8.75, "trip_distance": 1.2},
    # ... 很多条
]
"""
