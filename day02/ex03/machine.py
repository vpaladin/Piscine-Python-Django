import random
import beverages

class CoffeeMachine():
    def __init__(self) -> None:
        self.count = 10

    class EmptyCup(beverages.HotBeverage):
        def __init__(self) -> None:
            self.price = 0.90
            self.name = "empty cup"

        def description(self):
            description = "An empty cup?! Gimme my money back!"
            return description
    
    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.count = 10

    def serve(self, arg: beverages.HotBeverage):
        if self.count > 0:
            self.count -=1
            if random.randint(0,10) == 5:
                arg = CoffeeMachine.EmptyCup()
            return arg
        else:
            raise self.BrokenMachineException()
        
def test():
    coffeeMachine = CoffeeMachine()
    for _ in range(23):
        try:
            print(coffeeMachine.serve(random.choice(
                [beverages.Coffee(), beverages.Tea(), beverages.Cappuccino(), beverages.Chocolate()])))
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            coffeeMachine.repair()

if __name__ == '__main__':
    test()