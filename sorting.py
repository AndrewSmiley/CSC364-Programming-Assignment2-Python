__author__ = 'Andrew'
from random import randint

def insertion_sort(array):
    sublist = [array[0]]
    for i in range(1, len(array)):
        if array[i] >= sublist[i-1]:
            sublist.append(array[i])
            continue
        if array[i] <= sublist[0]:
            sublist.insert(0, array[i])
            continue
        for j in reversed(range(0, i)):
            if array[i] >= sublist[j-1] and array [i] <=sublist[j]:
                sublist.insert(j, array[i])
                break
    return sublist
"""
// To heapify a subtree rooted with node i which is
// an index in arr[]. n is size of heap
void heapify(int arr[], int n, int i)
{
    int largest = i;  // Initialize largest as root
    int l = 2*i + 1;  // left = 2*i + 1
    int r = 2*i + 2;  // right = 2*i + 2

    // If left child is larger than root
    if (l < n && arr[l] > arr[largest])
        largest = l;

    // If right child is larger than largest so far
    if (r < n && arr[r] > arr[largest])
        largest = r;

    // If largest is not root
    if (largest != i)
    {
        swap(arr[i], arr[largest]);

        // Recursively heapify the affected sub-tree
        heapify(arr, n, largest);
    }
}

// main function to do heap sort
void heapSort(int arr[], int n)
{
    // Build heap (rearrange array)
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // One by one extract an element from heap
    for (int i=n-1; i>=0; i--)
    {
        // Move current root to end
        swap(arr[0], arr[i]);

        // call max heapify on the reduced heap
        heapify(arr, i, 0);
    }
}
"""
# def heapify(array, n, i):
#     largest = i
#     l = 2*i +1  #left
#     r = 2*i +2 #right
#     if l < n and array[l] > array[largest]:
#         largest = l
#     if r < n and array[r] > array[largest]:
#         largest = r
#     if largest != i:
#         array[i], array[largest] = array[largest], array[i]
#         heapify(array, n, i)
# def heapsort(array, n):
#     for i in range(n, -1, -1):
#         heapify(array, n, i)
#
#     for i in range(n-1, 0, -1):
#         array[0], array[i] = array[i], array[0]
#         heapify(array, i, 0)
#     return array
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in reversed(range(0, n+1)): #range(n, -1, -1):
        heapify(arr, n, i)
    for i in reversed(range(0, n)):#range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)


def radix_sort(array):
    pass

ordered= [i for i in range(1, 101)]
unordered = [randint(1, 10001) for i in range(1, 1001)]

#do insertion sort first
lst = [5,2,6,71,92]
heapSort(lst)

# insertion_sorted = insertion_sort([5,4,3,2,1])
print ""

