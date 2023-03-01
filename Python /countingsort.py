#range is predefined 
#Create an array with len as max value
#Now traverse throught the list
#keep on increasing the counter of each element as soon as you find it in a list
def counting_sort(arr):
    maxelement = max(arr)
    minelement = min(arr)
    total_elem = maxelement-minelement+1
    l1 = [0 for i in range(total_elem)]
    l2 = [0 for i in range(total_elem)]
    for x in arr:
        l1[x-min(arr)]+=1
    k=0
    for x in range(len(l1)):
        for j in range(l1[x]):
            arr[k] = x+minelement
            k+=1
    
def main():
    arr = [4,11,10,9,9,4,5,5,6]
    counting_sort(arr)
    print(arr)

if __name__ == '__main__':
    main()