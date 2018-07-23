def distance(strand_a, strand_b):
    hamming_distance = 0
    if len(strand_a) != len(strand_b): raise ValueError(f'{len(strand_a)} != {len(strand_b)}')
    for index, value in enumerate(strand_a):
        if value != strand_b[index]: hamming_distance += 1
    return hamming_distance
