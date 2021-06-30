
10. Kichik harflar oldinga otsin 
str1 = PyNaTive

str1 = 'PyNaTive'  
katta=""  
kichik=""  
for belgi in str1:  
    if belgi.islower():  
        kichik+=belgi  
    else: 
        katta+=belgi  
yangi_satr=kichik+katta  
print(yangi_satr)
