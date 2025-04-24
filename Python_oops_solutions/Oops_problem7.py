def count_complete_subarrays(arr):
    n = len(arr)
    unique_elements = len(set(arr))
    count = 0

    for i in range(n):
        seen = set()
        for j in range(i, n):
            seen.add(arr[j])
            if len(seen) == unique_elements:
                count += 1

    return count

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 1, 3, 2]
    print("Count of complete subarrays:", count_complete_subarrays(arr))