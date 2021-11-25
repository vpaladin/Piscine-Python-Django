class Intern():

    def __init__(self, name="«Меня зовут? Я никто, стажер, у меня нет имени»"):
        self.name = name

    def __str__(self):
        return(self.name)
    
    class Coffee():
        def __str__(self):
            return ("This is the worst coffee you ever tasted.")

    @staticmethod
    def work():
        raise Exception("«Я просто стажер, я не могу этого сделать ...»")

    def make_coffee(self):
        coffee = Intern.Coffee()
        return coffee


if __name__ == "__main__":
    intern1 = Intern()
    intern2 = Intern("Vasya")
    print(intern1)
    print(intern2)
    try:
        intern2.work()
    except Exception as e:
        print(e)
    print(intern2.make_coffee())
