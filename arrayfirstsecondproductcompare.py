def process_series(arr):
    n = len(arr)

    # Ensure even-length array
    if n % 2 != 0:
        print("Error: Please enter an even number of elements.")
        return

    half = n // 2
    first_half, second_half = arr[:half], arr[half:]

    # Compute product of halves
    product_first = 1
    product_second = 1

    for num in first_half:
        product_first *= num
    for num in second_half:
        product_second *= num

    # Print original series
    print("Original series:", *arr)

    # Sort based on condition
    if product_second < product_first:
        arr.sort()  # Ascending order
    else:
        arr.sort(reverse=True)  # Descending order

    # Print modified series
    print("Modified series:", *arr)


# Taking user input
try:
    series = list(map(int, input("Enter numbers (even count, space-separated): ").split()))

    process_series(series)  # Process the series

except ValueError:
    print("Error: Invalid input! Please enter only numbers.")

