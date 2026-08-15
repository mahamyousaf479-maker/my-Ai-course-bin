#practice for data structure dictonary
bookdictionay = {"price": 50 , "book": "chemistry", "writer": "William Richard", "Isonsale":True}
print(bookdictionay)
print(type(bookdictionay))
print(len(bookdictionay))
for x in bookdictionay:
    print(bookdictionay[x])

print(bookdictionay["price"])
print(bookdictionay)
bookdictionay["city"] = "LA"
bookdictionay["price"] = 60
print(bookdictionay)

bookdictionay.pop("city")
print(bookdictionay)
bookdictionay.clear()
print(bookdictionay)