#program of list and functions of list
list1 = [2, 3, 4, 5, 6, 7, 8, 23]
list1.append(21)
print(list1)
list2=[2,3,5,6,7]
list2.extend(list1)
print(list2)
list3=[3,8,9]
list3.insert(2,4)
print(list3)
list4=[2,4,5]
list4.remove(5)
print(list4)
list5=[2,9,8,0,8]
print(list5.count(8))
list6=[2,6,7,9]
print(list6.pop())
print(list6.pop(2))
list7=[1,2,3,4]
list7.reverse()
print(list7)
list8=[1,2,3,6,8,0]
list8.sort()
print(list8)
list9=list8.copy()
print(list9)
list10=[3,8,7]
print(list10.clear())
print(any(list9))
print(all(list9))
list11=['suman#','lukesh']
print(ascii(list11))
print(bool(6))
for i in enumerate(list9):
    print(i)
print(sum(list9))
print(min(list9))
print(max(list9))
list14=[5,3,2,7,9]
o=map(len(list14),list14)
print(o)
print(sorted(list14))
student=['suman','kalia','lukesh']
age=[8,9,77]
salary=[20000,7000,80000]
student_info=list(zip(student,age,salary))
print(student_info)
list15=[2,5,7,9,3]
list16=[i**2 for i in list15]
print(list16)