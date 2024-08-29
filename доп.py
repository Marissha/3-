def calculate_structure_sum(s):
    sum = 0
    print(f'вызывается функция на {s}')
    for i in s:
        print(f'{i=}, {sum=}')
        if isinstance(i, list):
           sum += calculate_structure_sum(i)
        if isinstance(i, dict):
            sum += calculate_structure_sum(i.keys())
            sum += calculate_structure_sum(i.values())
        if isinstance(i, int):
           sum += i
        if isinstance(i, str):
           sum += len(i)
        if isinstance(i, tuple):
            sum += calculate_structure_sum(i)
        if isinstance(i, set):
            sum += calculate_structure_sum(i)
    return sum
data_structure = [
    [1, 2, 3],
    {'a':4, 'b':5},
    (6, {'cube':7, 'drum':8}),
    'Hello',
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print('ответ: ', result)