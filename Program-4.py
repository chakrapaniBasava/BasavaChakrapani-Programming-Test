def count_multiples(numbers: list):
    result = {i: 0 for i in range(1, 10)}
    for num in numbers:
        for i in range(1, 10):
            if num % i == 0:
                result[i] += 1
    return result

# Example usage
input_list = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
print(count_multiples(input_list))
