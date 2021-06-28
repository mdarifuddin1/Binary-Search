

# Happy coding ,code by Md Arif uddin
# This example of Binary Search code 
# coding time 11:17 Pm ,date 6/28/2021

pos = -1
list = [1, 4, 56, 67 ,78 ,99,101]
print(list)
n = 99   # if you change value of n our output will be changed 


def BinarySearch(list, n):
    lower= 0
    upper = len(list)-1

    while lower <= upper:
        mid = (lower+upper) // 2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid]<n:
                lower = mid
            else:
                upper= mid+1

    return False


if BinarySearch(list, n):
   print("The Found the value of index: ", pos)
else:
    print("This value is not Found of index")

# Right now my output is ,[1, 4, 56, 67, 78, 99, 101]
#The Found the value of index:  5

