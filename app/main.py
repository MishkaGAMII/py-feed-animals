class Animal:
    def __init__(self,
                 name: str,
                 appetite: int = 0,
                 is_hungry: bool = True
                 ) -> None:
        self.name = name
        self.appetite = appetite
        self.is_hungry = is_hungry

    def feed(self) -> int:
        if self.is_hungry:
            print(f"Eating {self.appetite} food points...")
            self.is_hungry = False
            return self.appetite

        return 0

    def print_name(self) -> None:
        print(f"Hello, I'm {self.name}")


class Cat(Animal):
    def __init__(self,
                 name: str,
                 is_hungry: bool = True
                 ) -> None:
        appetite = 3
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def catch_mouse() -> None:
        print("The hunt began!")


class Dog(Animal):
    def __init__(self,
                 name: str,
                 is_hungry: bool = True
                 ) -> None:
        appetite = 7
        super().__init__(name, appetite, is_hungry)

    @staticmethod
    def bring_slippers() -> None:
        print("The slippers delivered!")


def feed_animals(animals: list[Animal]) -> int:
    return sum(animal.feed() for animal in animals)
