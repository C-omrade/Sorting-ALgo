#Algo -: firstly keep on dividing all the elemets to its smallest size that is 1
# Then start with merging of the elements thinking of two pointers on two lists left and right
# Then using the pointers and comparison keep on updating a new list 
# Here we divide initially such that the smallest lists firstly becomes sorted and it does not create problem for the upper lists while we are creating a new arr.

# based on divide and conquer algo
# Starting with, dividing array into each element and then merging it and joing it together.
def create_array(n):
    array = []
    while(int(n)>0):
        x = int(input())
        array.append(x)
        n= int(n)-1
    return array
# Firstly we will create an array to be sorted 
def merge_sort(arr):
    if(len(arr)>1):
        mid = len(arr)//2
        leftarr = arr[:mid]
        rightarr = arr[mid:]
        merge_sort(leftarr)
        merge_sort(rightarr)
        i=j=k=0
    
        while(i<len(leftarr) and j<len(rightarr)):
            if(leftarr[i]<rightarr[j]):
                arr[k] = leftarr[i]
                i+=1
            else:
                arr[k] = rightarr[j]
                j+=1
            k+=1
        while(i<len(leftarr)):
            arr[k] = leftarr[i]
            i+=1
            k+=1
        while(j<len(rightarr)):
            arr[k] = rightarr[j]
            j+=1 
            k+=1
        
def main():
    size = input("Size of array")
    a = create_array(size)
    #a = [2,10,4]
    #fin_array = merge_sort(a)
    merge_sort(a)
    print(a)
    #return fin_array    
if __name__ == '__main__':
    main()