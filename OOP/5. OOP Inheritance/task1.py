class KK_tea:
    total_boxes = 0
    total_profit = 0

    def __init__(self, weight, price=None):
        self.weight = weight
        self.price = price if price is not None else weight * 0.5
        self.num_bags = weight // 2
        self.status = "unsold"
        KK_tea.total_boxes += 1

    def product_detail(self):
        print(f"Weight: {self.weight} gm")
        print(f"Price: {self.price} tk")
        print(f"Number of bags: {self.num_bags}")
        print(f"Status: {self.status}")

    @classmethod
    def total_sales(cls):
        print(f"Total boxes sold: {cls.total_boxes}")
        print(f"Total Profit: {cls.total_profit} tk")

    @classmethod
    def update_sold_status_regular(cls, *teas):
        for tea in teas:
            if tea.status == "unsold":
                tea.status = "sold"
                cls.total_profit += tea.price

class KK_flavoured_tea(KK_tea):
    flavour_count = {}

    def __init__(self, flavour, weight, price):
        super().__init__(weight, price)
        self.flavour = flavour
        KK_flavoured_tea.flavour_count[flavour] = KK_flavoured_tea.flavour_count.get(flavour, 0) + 1

    def product_detail(self):
        super().product_detail()
        print(f"Flavour: {self.flavour}")
        print(f"Total {self.flavour} tea: {KK_flavoured_tea.flavour_count[self.flavour]}")

    @classmethod
    def update_sold_status_flavoured(cls, *teas):
        KK_tea.update_sold_status_regular(*teas)

# Test the classes
t1 = KK_tea(250)
print("-----------------1-----------------")
t1.product_detail()
print("-----------------2-----------------")
KK_tea.total_sales()
print("-----------------3-----------------")
t2 = KK_tea(470, 100)
t3 = KK_tea(360, 75)
KK_tea.update_sold_status_regular(t1, t2, t3)
print("-----------------4-----------------")
t3.product_detail()
print("-----------------5-----------------")
KK_tea.total_sales()
print("-----------------6-----------------")
t4 = KK_flavoured_tea("Jasmine", 260, 50)
t5 = KK_flavoured_tea("Honey Lemon", 270, 45)
t6 = KK_flavoured_tea("Honey Lemon", 270, 45)
print("-----------------7-----------------")
t4.product_detail()
print("-----------------8-----------------")
t6.product_detail()
print("-----------------9-----------------")
KK_flavoured_tea.update_sold_status_flavoured(t4, t5, t6)
print("-----------------10-----------------")
KK_tea.total_sales()
