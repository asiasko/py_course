# Homework 3.1.
hat_list = [1, 2, 3, 4, 5]
print('Length of list: ', hat_list, 'equal', len(hat_list))  # Step 0.
hat_list.insert(2,int(input("Input number for center of list:")))  # Step 1.
print('Result list: ', hat_list)
hat_list.pop()  # Step2.
print('Length of finish list: ', hat_list, 'equal', len(hat_list))  # Step 3.



# Lab 3.2.
beatles = []
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')

for i in range(2):
    beatles.append(input("Follow other members(Example:Stu Sutcliffe or Pete Best)--->"))  # Stu Sutcliffe and Pete Best.
print(beatles)
beatles.pop()
print(beatles)  # List after delete last element of list.
beatles.pop()
print(beatles)  # List after delete last element of list.
beatles.insert(0, 'Ringo Starr')
print(beatles)  # List after add Ringo Starr in start of list


# Lab 3.4.
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
print('Original list: ',my_list)
res_list = []
for value in my_list:
    if value not in res_list:
        res_list.append(value)
print('The list with unique elemens: ',res_list)

# Homework 3.3. The bubble sort video and review
list_for_sort = [14, 9, 4, 2, 8, 10]
swapped = True

print('Original list: ', list_for_sort)

while swapped:
    swapped = False
    for i in range(len(list_for_sort) - 1):
        if list_for_sort[i] > list_for_sort[i+1]:  # Compare items
            list_for_sort[i], list_for_sort[i+1] = list_for_sort[i+1], list_for_sort[i]  # Change
            swapped = True

print('Sorted list: ',list_for_sort)




# Home work 3.5 split().
li = input('put string of numbers by space:').split()
Li = [int(val) for val in li]
print('Result list:',Li)
sum_ = sum(Li)
print('Sum(list):', sum_, sep='\n')

