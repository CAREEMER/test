sample_list = [1, 6, 42, 2, 0, 6, 0, 23, 0]

for idx, item in enumerate(sample_list):
    if item == 0:
        sample_list.pop(idx)

print(sample_list)