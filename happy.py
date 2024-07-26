print('calculate happyness -')
n, m = map(int, input().split())
array = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

# Calculate happiness
for element in array:
    if element in A:
        happiness += 1
    if element in B:
        happiness -= 1

print('happyness=', happiness)           