# i = 1
# while i <=10:
#   print( 17*i)
#   i += 1

# print (" loop ending")
# n = int(input("enter number :"))
# i = 1
# while i <= 10:
#   print(n*i)
#   i +=1
num = [1,3,5,6,7,4,9,10,45,78,89]
student = ["atif","nabeel","faizi","rs"]

x = "faizi"
i = 0

while i < len(student):
    if student[i] == x:
        print("found at idx", i)
    else:
        print("finding..")
    i += 1
