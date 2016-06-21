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
public static void heapSort(int[] a){
	int count = a.length;

	//first place a in max-heap order
	heapify(a, count);

	int end = count - 1;
	while(end > 0){
		//swap the root(maximum value) of the heap with the
		//last element of the heap
		int tmp = a[end];
		a[end] = a[0];
		a[0] = tmp;
		//put the heap back in max-heap order
		siftDown(a, 0, end - 1);
		//decrement the size of the heap so that the previous
		//max value will stay in its proper place
		end--;
	}
}

public static void heapify(int[] a, int count){
	//start is assigned the index in a of the last parent node
	int start = (count - 2) / 2; //binary heap

	while(start >= 0){
		//sift down the node at index start to the proper place
		//such that all nodes below the start index are in heap
		//order
		siftDown(a, start, count - 1);
		start--;
	}
	//after sifting down the root all nodes/elements are in heap order
}

public static void siftDown(int[] a, int start, int end){
	//end represents the limit of how far down the heap to sift
	int root = start;

	while((root * 2 + 1) <= end){      //While the root has at least one child
		int child = root * 2 + 1;           //root*2+1 points to the left child
		//if the child has a sibling and the child's value is less than its sibling's...
		if(child + 1 <= end && a[child] < a[child + 1])
			child = child + 1;           //... then point to the right child instead
		if(a[root] < a[child]){     //out of max-heap order
			int tmp = a[root];
			a[root] = a[child];
			a[child] = tmp;
			root = child;                //repeat to continue sifting down the child now
		}else
			return;
	}
}
"""
def sift_down(array, start, end):
    root = start
    while (start *2+1) <= end:
        child = root *2+1
        if (child + 1) <= end and array[child] < array[child +1]:
            child = child+1
        if array[root] < array[child]:
            tmp = array[root]
            array[root] = array[child]
            array[child] = tmp
            root = child
        else:
            return



def heapify(array,count):
    start = (count -2 )/2
    while start >=0:
        sift_down(array, start, count-1)
        start = start-1
def heap_sort(array):
    count = len(array)
    heapify(array, count)
    end= count-1
    while end > 0:
        tmp = array[end]
        array[end]= array[0]
        array[0] =tmp
        sift_down(array, 0, end-1)
        end = end-1


def radix_sort(array):
    pass

ordered= [i for i in range(1, 101)]
unordered = [randint(1, 10001) for i in range(1, 1001)]

#do insertion sort first
heap_sorted = heap_sort([5,2,6,71,92])
# insertion_sorted = insertion_sort([5,4,3,2,1])
print ""

