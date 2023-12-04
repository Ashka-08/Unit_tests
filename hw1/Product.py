class Product:
    def __init__(self, name: str, cost: int):
        self.name = name
        self.cost = cost

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost