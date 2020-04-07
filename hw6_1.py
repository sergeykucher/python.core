def count_positives_sum_negatives(arr):
    if not arr:
        return []
    sum_arr = [0,0]    
    for value in arr:
        if value > 0:
            sum_arr[0] += 1
        else:
            sum_arr[1] += value