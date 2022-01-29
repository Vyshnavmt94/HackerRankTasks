def first_last(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i + 1 < len(arr) and arr[i] == target:
                i += 1
            return [start, i]
    return [-1, -1]


if __name__ == '__main__':
    print(first_last([2, 4, 5, 5, 5, 7, 9, 9], 5))
