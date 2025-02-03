

coords = [(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1), (8, 0)]

move_dir, idx = ['vertic', 3]
if move_dir in ['horizo', 'vertic']:
    i = {'horizo': 0, 'vertic': 1}[move_dir]
    print([coord for coord in coords if coord[i] == idx])