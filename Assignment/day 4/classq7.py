# Create matrix of dim 3x4 as list of list with few fixed values

list  = [[11, 12, 13,14], 
         [21, 22, 23, 24], 
         [31, 32, 33, 34]
         ]
# print(len(list))
# print(f"list0[0] = {list[0]}")
# print(f"list1[1] = {list[1]}")
# print(f"list2[2] = {list[2]}")

t1 = ((1, 2, 3, 4),
      (5, 6, 7, 8),
      (9, 10, 11, 12)
      )
# for i in t1:
#     print(t1)
# print(f"t1[0] = {t1[0]}")
# print(f"t1[1] = {t1[1]}")
# print(f"t1[2] = {t1[2]}")
def add_sub_matrices(m1, m2):
    rows = len(m1)
    cols = len(m1[0])
    print(rows, "*" ,cols)

    addition = []
    subtraction = []

    for i in range(rows):
        add_row = []
        sub_row = []
        for j in range(cols):
            add_row.append(m1[i][j] + m2[i][j])
            sub_row.append(m1[i][j] - m2[i][j])
        addition.append(add_row)
        subtraction.append(sub_row)

    return addition, subtraction

# if __name__ == "__main__":
    add_result, sub_result = add_sub_matrices(list, t1)

    print("Addition Result:")
    for row in add_result:
        print(row)

    print("\nSubtraction Result:")
    for row in sub_result:
        print(row)
