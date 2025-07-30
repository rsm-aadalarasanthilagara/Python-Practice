def calculate_variance(lst):
    if not lst:
        return 0.0
    else:
        # find mean
        total_count = 0
        count = 0
        mean = 0.0
        for i in lst:
            total_count += i
            count += 1
            mean = total_count / count
        # find variance
        variance = 0.0
        for i in lst:
            variance += (i - mean) ** 2
        variance = variance / count

    return variance
