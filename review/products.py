class ListProduct:
    def __init__(self):
        self.products=[]
        #self.products=None=> khong cap so nho cho products quan ly
        #self.products=[] co cap phat o nho cho product quan ly nhung chua day data
    def add_product(self,p):
        self.products.append(p)
    def descend_price(self):
        pass
    def print_products(self):
        for p in self.products:
            print(p)
    def sort_desc_price(self):
        for i in range(0,len(self.products)):
            for j in range(i+1,len(self.products)):
                pi=self.products[i]
                pj=self.products[j]
                if pi.price<pj.price:
                    self.products[i]=pj
                    self.products[j]=pi