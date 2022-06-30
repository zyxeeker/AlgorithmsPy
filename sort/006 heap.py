

class Array:
    def __init__(self, data):
        self.data = data
        self.heap_size = len(data)

# 
def Parent(i):
    return int(i/2);

def Left(i):
    return 2*i

def Right(i):
    return 2*i+1

def Swap(e1, e2):
    return e2, e1

def MaxHeapify(array, i):
    l = Left(i)
    r = Right(i)
    largest = 0

    if l <= array.heap_size and array.data[l-1] > array.data[i-1]:
        largest = l
    else:
        largest = i
    if r <= array.heap_size and array.data[r-1] > array.data[largest-1]:
        largest = r

    if largest != i:
        array.data[i-1], array.data[largest-1] = Swap(array.data[i-1], array.data[largest-1])
        print("PROCESS: ", array.data)
        MaxHeapify(array, largest)

def BuildMaxHeap(array):
    A = Array(array)
    for i in range(int(A.heap_size/2), 0, -1):
        MaxHeapify(A, i)
    return A

def HeapSort(array):
    BuildMaxHeap(array)
    # for i in range()

a = [4,1,3,2,16,9,10,14,8,7]
print("SRC: ", a)

a_dst = BuildMaxHeap(a)
print("DST: ", a_dst.data)