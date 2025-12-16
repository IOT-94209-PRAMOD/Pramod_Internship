# class q8.py

def average(data):
    rows = len(data)
    cols = len(data[0])
    list = []

    for c in range(cols):
        total = 0
        for r in range(rows):
            total += data[r][c]
        list.append(total / rows)

    return list


# Input
data = ((10, 10, 10, 12),
        (30, 45, 56, 45),
        (81, 80, 39, 32),
        (1, 2, 3, 4))


print(average(data))
