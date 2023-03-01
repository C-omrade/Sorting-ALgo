# if values are from 0 to 1 then only it is applicable
# Create n empty buckets or lists
# Insert arr[i] into bucket[n*arr[i]] #This n*arr[i] is for keeping a check on maximum value 
# sort individual buckets using insertion sort 
# Concatenate all sorted buckets.
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
def bucket_sort(arr):
    l1 = []
    # Making empty lists depending on the size of the array
    for x in range(len(arr)):
        l1.append([])
    # Depending on the value moving the values to a particular bucket
    for x in range(len(arr)):
        val = int(len(arr)*arr[x])
        l1[val].append(arr[x])
    #applying insetion sort on each bucket
    for x in range(len(arr)):
        l1[x] = insertion_sort(l1[x])
    #concatinating the bucket
    k=0
    for i in range(len(arr)):
        for j in range(len(l1[i])):
            arr[k] = l1[i][j]
            k+=1
    return arr

# Firstly we will create an array to be sorted 
def main():
    #size = input("Size of array")
    #a = create_array(size)
    #a = [2,10,4]
    #fin_array = bucket_sort(a)
    #print(fin_array)
    #return fin_array 
    arr = [0.1,0.159,0.55,0.59,0.959,0.2,0.3]
    print(bucket_sort(arr)) 
if __name__ == '__main__':
    main()