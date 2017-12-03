N, D = input().split(' ')
N = int(N)
D = int(D)

arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr_t = (arr[D:] + arr[:D])

for a in arr_t:
    print(a, end = ' ')
