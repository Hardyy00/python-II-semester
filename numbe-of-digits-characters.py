string = 'Nagpur-440010'
alpha = 0
digit = 0
for c in string :
    if (c.isalpha()) :
        alpha = alpha + 1
    elif (c.isdigit()) :
        digit = digit + 1 
print("\nNo. of alphabets :",alpha)
print("\nNo. of  digits :",digit)