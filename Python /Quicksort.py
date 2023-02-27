def create_array(n):
    array = []
    while(int(n)>0):
        x = int(input())
        array.append(x)
        n= int(n)-1
    return array
def quick_sort(arr):
    
    if(len(arr)<2):
        return arr
    pivot = arr[0]
    leftarr = [x for x in arr[1:] if x<=pivot]
    rightarr= [x for x in arr[1:] if x>pivot]
    arr = quick_sort(leftarr)+[pivot]+quick_sort(rightarr)
    return arr
# Firstly we will create an array to be sorted 
def main():
    size = input("Size of array")
    a = create_array(size)
    #a = [2,10,4]
    fin_array = quick_sort(a)
    print(fin_array)
    #return fin_array    
if __name__ == '__main__':
    main()