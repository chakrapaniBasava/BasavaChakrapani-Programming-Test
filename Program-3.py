
def generate_series(n: int):
    count = n if n % 2 == 1 else n - 1
    series = [2 * i + 1 for i in range((count + 1) // 2)]
    print(", ".join(map(str, series)))

# Example usage
a = int(input("Enter a: "))
generate_series(a)
