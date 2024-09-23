my_list = [42, 69,  322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

i = 0
while i < len(my_list):
    if my_list[i] == 0:
        i += 1
        continue
    if my_list[i] < 0:
        i += 1
        break

    print(my_list[i])
    i += 1












#     else:
#         print('u')
# #     my = my_list
# #     == 0 == True
# # print(my)
# # break
#

# Kol = len(my_list)
# my_list1 = my_list[:]
# g = my_list1 * Kol
# if my_list1 > 0:
#     print(my_list)
#
# print(g)
# #
# # a = Kol * g
