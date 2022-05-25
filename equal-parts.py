s = input("\nEnter a string : ")
n = int(input("\nEnter number of parts : "))
e = len(s)//n
s1 = [s[i:i+e] for i in range(0,len(s),e)]
print(s1)


