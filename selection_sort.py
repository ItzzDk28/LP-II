def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        arr[i],arr[min_idx] = arr[min_idx], arr[i]

    return arr

def user_input():
	ele_nos = int(input("Enter number of elements: "))
	elements = []

	for ele in range(ele_nos):
		user_ele = int(input("Enter ele no " + str(ele) + ": "))
		elements.append(user_ele)

	return elements



if __name__ == '__main__':

	ele_lis = user_input()
	
	print("-------------------")
	print("Unsorted List: ", end=" ")
	print(ele_lis)
	print("-------------------")
	print("Sorted List: ", end=" ")
	print(selectionSort(ele_lis))
	print("\nExeution Done!")
