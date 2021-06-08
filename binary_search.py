def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (high + low) // 2
        print(f"Searching for x in {arr[low:high+1]}, middle = {arr[mid]}", end=", ")
        if arr[mid] < x:
            print("x > middle element")
            low = mid + 1
        elif arr[mid] > x:
            print("x < middle element")
            high = mid - 1
        else:
            print("x = middle element")
            return mid

    return -1


def binary_search2(arr, x):
    low = 0
    high = len(arr) - 1

    while high >= low:
        i = low + round((high-low) * (x-arr[low]) / (arr[high]-arr[low]))
        print(f"Searching for x in {arr[low:high+1]}, i-th element = {arr[i]}", end=", ")
        if x < arr[i]:
            print("x < i-th element")
            high = i - 1
        elif x > arr[i]:
            print("x > i-th element")
            low = i + 1
        else:
            print("x = i-th element")
            return i

    return -1


def binary_search3(arr, x):
    low = 0
    high = len(arr)
    mid = 0

    if x < arr[0]:
        return -1
    if x >= arr[-1]:
        return high-1

    while low < high:
        mid = (high + low) // 2

        if x < arr[mid]:
            if x > arr[mid-1]:
                return mid
            high = mid
        elif x > arr[mid]:
            if x < arr[mid+1]:
                return mid
            low = mid + 1
        else:
            return mid

    return mid


old = 10


def binary_search4(arr, x):
    n = len(arr)
    global old

    if x < arr[0]:
        return -1
    if x >= arr[-1]:
        return n - 1

    if 0 <= old < n-1:
        inc = 1
        low = high = old
        if x < arr[old]:
            while True:
                low -= inc
                if low <= 0:
                    low = 0
                    break
                if arr[low] <= x:
                    break
                high = low
                inc <<= 1
        else:
            while True:
                high += inc
                if high >= n-1:
                    high = n-1
                    break
                if arr[high] > x:
                    break
                low = high
                inc <<= 1

    else:
        low = 0
        high = n - 1

    while low < high - 1:
        node = (low+high) >> 1
        if x >= arr[node]:
            low = node
        else:
            high = node

    old = low
    return old


def test():
    return


if __name__ == "__main__":
    array = [1, 5, 10, 16, 17, 20, 26]
    element = 0

    result = binary_search4(array, element)
    print("res: ", result)

