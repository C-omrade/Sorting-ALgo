# Here we are going to implement insetion sort 
def create_array(n):
    array = []
    while(int(n)>0):
        x = int(input())
        array.append(x)
        n= int(n)-1
    return array
def insertion_sort(arr):
    #print(arr)
    for x in range(1,len(arr)):
        current_elem=arr[x]
        j= x-1
        while(arr[j]>current_elem and j>=0):
              #print(arr)
              arr[j+1] = arr[j]
              j=j-1
        arr[j+1] = current_elem
    #print(arr)
    return arr
# Firstly we will create an array to be sorted 
def main():
    size = input("Size of array")
    a = create_array(size)
    #a = [2,10,4]
    fin_array = insertion_sort(a)
    print(fin_array)
    #return fin_array    
if __name__ == '__main__':
    main()