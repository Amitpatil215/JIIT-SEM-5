no_list = [2, 6, 41, 85, 0, 3, 7, 6, 10]
N = 2

final_list = []

for i in range(0, N):
        max1 = 0
        for j in range(len(no_list)):
            if no_list[j] > max1:
                max1 = no_list[j]

        no_list.remove(max1)
        final_list.append(max1)

print(final_list)

"""
[85, 41]
"""