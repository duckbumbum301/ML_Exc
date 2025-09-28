from review.product import Product
from review.products import ListProduct

lp=ListProduct()
lp.add_product(Product("p1","coca",15,35))
lp.add_product(Product("p2","pepsi",14,25))
lp.add_product(Product("p3","sting",20,32))
lp.add_product(Product("p4","redbull",30,25))
lp.print_products()
lp.sort_desc_price()
print("---List Products - Sort Desc Price:---")
lp.print_products()