def calculate_variance(numbers):
    print("Calculating variance of the list:", numbers)
    if not numbers:
        return 0.0
    mean = sum(numbers) / len(numbers)
    squared_diffs = [(x - mean) ** 2 for x in numbers]
    return sum(squared_diffs) / len(numbers)


# test the function
print(calculate_variance([20, 30, 50]))
print(calculate_variance([]))
print(calculate_variance([1]))
