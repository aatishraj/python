def partial_reverse(a, i, j):
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return a

def reverseList(A, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    reverseList(A, start + 1, end - 1)

vector = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
r_vector = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
print vector
print "Normal Way:"
partial_reverse(vector, 2, 5)
print vector
print "Reccursive Way:"
reverseList(r_vector, 1, 4)
print r_vector
