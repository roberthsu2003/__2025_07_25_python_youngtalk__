class Person:
    def __init__(self,name):
        self.name = name #建立attribute

def main():
    p1 = Person("robert")
    print(p1.name)

    p2 = Person("jenny")
    print(p2.name)

if __name__ == "__main__":
    main()