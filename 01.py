with open('inputs/01.txt', 'r') as f:
    depths = [int(depth.strip()) for depth in f.readlines()]
    inc = 0
    inc_roll = 0
    for i, depth in enumerate(depths):
        if i > 0 and depth > depths[i-1]:
            inc += 1
        if i > 2:
            cur_roll = depth + depths[i-1] + depths[i-2]
            prev_roll = depths[i-1] + depths[i-2] + depths[i-3]
            if cur_roll > prev_roll:
                inc_roll += 1
    print(f'Part 1 solution: {inc}')
    print(f'Part 2 solution: {inc_roll}')
