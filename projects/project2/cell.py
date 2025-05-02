
class Cell:
    def __init__(self, is_alive: bool= False) -> None:
        self.is_alive = is_alive

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Cell):
            return False
        return self.is_alive == other.is_alive


        

