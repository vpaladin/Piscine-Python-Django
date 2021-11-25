class HotBeverage():
    def __init__(self) -> None:
        self.price = 0.30
        self.name = "hot Beverage"

    def description(self):
        description = "Just some hot water in a cup."
        return description

    def __str__(self) -> str:
        str = (f"name: {self.name}\n"
        f"price: {self.price}\n"
        f"decription: {self.description()}")
        return(str)


class Coffee(HotBeverage):
    def __init__(self) -> None:
        self.name = "coffee"
        self.price = 0.40

    @staticmethod
    def description():
        description = "A coffee, to stay awake."
        return description

class Chocolate(HotBeverage):
    def __init__(self) -> None:
        self.name = "chocolate"
        self.price = 0.50

    @staticmethod
    def description():
        description = "Chocolate, sweet chocolate..."
        return description
        
class Cappuccino(HotBeverage):
    def __init__(self) -> None:
        self.name = "cappuccino"
        self.price = 0.45

    @staticmethod
    def description():
        description = "Un po’ di Italia nella sua tazza!"
        return description

class Tea(HotBeverage):
    def __init__(self) -> None:
        super().__init__()
        self.name = "Tea"


coffee = Coffee()
tea = Tea()
chok = Chocolate()
capuc = Cappuccino()
print(coffee)
print(tea)
print(chok)
print(capuc)