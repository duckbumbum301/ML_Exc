from PyQt6.QtWidgets import QApplication, QMainWindow

from review.MainWindowListProductsExt import MainWindowListProductsExt
from review.product import Product
from review.products import ListProduct

app=QApplication([])
qmain=QMainWindow()
my_window=MainWindowListProductsExt()
my_window.setupUi(qmain)

#load data
lp=ListProduct()
lp.add_product(Product("p1","coca",15,35))
lp.add_product(Product("p2","pepsi",14,25))
lp.add_product(Product("p3","sting",20,32))
lp.add_product(Product("p4","redbull",30,25))

my_window.load_products(lp)

my_window.showWindow()
app.exec()