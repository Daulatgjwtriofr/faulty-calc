s = set()
print(type(s))
s_from_list = set([1,2,3,4])
# print(s_from_list)
s.add(2)
s.add(3)
s1 = s.union({1,2,3})
s2 = s.intersection({2,3,4,5})
print(s,s1)
# print(s,s2)
# print(max(s))
# print(min(s))
# s3 = {5,7}
# print(s.isdisjoint(s3))


####--------------- faulty calculator-----------######
 
# ###------>que.design a calculator which will correctly solve all problm expect the following 
# 45*3 = 555,  56+9 = 77, 56/6 = 4
#1 your proggram should takes operator and the two number as input from and return the result

# print("enter your number")
# num1 = int(input())
# print("enter your 2nd number")
# num2 = int(input())
# print('you put as your choice '+'+,-,*,/,%')
# num3 =input()


# if num1 == 45 and num2 ==3 and num3=='*':
#     print("555")
# elif num1 == 56 and num2 == 9 and num3=='+':
#     print("77")
# elif num1 == 56 and num2 == 6 and num3=='/':
#     print("4")
# elif num3 =='*':
#     pol = num1*num2
#     print(pol)
# elif num3 =='+':
#     pol2 = num1+num2
#     print(pol2)
# elif num3 =='/':
#     pol3 =num1 / num2
#     print(pol3)
# elif num3 =='%':
#     pol4 = num1%num2
#     print(pol4)
# elif num3 =='-':
#     pol5 = num1-num2
#     print(pol5)
# else:
#     print(" error check your input")




