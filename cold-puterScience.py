n = int(input())
temps = input()

temp_list = temps.split()

count = 0
for i in range(0, n):
    if int(temp_list[i]) < 0:
        count += 1

print(count)
