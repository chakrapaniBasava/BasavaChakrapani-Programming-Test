
def generate_series(n: int):
    series = [2 * i + 1 for i in range(n)]
    print(", ".join(map(str, series)))

# Example usage
a = int(input("Enter a: "))
generate_series(a)
