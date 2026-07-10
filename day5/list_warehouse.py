#products in warehouse
l=["Laptop","Mouse","Keyboard"] 
#adding product to warehouse

l.append("Monitor")
# combining warehoue 2 to warehouse1
new_products=["Tablet","Webcam"]
l.extend(new_products)

#removing product from warehouse 
l.remove("Mouse")

# product removed from warehouse after shipping
l.remove("Webcam")
#couning laptops in warehouse
print(l.count('Laptop'))
#
print(l)
#Find position of Monitor in warehouse
print(l.index("Monitor")+1)
#sorting the product
print(sorted(l))
#reversing the lisr
lt=l.reverse()
print(l)

#creating alist copy and delteing the temporary
list_copy=l.copy()
print(list_copy)
del list_copy


