def Find_Min_Length(lst):
    if not lst:
        return 0
    return min(len(sublist) for sublist in lst)