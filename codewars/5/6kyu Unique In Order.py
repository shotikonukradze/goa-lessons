def unique_in_order(sequence):
    if not sequence:
        return []
    result = []
    result.append(sequence[0])
    for i in range(1, len(sequence)):
        if sequence[i] != sequence[i-1]:
            result.append(sequence[i])
    
    return result
