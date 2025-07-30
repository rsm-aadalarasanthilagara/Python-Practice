def calculate_mean(numbers):
    print("Calculating mean of the list:", numbers)
    if not numbers:
        return 0.0
    else:
        total_sum = 0
        mean_result = 0.0
        count = 1
        for num in numbers:
            total_sum += num
            count += 1
        mean_result = total_sum / count
        return mean_result


# test the function
print(calculate_mean([20, 30, 50]))
print(calculate_mean([]))
print(calculate_mean([1]))
