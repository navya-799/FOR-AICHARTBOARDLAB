def find_closest_pair(arr):
    arr.sort()  
    left, right = 0, len(arr) - 1
    closest_sum = float('inf')  
    best_pair = (None, None)
    while left < right:
        current_sum = arr[left] + arr[right]
        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            best_pair = (arr[left], arr[right])
        if current_sum < 0:
            left += 1
        else:
            right -= 1
    return best_pair, closest_sum
array = [-1, 2, 3, -4, 5]
pair, sum_closest_to_zero = find_closest_pair(array)
print(f"The pair with the sum closest to zero is: {pair} with sum {sum_closest_to_zero}")
