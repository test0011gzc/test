# 数字转为千分位
def convert_str_contain_comma_v2(num):
    if num == '-':
        return num
    split_num = str(num).split('.')
    int_part = split_num[0]
    decimal_part = '.' + split_num[1] if len(split_num) > 1 else ''

    result = ''
    count = 0
    for i in int_part[::-1]:
        count += 1
        result += i
        if count % 3 == 0:
            result += ','
    return result[::-1].strip(',') + decimal_part


