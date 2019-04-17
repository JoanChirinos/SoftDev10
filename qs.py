def quicksort(arr):
    return arr if len(arr) <= 1 else quicksort([x for x in arr if x < arr[0]]) +\
           [x for x in arr if x == arr[0]] +\
           quicksort([x for x in arr if x > arr[0]])

def pythagorean_triples(n):
    return [(i, j, k) for i in range(2, n) \
                      for j in range(i, n) \
                      for k in range(j, n) if i**2 + j**2 == k**2]
                

    
