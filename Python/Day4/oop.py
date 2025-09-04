class books:
    def __init__(self,title,author,price,discount):
        self.title=title
        self.author=author
        self.price=price
        self.discount=discount

    def Discountcal(self):
        return self.price - (self.price*self.discount/100)
    def display(self):
        print(f"Title: {self.title}\nAuthor : {self.author}\nPrice : {self.price}\nPrice after Discount: {self.Discountcal():.3f}")




object1=books("AI Basics","John Smith",34.24,10)
object1.display()

