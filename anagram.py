s = input("\nEnter a string : ").lower()
s1 = input("Enter another string : ").lower()
if sorted(s) == sorted(s1) :
    print("\nIts an anagram")
else :
    print("\nIts not an anagram")