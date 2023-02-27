def create_array(n):
    array = []
    while(int(n)>0):
        x = int(input())
        array.append(x)
        n= int(n)-1
    return array
def bubble_sort(arr):
    n = len(arr)
    for x in range(len(arr)):
        i= 0
        while(i<n-1):
            if(arr[i]>arr[i+1]):
                temp = arr[i+1]
                arr[i+1]=arr[i]
                arr[i] = temp
                i+=1
            else:
                i+=1
        n-=1
    return arr
    
# Firstly we will create an array to be sorted 
def main():
    size = input("Size of array")
    a = create_array(size)
    #a = [2,10,4]
    fin_array = bubble_sort(a)
    print(fin_array)
    #return fin_array    
if __name__ == '__main__':
    main()