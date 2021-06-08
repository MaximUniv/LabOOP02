import bisect


def longest_increasing_subsequence(elements):
    elements = list(elements)
    if not elements:
        return []

    tableau_elements = []
    tableau_indexes = []
    predecessors = []
    for i, element in enumerate(elements):
        j = bisect.bisect_left(tableau_elements, element)
        predecessors.append(tableau_indexes[j - 1] if j > 0 else None)
        if j < len(tableau_elements):
            tableau_elements[j] = element
            tableau_indexes[j] = i
        else:
            tableau_elements.append(element)
            tableau_indexes.append(i)

    lengths = []
    for i, predecessor in enumerate(predecessors):
        lengths.append(1 if predecessor is None else lengths[predecessor] + 1)

    best = max(range(len(lengths)), key=lambda i: lengths[i])
    subsequence = []
    while best is not None:
        subsequence.append(elements[best])
        best = predecessors[best]
    subsequence.reverse()
    return subsequence


print(longest_increasing_subsequence([5, 1, 4, 11, 5, 9, 2, 6, 5, 3, 5, 8, 123, 7, 9, 3]))
