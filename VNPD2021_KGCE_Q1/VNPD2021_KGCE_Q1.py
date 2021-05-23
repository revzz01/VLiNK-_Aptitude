#Print Array
def printArraystring(string, n):
    for i in range(n):
        print(string[i], end = " ")
        
#Sort the array in ascending order
def sort(s, n):
    for i in range(1, n):
        temp = s[i]
 
        j = i - 1
        while j >= 0 and len(temp) < len(s[j]):
            s[j + 1] = s[j]
            j -= 1
 
        s[j + 1] = temp

        
        result = min(arr, key = len)
        print("Shortest string is : " + res)

#Driver Code              
if __name__ == "__main__":
    n = int(input("Enter no. of string in the array: "))
    if n > 0:
        arr = input()
        for i in range(n):
            s = input()
            arr.append(s)
    else:
        print("Invalid Input")
 
    sort(arr, n)
 
    printArraystring(arr, n)
