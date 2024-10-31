def list_index(list1, list2):
    if len(list1) != len(list2):
        return "Lists must have the same length."
    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])
    return result

def userlist(userinput):
    numbers = input(userinput).split(",")
    return [int(num) for num in numbers]

##Do I need to define a main? Cannot get it to work putting the below in a main function to run

list1 = userlist("Enter the first list of numbers separated by comma: ")
list2 = userlist("Enter the second list of numbers separated by comma: ")
result = list_index(list1, list2)
print("Result:", result)