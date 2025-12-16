# function overlapping 
def overlapping(list1, list2):
    # set1 = set(list1)
    # set2 = set(list2)
    # return not set1.isdisjoint(set2)
    for item in list1:
        if item in list2:
            return True
    return False


list1 = [1, 2, 3, 4, 5]
list2 = [5, 2, 7, 8, 9] 


if list1 and list2:
    if overlapping(list1, list2):
        print("The lists have overlapping elements.")
    else:
        print("The lists do not have overlapping elements.")

