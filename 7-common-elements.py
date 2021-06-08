sorted_full = [0, 2, 7, 8, 7, 9, 11, 15]
sorted_sub = [2, 4, 7, 11, 15]

full_ix = 0
sub_ix = 0

while full_ix < len(sorted_full) and sub_ix < len(sorted_sub):
    curr_full = sorted_full[full_ix]
    curr_sub = sorted_sub[sub_ix]
    if curr_full == curr_sub:
        print('Common element ' + str(curr_full) + ' at index ' + str(full_ix))
        full_ix += 1
        sub_ix += 1
        continue
    if curr_full < curr_sub:
        full_ix += 1
    else:
        sub_ix += 1
