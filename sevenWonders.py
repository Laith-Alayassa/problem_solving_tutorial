s = input()


t_counter, c_counter, g_counter = 0, 0, 0

for char in s:
    if char == "C":
        c_counter += 1
    if char == "G":
        g_counter += 1
    if char == "T":
        t_counter += 1

print(t_counter, c_counter, g_counter)
total = t_counter ** 2 + c_counter ** 2 + g_counter ** 2

total += min(t_counter, g_counter, c_counter) * 7

print(total)
