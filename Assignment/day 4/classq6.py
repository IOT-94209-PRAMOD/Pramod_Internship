#. Given stock prices over 7 days: prices = [105, 110, 108, 112, 115, 116, 114].
prices = [105, 110, 108, 112, 115, 116, 114]

# for i in range( ):
avg = []

for i in range(len(prices) - 2):
    avg = sum(prices[i:i+3]) / 3
    avg.append(round(avg, 2))

print(avg)
