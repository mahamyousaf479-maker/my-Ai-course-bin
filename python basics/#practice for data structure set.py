#practice for data structure set 
bookset = {23231 , "Thick and grow rich" , "ABC Int" , 35.50 , "William Richard" , True}
print(bookset)
print(type(bookset))
print(len(bookset))
for x in bookset:
    print(x)
bookset.add("cheistry")
print('update set:', bookset)
bookset.discard(35.50)
print('update set:' , bookset)